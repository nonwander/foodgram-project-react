import { Container, Title, Main} from '../../components'
import styles from './styles.module.css'
import { Redirect } from 'react-router-dom'
import MetaTags from 'react-meta-tags'
import zen_python from '../../images/zen_of_python.jpg'

const About_tech = () => {

  return <Main>
    <Container>
      <MetaTags>
        <title>Технологии</title>
        <meta name="description" content="Продуктовый помощник - Технологии" />
        <meta property="og:title" content="Технологии" />
      </MetaTags>
      <Title title='Технологии, используемые в проекте' />
        <img src={zen_python} />
        <br/><br/>
        <hr WIDTH="95%" ALIGN="center" SIZE="3"></hr>
        <h1>Python | Django | DRF | PostgreSQL | Nginx | gunicorn | docker | GitHub | Yandex.Cloud | JS | React</h1>
        <br/><br/>
    </Container>
  </Main>
}

export default About_tech
