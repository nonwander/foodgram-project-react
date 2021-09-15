import { Container, Title, Main} from '../../components'
import styles from './styles.module.css'
import { Redirect } from 'react-router-dom'
import MetaTags from 'react-meta-tags'
import me_before from '../../images/about/Mebefore.jpg'
import yapost from '../../images/about/YaPost.jpg'
import ya_hello from '../../images/about/YaPraktikum_hello.jpg'
import on_start from '../../images/about/YaPraktikum_On_start.jpg'
import end_of_base from '../../images/about/YaPraktikum_End_of_Base.jpg'
import final_2020 from '../../images/about/YaPraktikum_Final2020.jpg'


const About_author = () => {

  return <Main>
    <Container>
      <MetaTags>
        <title>Об авторе проекта</title>
        <meta name="description" content="Продуктовый помощник - Об авторе проекта" />
        <meta property="og:title" content="Об авторе проекта" />
      </MetaTags>
      <Title title='Об авторе проекта' />
      <table className={styles.table_about}>
      <tr>
        <td>
          <b>Где-то в 2014 году..</b>
          <br /><br />Я и водогрейный котёл:
          <br />боевое крещение на моей первой работе!
          <br /><br /><strong>Немыкин Евгений Васильевич</strong>
          <br />1990 г.р.
          <br />образование: инженер АСУ ТП
          <br /><br /><b>Навыки:</b>
          <br />разбираюсь в устройстве газогорелочного оборудования
          <br />умею проводить установку и наладку агрегатов
        </td>
        <td><img src={me_before} width='500'/></td>
      </tr>
    </table>
    <hr WIDTH="95%" ALIGN="center" SIZE="3"></hr>
    <table className={styles.table_about}>
    <tr>
      <td>
        <b>Начало..</b>
        <br /><b>30.08.20 в 11:51</b>
        <br /><br /><img src={yapost} alt="E-mail" width="50"/>
        <br />Подтверждаем регистрацию в Яндекс.Практикуме
      </td>
      <td>
        <img src={ya_hello} alt="Hello, Ya.Praktikum" width="500px"/>
      </td>
    </tr>
    </table>
    <hr WIDTH="95%" ALIGN="center" SIZE="3"></hr>
    <table className={styles.table_about}>
    <tr>
      <td>
        <b>На старт!</b>
        <br /><b>22.09.20 в 13:40</b>
        <br /><br /><img src={yapost} alt="E-mail" width="50px"/>
        <br />Поздравляем с началом обучения в Яндекс.Практикуме
        <br />Это будет интересно! Но у меня нет совсем времени!
      </td>
      <td>
        <img src={on_start} alt="Start!" width="500px"/>
      </td>
    </tr>
    </table>
    <hr WIDTH="95%" ALIGN="center" SIZE="3"></hr>
    <table className={styles.table_about}>
    <tr>
      <td>
        <b>Первая победа!</b>
        <br /><b>26.09.20 в 20:22</b>
        <br /><br /><img src={yapost} alt="E-mail" width="50px"/>
        <br />Вы прошли курс — поздравляем!
        <br /><br /><b><h2>Мой стальной зад победил! Мозг ему в помощь!</h2></b>
        <br /><br /><h2>Теперь я:</h2>
        <br />умею дописывать новые функции в готовый код;
        <br />могу пользоваться несколькими популярными библиотеками в Python;
        <br />знаю, что такое HTTP и зачем он нужен;
        <br />умею отправлять запросы внешним сервисам и получать от них ответы;
        <br />не пугаюсь проблем — я решил много задач и поборол массу ошибок!
      </td>
      <td>
        <img src={end_of_base} alt="End of Base!" width="500px"/>
      </td>
    </tr>
    </table>
    <hr WIDTH="95%" ALIGN="center" SIZE="3"></hr>
    <table className={styles.table_about}>
    <tr>
      <td>
        <b>Python!</b>
        <br /><b>30.12.20 в 19:15</b>
        <br /><br /><img src={yapost} alt="E-mail" width="50px"/>
        <br />2020 – всё!
        <br />Прошло 3 месяца и 0 дней. За это время пройдено 29 тем и выполнено 161 задание.
        <br /><br />Python - кайф!
      </td>
      <td>
        <img src={final_2020} alt="Final 2020!" width="500px"/>
      </td>
    </tr>
    </table>
    <h4>продолжение следует...</h4>
    </Container>
  </Main>
}

export default About_author
