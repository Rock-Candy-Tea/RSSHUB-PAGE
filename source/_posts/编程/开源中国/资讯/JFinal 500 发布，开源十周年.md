
---
title: 'JFinal 5.0.0 发布，开源十周年'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4520'
author: 开源中国
comments: false
date: Thu, 05 May 2022 02:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4520'
---

<div>   
<div class="content">
                                                                                            <p>    这一年多以年来工作繁忙，上一次发版还是去年一月份的事了，这次趁着五一长假，发布 5.0.0 版，纪念一下 jfinal 开源十周年。</p> 
<p>    5.0.0 版本中较为重要的功能来源于公司库存管理的现实需求，该项目采用前后分离开发模式，前后端 json 交互产生了 json 注入 action 方法参数的需求。</p> 
<p>    开启 json 解析配置可自动解析 json 数据并注入 action 形参：</p> 
<pre><code class="language-java">me.setResolveJsonRequest(true);</code></pre> 
<p>  假定请求 json 格式如下：</p> 
<pre><code class="language-java">&#123;
  "name": "信息论",
  "publisher": "清华出版社"
&#125;</code></pre> 
<p>     在 action 中的接受方式如下：</p> 
<pre><code class="language-java">public void search(String name, String publisher) &#123;
  renderJson("msg", "接收到参数:" + name + "," + publisher);
&#125;</code></pre> 
<p>    对象类型必然也是支持的：</p> 
<pre><code class="language-java">&#123;
  "book": &#123;
     "name": "信息论",
     "publisher": "清华出版社"
   &#125;
&#125;</code></pre> 
<p>     在 action 中的接受方式如下：</p> 
<pre><code class="language-java">public void search(Book book) &#123;
  renderJson("msg", "接收到参数:" + book.getName() + "," + book.getPublisher());
&#125;</code></pre> 
<p>     另一个比较重要的功能是 #para 指令添加了对 sql like、in 子句的支持，大致用法如下：</p> 
<pre><code class="language-java">### 一般用法，第二个参数传入 "like"、"in" 参数即可
select * from t title like #para(title, "like")
select * from t title like #para(title, "in")

### like 类型第一个参数支持 int 类型
select * from t title like #para(0, "like")

### like 支持左侧与右侧百分号用法
select * from t title like #para(title, "%like")
select * from t title like #para(title, "like%")

### 警告：对于 in 子句，如果 #para 第一个参数是 int 型，并且 java 代码针对 Object... 参数传入的是数组
select * from t id in #para(0, "in")

### 那么 java 代码中要将 Object... 处的参数强制转成 Object，否则参数传递不正确
Integer[] idArray = &#123;1, 2, 3&#125;;
Db.template("findByIdArray", (Object)idArray).find();</code></pre> 
<p>    该功能在没有引入新指令的情况下，通过扩展现有 #para 指令实现，简洁、学习成本低。</p> 
<p>    再一个实用功能是 enjoy 引擎添加了 optional chain 操作符，用法如下：</p> 
<pre><code class="language-java"># 当 article 为 null 时不对 title 进行取值，而是直接返回 null
article?.title

# 可用于方法调用
article?.getTitle()

# 可级联操作
page?.list?.size()

# 可用在方法调回之后，以下代码在 getList() 返回 null 时可避免抛出异常
page?.getList()?.size()</code></pre> 
<p>    由于 enjoy 是极简设计，实现此功能只用了 30 行代码。该功能一开始我是拒绝的，用上以后，嗯，挺香！</p> 
<p>    再一个比较贴心的功能是 Db.update(...)、Db.batchUpdate(...) 支持 modifyFlag 机制，仅更新修改过的字段，该功能以前只在 Model 中被支持。</p> 
<p>    由于 jfinal 已开源十年，诞生十一年，已经非常完善，所以需要新增、改进的功能已经非常之少，除了上面较为实用的功能外，其它细致打磨可下载 changelog 进行查看：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjfinal.com%2Fdownload%2Fnow%3Ffile%3Djfinal-5.0.0-changelog.txt" target="_blank">jfinal-5.0.0-changelog.txt</a>  </p> 
<p>    时光飞逝，至简永恒，jfinal 开源十周年之际祝你 bug 少头发多，也希望 jfinal 在下个十年里继续陪伴着你！</p> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            