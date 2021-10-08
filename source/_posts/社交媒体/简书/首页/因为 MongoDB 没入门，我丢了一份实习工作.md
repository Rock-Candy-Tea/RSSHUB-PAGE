
---
title: '因为 MongoDB 没入门，我丢了一份实习工作'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/1179389-bddce91555c7bc37.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/1179389-bddce91555c7bc37.png'
---

<div>   
<p>有时候不得不感慨一下，系统升级真的是好处多多，不仅让我有机会重构了之前的烂代码，也满足了我积极好学的虚荣心。你看，<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FNPJkMy5RppyFk9QhzHxhrw" target="_blank">Redis 入门</a>了、<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FZjsZxle7m_dfmVwVkq2ayg" target="_blank">Elasticsearch 入门</a>了，这次又要入门 MongoDB，感觉自己变秃的同时，也变强大了。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="200" data-height="200"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-bddce91555c7bc37.png" data-original-width="200" data-original-height="200" data-original-format="image/png" data-original-filesize="36528" src="https://upload-images.jianshu.io/upload_images/1179389-bddce91555c7bc37.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>小伙伴们在继续阅读之前，我必须要声明一点，我对 MongoDB 并没有进行很深入的研究，仅仅是因为要用，就学一下。但作为一名负责任的技术博主，我是花了心思的，这篇入门教程，小伙伴们读完后绝对会感到满意，忍不住点赞。</p>
<p>当然了，小伙伴们遇到文章中有错误的地方，不要手下留情，可以组团过来捶我，但要保证一点，不要打脸，我怕毁容。</p>
<h3>01、MongoDB 是什么</h3>
<blockquote>
<p>MongoDB 是一个基于分布式的文件存储数据库，旨在为 Web 应用提供可扩展的高性能数据存储解决方案。</p>
</blockquote>
<p>以上引用来自于官方，不得不说，解释得文绉绉的。那就让我来换一种通俗的说法给小伙伴们解释一下，MongoDB 将数据存储为一个文档（类似于 JSON 对象），数据结构由键值对组成，类似于 Java 中的 Map，通过 key 的方式访问起来效率就高得多，对吧？这也是 MongoDB 最重要的特点。</p>
<p>MongoDB 提供了企业版（功能更强大）和社区版，对于我们开发者来说，拿社区版来学习和使用就足够了。MongoDB 的驱动包很多，常见的编程语言都有覆盖到，比如说 Java、JavaScript、C++、C#、Python 等等。</p>
<p>很多知名的互联网公司都在用 MongoDB，比如说谷歌、Facebook、eBay 等等。总之，值得信赖，小伙伴们放心入门，技多不压身啊，就当是给自己一次学习的机会。</p>
<h3>02、安装 MongoDB</h3>
<p>MongoDB 针对不同的操作系统有不同的安装包，我们这篇入门的文章就以 Windows 为例吧。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="755" data-height="395"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-31e9ea0321379de7.png" data-original-width="755" data-original-height="395" data-original-format="image/png" data-original-filesize="22035" src="https://upload-images.jianshu.io/upload_images/1179389-31e9ea0321379de7.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>官网下载地址如下：</p>
<p><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fwww.mongodb.com%2Fdownload-center%2Fcommunity" target="_blank">https://www.mongodb.com/download-center/community</a></p>
<p>最新的版本是 4.2.6，我选择的是安装版，msi 格式的，264M 左右。下载完就可以双击运行安装，傻瓜式的。</p>
<p>建议选择「Custom」自定义安装，如下图所示。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="493" data-height="360"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-fe094fdee35b36fe.png" data-original-width="493" data-original-height="360" data-original-format="image/png" data-original-filesize="22459" src="https://upload-images.jianshu.io/upload_images/1179389-fe094fdee35b36fe.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>以服务模式运行，并配置好数据和日志目录，如下图所示。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="493" data-height="360"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-e21c8ff0668650ce.png" data-original-width="493" data-original-height="360" data-original-format="image/png" data-original-filesize="19248" src="https://upload-images.jianshu.io/upload_images/1179389-e21c8ff0668650ce.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>建议取消勾选安装 MongoDB 的图形化客户端工具，否则安装速度慢到你想要去扣会手机。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="493" data-height="360"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-cd8e9cdd1d8aaa16.png" data-original-width="493" data-original-height="360" data-original-format="image/png" data-original-filesize="22936" src="https://upload-images.jianshu.io/upload_images/1179389-cd8e9cdd1d8aaa16.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>安装完成后进入到 bin 目录下，双击 mongo.exe 文件就可以连接到 MongoDB 服务了。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="902" data-height="512"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-464b1f7cedc947e3.png" data-original-width="902" data-original-height="512" data-original-format="image/png" data-original-filesize="52487" src="https://upload-images.jianshu.io/upload_images/1179389-464b1f7cedc947e3.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>1）MongoDB 的默认端口号为 27017。</p>
<p>2）MongoDB 的版本号为 4.2.6。</p>
<p>默认会连接到 test 文档（相当于数据），可以通过 db 命令查询。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="92" data-height="56"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-bd22104dc3c65575.png" data-original-width="92" data-original-height="56" data-original-format="image/png" data-original-filesize="577" src="https://upload-images.jianshu.io/upload_images/1179389-bd22104dc3c65575.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>还可以运行一些简单的算术运算：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="75" data-height="44"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-196805cb16513fc1.png" data-original-width="75" data-original-height="44" data-original-format="image/png" data-original-filesize="642" src="https://upload-images.jianshu.io/upload_images/1179389-196805cb16513fc1.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>那如何停止服务呢？可以直接点击右上角的 X 号——粗暴、壁咚。</p>
<h3>03、安装 Robo 3T</h3>
<p>Robo 3T 提供了对 MongoDB 和 SCRAM-SHA-256（升级的 mongo shell）的支持，是一款轻量级的 MongoDB 客户端工具。</p>
<p>下载地址如下：</p>
<p><a href="https://links.jianshu.com/go?to=https%3A%2F%2Frobomongo.org%2Fdownload" target="_blank">https://robomongo.org/download</a></p>
<p>最新的版本是 1.3，选择 zip 格式进行下载，23M 左右。下载完成后，解压就行了。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1124" data-height="642"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-a514cf612a2507fe.png" data-original-width="1124" data-original-height="642" data-original-format="image/png" data-original-filesize="103733" src="https://upload-images.jianshu.io/upload_images/1179389-a514cf612a2507fe.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>包目录不再一一解释了，进入 bin 目录下，双击运行 robo3t.exe 文件，启动 Robo 3T 客户端。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="654" data-height="394"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-ebe204e56a5ea06a.png" data-original-width="654" data-original-height="394" data-original-format="image/png" data-original-filesize="11699" src="https://upload-images.jianshu.io/upload_images/1179389-ebe204e56a5ea06a.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>点击「Create」创建一个 MongoDB 的连接。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="452" data-height="315"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-8be7ec01b23a3eca.png" data-original-width="452" data-original-height="315" data-original-format="image/png" data-original-filesize="11623" src="https://upload-images.jianshu.io/upload_images/1179389-8be7ec01b23a3eca.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>连接成功后，就可以操作 MongoDB 了。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="927" data-height="415"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-8370a3b787d3756e.png" data-original-width="927" data-original-height="415" data-original-format="image/png" data-original-filesize="49477" src="https://upload-images.jianshu.io/upload_images/1179389-8370a3b787d3756e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>（不过，小伙伴们这时候也不太知道该怎么操作，毕竟 MongoDB 的一些相关概念还不清楚，无从下手啊）</p>
<h3>04、MongoDB 的相关概念</h3>
<p>随着互联网的极速发展，用户数据也越来越庞大，NoSQL 数据库的发展能够很好地处理这些大的数据，MongoDB 是 NoSQL 数据库中的一个典型的代表。</p>
<p>说到这，可能有些小伙伴们还不知道 NoSQL 是啥意思，我简单解释一下。NoSQL 可不是没有 SQL 的意思，它实际的含义是 Not Only SQL，也就是“不仅仅是 SQL”，指的是非关系型数据库，和传统的关系型数据库 MySQL、Oracle 不同。</p>
<p>MongoDB 命名源于英文单词 hu<strong>mongo</strong>us，意思是「巨大无比」，可以看得出 MongoDB 的野心。MongoDB 的数据以类似于 JSON 格式的二进制文档存储：</p>
<pre><code>&#123;
    name: "沉默王二",
    age: 18,
    hobbies: ["写作", "敲代码"]
&#125;
</code></pre>
<p>在进行下一步之前，需要先来理解 MongoDB 中的几个关键概念，比如说什么是集合，什么是文档，什么是字段等等。MongoDB 虽然是非关系型数据库，但和关系型数据库非常相似。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="670" data-height="274"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-4dc7b7e0e40d058d.png" data-original-width="670" data-original-height="274" data-original-format="image/png" data-original-filesize="17893" src="https://upload-images.jianshu.io/upload_images/1179389-4dc7b7e0e40d058d.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>看完上面这幅图（图片来源于好朋友 macrozheng 的文章），是不是瞬间就清晰了？</p>
<h3>05、在 Java 中使用 MongoDB</h3>
<p>有些小伙伴可能会问，“二哥，我是一名 Java 程序员，我该如何在 Java 中使用 MongoDB 呢？”这个问题问得好，这就来，这就来。</p>
<p>第一步，在项目中添加 MongoDB 驱动依赖：</p>
<pre><code><dependency>
    <groupId>org.mongodb</groupId>
    <artifactId>mongodb-driver-sync</artifactId>
    <version>4.0.3</version>
</dependency>
</code></pre>
<p>第二步，新建测试类 MongoDBTest：</p>
<pre><code class="java">public class MongoDBTest &#123;
    public static void main(String[] args) &#123;
        MongoClient mongoClient = MongoClients.create();
        MongoDatabase database = mongoClient.getDatabase("mydb");
        MongoCollection<Document> collection = database.getCollection("test");

        Document doc = new Document("name", "沉默王二")
                .append("age", "18")
                .append("hobbies", Arrays.asList("写作", "敲代码"));
        collection.insertOne(doc);

        System.out.println("集合大小：" +collection.countDocuments());

        Document myDoc = collection.find().first();
        System.out.println("文档内容：" + myDoc.toJson());
    &#125;
&#125;
</code></pre>
<p>1）MongoClient 为 MongoDB 提供的客户端连接对象，不指定主机名和端口号的话，默认就是“localhost”和“27017”。</p>
<p>如果小伙伴想自定义主机名和端口号的话，也可以通过字符串的形式：</p>
<pre><code class="java">MongoClient mongoClient = MongoClients.create("mongodb://localhost:27017");
</code></pre>
<p>是不是感觉和 MySQL 的连接字符串挺像的？</p>
<p>2）<code>getDatabase()</code> 方法用于获取指定名称的数据库，如果数据库已经存在，则直接返回该 DB 对象（MongoDatabase），否则就创建一个再返回（省去了判空的操作，非常人性化）。</p>
<p>3）<code>getCollection()</code> 方法用于获取指定名称的文档对象，如果文档已经存在，则直接返回该 Document 的集合对象，否则就创建一个再返回（和 <code>getDatabase()</code> 方法类似）。</p>
<p>有了文档对象（MongoCollection<Document>）后，就可以往里面添加具体的文档内容了。</p>
<pre><code class="java"> Document doc = new Document("name", "沉默王二")
                .append("age", "18")
                .append("hobbies", Arrays.asList("写作", "敲代码"));
</code></pre>
<p>Document 对象来源于 org.bson 包下，可以在实例化该对象之后通过 <code>append()</code> 方法添加对应的键值对，非常方便，就像 String 类的 <code>append()</code> 方法一样。</p>
<p>有了文档对象后，就可以通过 <code>insertOne()</code> 方法将文档添加到集合当中了。</p>
<p>4）<code>countDocuments()</code> 方法用于获取集合中的文档数目。</p>
<p>5）要查询文档，可以通过 <code>find()</code> 方法，它返回一个 <code>FindIterable</code> 对象，<code>first()</code> 方法可以返回当前集合中的第一个文档对象。</p>
<p>好了，来看一下程序的输出结果：</p>
<pre><code>集合大小：1
文档内容：&#123;"_id": &#123;"$oid": "5ebcaa76465cab3f18b93e1a"&#125;, "name": "沉默王二", "age": "18", "hobbies": ["写作", "敲代码"]&#125;
</code></pre>
<p>完全符合我们的预期，perfect！</p>
<p>也可以通过 Robo 3T 查看“mydb”数据库，结果如下图所示。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="927" data-height="355"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-038a2821d082cc54.png" data-original-width="927" data-original-height="355" data-original-format="image/png" data-original-filesize="44835" src="https://upload-images.jianshu.io/upload_images/1179389-038a2821d082cc54.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h3>06、鸣谢</h3>
<p>好了，我亲爱的小伙伴们，以上就是本文的全部内容了，是不是看完后很想实操一把 MongoDB，赶快行动吧！如果你在学习的过程中遇到了问题，欢迎随时和我交流，虽然我也是个菜鸟，但我有热情啊。</p>
<p>另外，如果你想写入门级别的文章，这篇就是最好的范例。</p>
<p>我是沉默王二，一枚有趣的程序员。如果觉得文章对你有点帮助，请微信搜索「 <strong>沉默王二</strong> 」第一时间阅读，回复【<strong>666</strong>】更有我为你精心准备的 500G 高清教学视频（已分门别类）。</p>
<blockquote>
<p>本文 <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fqinggee%2Fitwanger.github.io" target="_blank">GitHub</a> 已经收录，有大厂面试完整考点，欢迎 Star。</p>
</blockquote>
<p><strong>原创不易，莫要白票，请你为本文点个赞吧</strong>，这将是我写作更多优质文章的最强动力。</p>
  
</div>
            