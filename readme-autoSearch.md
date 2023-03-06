<div>
  <p>O código é composto por uma classe chamada <code>GooglePlacesAPI</code> e uma função chamada <code>start()</code>. A classe <code>GooglePlacesAPI</code> é responsável por realizar consultas à API do Google Places para obter informações sobre empresas em uma determinada localização e com determinadas palavras-chave. Já a função <code>start()</code> é responsável por utilizar a classe <code>GooglePlacesAPI</code> para realizar uma busca por empresas com base em uma determinada localização, raio de busca e palavras-chave, e salvar os resultados em um arquivo JSON.</p>
  <p>A seguir, são apresentados os métodos e variáveis presentes na classe <code>GooglePlacesAPI</code>:</p>
  <ul>
    <li><code>__init__(self)</code>: Este método é executado quando um objeto da classe é criado. Ele utiliza a função <code>get_key()</code> do módulo <code>utils</code> para obter a chave da API do Google Places e armazená-la na variável <code>self.api_key</code>.</li>
    <li><code>search_places(self, location, radius, keywords)</code>: Este método realiza a consulta à API do Google Places para obter informações sobre as empresas em uma determinada localização e com determinadas palavras-chave. Ele recebe como parâmetros a localização (no formato "latitude,longitude"), o raio de busca em metros e uma lista de palavras-chave. O método retorna uma lista de resultados (dicionários contendo informações sobre as empresas) ou None em caso de erro. O método realiza a consulta para a primeira página de resultados e, em seguida, continua consultando páginas adicionais até que não haja mais resultados disponíveis. O método espera 10 segundos entre cada consulta.</li>
    <li><code>get_place_details(self, place_id)</code>: Este método recebe como parâmetro o ID de uma empresa (obtido a partir dos resultados da consulta) e realiza uma nova consulta à API do Google Places para obter informações detalhadas sobre a empresa, como nome, endereço, telefone e site. O método retorna um dicionário com essas informações.</li>
  </ul>
  <p>A seguir, é apresentada a função <code>start()</code>:</p>
  <ul>
    <li><code>start(location, radius, keywords, user_id)</code>: Esta função é responsável por realizar uma busca por empresas com base em uma determinada localização, raio de busca e palavras-chave. Ela recebe como parâmetros a localização (no formato "latitude,longitude"), o raio de busca em metros, uma lista de palavras-chave e um ID de usuário. A função utiliza a classe <code>GooglePlacesAPI</code> para realizar a busca e salvar os resultados em um arquivo JSON. A função retorna None.</li>
  </ul>
  <p>O processo de busca realizado pela função <code>start()</code> é realizado da seguinte maneira:</p>
  <ol>
    <li>Cria uma instância da classe <code>GooglePlacesAPI</code>.</li>
    <li>Obtém a data da busca como um timestamp.</li>
    <li>Realiza a busca por empresas utilizando a API do Google Places para cada palavra-chave presente na lista <code>keywords</code>.
    <li>Para cada resultado da busca, extrai as informações detalhadas da empresa utilizando o método <code>get_place_details()</code> da classe GooglePlacesAPI.</li>
    <li>Salva os resultados da busca em um arquivo JSON com um nome aleatório gerado pela função <code>secrets.token_urlsafe()</code>.</li>
    <li>Lê o arquivo JSON e imprime seus conteúdos.</li>
    <li>Em caso de erro durante a busca, o programa imprime uma mensagem de erro e retorna <code>None</code>.</li>
  </ol>
</div>