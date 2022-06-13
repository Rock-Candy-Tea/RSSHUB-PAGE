
---
title: '搞大数据，Java 工程师需要掌握哪些知识？'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/1179389-72c4808a2be1026c.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/1179389-72c4808a2be1026c.png'
---

<div>   
<blockquote>
<p>先看再点赞，给自己一点思考的时间，微信搜索【<strong>沉默王二</strong>】关注这个有颜值却假装靠才华苟且的程序员。<br>
本文 <strong>GitHub</strong> <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fitwanger%2Fitwanger.github.io" target="_blank">github.com/itwanger</a> 已收录，里面还有一线大厂整理的面试题，以及我的系列文章。</p>
</blockquote>
<p>题目是一名叫“截然不同”的同学私信我的一个问题，原话是，“搞大数据，java 需要掌握哪些技术点？”，我稍微调整了一下。必须得承认一点，我本人没有搞过大数据，所在这方面的经验为零。</p>
<p>但同学既然问了，咱就不能假装不知道啊，虽然真的是不知道。但要变强，就必须无所畏惧，迎难而上，对吧？</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="342" data-height="323"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-72c4808a2be1026c.png" data-original-width="342" data-original-height="323" data-original-format="image/png" data-original-filesize="108525" src="https://upload-images.jianshu.io/upload_images/1179389-72c4808a2be1026c.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>幸好我身边有一些朋友是做大数据的，我可以向他们请教，了解清楚后，我现在就把他们给我的建议整理一下发出来，希望给有需求的同学们一点帮助。</p>
<h3>01、大数据的就业方向有哪些？</h3>
<p>现实点，我们掌握任何技能都是为了就业，为了能够找份工作糊口；立志不打工的同学们请绕行哈。</p>
<p>那大数据的就业方向都有哪些呢？</p>
<ul>
<li><p>大数据工程师</p></li>
<li><p>大数据科学家</p></li>
<li><p>数据分析师</p></li>
</ul>
<p>那针对这些不同的就业方向，都需要哪些技能呢？我们来一一的分析下。</p>
<h3>02、大数据工程师的技能要求</h3>
<p>大数据工程师的门槛相对其他两个较低一些，所以同学们可以重点关注一下这个方向。</p>
<p>先说一些必备的技能吧。</p>
<ul>
<li><p>对 Java 虚拟机有着深入的研究，推荐书籍，周志明的《深入理解 Java 虚拟机》。</p></li>
<li><p>对 Java 并发掌握得很透彻，推荐书籍，《Java 并发编程实战》。</p></li>
<li><p>掌握 Hadoop。Hadoop 是一款支持数据密集型分布式应用程序并以 Apache 2.0 许可协议发布的开源软件框架，可以使应用程序与成千上万的独立计算的电脑和 PB 级的数据连接起来，整个 Hadoop “平台”还包括 MapReduce、Hadoop 分布式文件系统（HDFS）。</p></li>
<li><p>掌握 HBase。HBase 是一个开源的非关系型分布式数据库，是 Hadoop 项目的一部分，运行于 HDFS 文件系统之上，对稀疏文件提供极高的容错率。</p></li>
<li><p>掌握 Hive。Hive 是一个建立在 Hadoop 架构之上的数据仓库，能够提供数据的精炼，查询和分析。</p></li>
<li><p>掌握 Kafka。Kafka 的目标是为处理实时数据提供一个统一、高吞吐、低延迟的平台。</p></li>
<li><p>掌握 Storm。Storm 是一个分布式计算框架，使用用户创建的“管”和“螺栓”来定义信息源和操作，允许批量、分布式处理流式数据。</p></li>
<li><p>了解 Scala。Scala 是一门多范式的编程语言，设计初衷是要集成面向对象编程和函数式编程的各种特性。可以和 Java 兼容，运行在 Java 虚拟机上。</p></li>
<li><p>掌握 Spark。Spark 是一个开源集群运算框架，相对于 Hadoop 的 MapReduce 会在运行完工作后将中介数据存放到磁盘中，Spark 使用了存储器内运算技术，能在数据尚未写入硬盘时即在存储器内分析运算。</p></li>
<li><p>会用 Linux。推荐书籍，鸟哥的《Linux 私房菜》。</p></li>
</ul>
<p>再来说一些高阶的技能吧。</p>
<ul>
<li><p>会用 Python。</p></li>
<li><p>会用 R 语言。</p></li>
<li><p>精通算法和数据结构。</p></li>
</ul>
<h3>03、大数据科学家的技能要求</h3>
<p>“科学家”，这个 title 听起来就很牛逼，不会出乎同学们的意料，我小时候的梦想之一除了成为一名作家之外，就是成为一名“科学家”。</p>
<p>那大数据科学家，要求的技能就会超出绝大多数普通人的能力。首先，要对“统计机器学习方法”有着很深入的研究，既要会预测，还要能解释为什么要这样预测，对吧？</p>
<p>如果要预测股票是涨还是跌，就必须得有一套可以解释给客户听的理论，还要有一套预测方法，让程序能够按照这个方法去执行，并得出预期的结论。</p>
<p>现如今，数据已经不值钱了，哪里都是大量的数据，值钱的是通过对这些数据进行分析，得出指导性的建议——这就要求科学家要有数据处理的能力。</p>
<p>不多说了，这方面的要求非常高，最起码也得考个研究生吧。</p>
<h3>04、数据分析师的技能要求</h3>
<p>数据分析也可以细分为两个领域，一个类似产品经理，更注重业务，对业务能力要求比较高；一个偏向数据挖掘，更注重技术，对算法和数据结构要求比较高。</p>
<p>那不管是产品经理还是做数据挖掘，SQL 是必知必会的，因为数据分析师每天都要处理海量的数据，而这些数据来自哪呢？就是数据库。那怎么把数据从数据库中取出来呢？SQL 语句（<code>select * from xxx</code>，哈哈），别无其他。</p>
<p>那还需要什么技能呢？统计学基础，对，没错，数据和时间的关系，数据的动态分布，数据的最大值、最小值、平均值，这些都需要一定的统计学基础。</p>
<p>当然了，做数据分析最好的编程语言是 R 语言或者 Python，所以还需要学习一下这两门语言。不过，有了 Java 作为基础，学 Python 就会更容易些，因为 Python 本身的语言更简洁。（R 语言主要用于统计分析、绘图、数据挖掘）</p>
<p>推荐两本书吧，《深入浅出数据分析》和《精益数据分析》。</p>
<h3>05、最后</h3>
<p>好了，我已经把要学习的技能告诉同学们了，接下来，就靠同学们自己的修行了。看书，或者网上找资料（按照关键字去搜索），都可以，关键就看你愿不愿意沉下心，去花时间钻研了。</p>
<p>执行力，很重要，对吧？</p>
<hr>
<p>我是沉默王二，一枚有颜值却假装靠才华苟且的程序员。<strong>关注即可提升学习效率，别忘了三连啊，点赞、收藏、留言，我不挑，奥利给🌹</strong>。</p>
<p>注：如果文章有任何问题，欢迎毫不留情地指正。</p>
<p>如果你觉得文章对你有些帮助，欢迎微信搜索「<strong>沉默王二</strong>」第一时间阅读，回复关键字「<strong>小白</strong>」可以免费获取我肝了 4 万+字的 《Java 小白从入门到放肆》2.0 版；本文 <strong>GitHub</strong> <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fitwanger%2Fitwanger.github.io" target="_blank">github.com/itwanger</a> 已收录，欢迎 star。</p>
  
</div>
            