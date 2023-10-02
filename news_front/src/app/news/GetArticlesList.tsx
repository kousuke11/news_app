type Article = {
    id: number;
    title: string;
    company: string;
};

const getArticles = async () => {
    const response = await fetch('http://127.0.0.1:8000/Articles/');
    const articles: Article[] = await response.json();
    return articles;
};

const ArticlesList = async () => {
    const articles = await getArticles();
// console.log(articles,"test")
    return (
      <div>
        <h1>ユーザー一覧</h1>
                 <ul>{articles && articles.results.map((article) => {return <li> {article.title}</li>})}</ul>
      </div>
    );
};

export default ArticlesList;
