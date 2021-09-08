from django.core.validators import MinValueValidator
from django.db import models

from users.models import CustomUser


class Tag(models.Model):
    name = models.CharField(
        max_length=10,
        unique=True
    )
    color = models.CharField(
        max_length=7,
        verbose_name='Цвет тега',
        unique=True
    )
    slug = models.SlugField(
        max_length=10,
        unique=True
    )

    class Meta:
        ordering = ('slug',)
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        constraints = [
            models.UniqueConstraint(
                fields=['slug'],
                name='unique_slug'
            )
        ]

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=200, verbose_name='ingredient name')
    measurement_unit = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'

    def __str__(self):
        return self.name


class Recipe(models.Model):

    name = models.CharField(max_length=200, verbose_name='recipe title')
    image = models.ImageField(
        upload_to='recipes/',
        verbose_name='recipe image',
        help_text='Картинка рецепта',
    )
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='recipes',
        verbose_name='recipe author', help_text='Автор рецепта',
    )
    text = models.TextField(
        help_text='Текстовое описание рецепта', verbose_name='recipe text',
    )
    ingredients = models.ManyToManyField(
        Ingredient, through='IngredientsRecipe',
        related_name='recipes',
        verbose_name='list of ingredients',
        help_text='Список ингредиентов',
    )
    tags = models.ManyToManyField(
        Tag, through='TagsRecipe',
        related_name='recipes',
        help_text='Выберите тэг',
    )
    cooking_time = models.PositiveSmallIntegerField(
        help_text='Время приготовления, мин',
        validators=[MinValueValidator(
            1, 'Время приготовления не может быть меньше 1 мин'
        )],
    )
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True, db_index=True
    )

    class Meta:
        ordering = ("-pub_date",)

    def __str__(self):
        return self.name


class IngredientsRecipe(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='recipe_ingredients'
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='recipe_ingredients'
    )
    amount = models.PositiveSmallIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        help_text='Количество ингредиента',
    )

    class Meta:
        verbose_name = 'Ingredient in recipe'
        verbose_name_plural = 'Ingredients in recipe'
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='unique_recipe'
            )
        ]


class TagsRecipe(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)


class FavoriteRecipe(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='favorite_recipes'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        blank=False, null=False,
        related_name='favorite_recipes'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'user'],
                name='unique_favorite'
            )
        ]


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='shopping_cart'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shopping_cart'
    )

    class Meta:
        verbose_name = 'Shopping cart'
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'user'],
                name='unique_recipe_cart'
            )
        ]
