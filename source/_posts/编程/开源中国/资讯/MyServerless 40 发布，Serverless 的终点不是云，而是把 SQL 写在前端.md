
---
title: 'MyServerless 4.0 发布，Serverless 的终点不是云，而是把 SQL 写在前端'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-4b5d43506d142bdd619a9b8e967c9058ee4.png'
author: 开源中国
comments: false
date: Mon, 04 Jul 2022 09:09:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-4b5d43506d142bdd619a9b8e967c9058ee4.png'
---

<div>   
<div class="content">
                                                                                            <p>本次更新内容：<br> 1. 所有远程方法原来只有一种同步阻塞式调用方法，现在改成每个方法都有4种变体形式，可以有“异步返回JSON”、“异步返回值”、“同步返回JSON”、“同步返回值”四种调用方式，详见下面的使用说明。<br> 2.演示项目SQL方法新增executeSQL、qryString两个方法，前端不光可以用SQL查询，还可以直接用SQL执行插入、删除和更新。<br> 3.签权接口类有变动，返回值是一个字符串而不是boolean类型，可参考示例项目的ProjectTokenSecurity.java实现。<br> 4. 删除原来的示例，改成以ReactMRP实际项目为唯一的演示项目，参见 <a href="https://gitee.com/drinkjava2/reactmrp">ReactMRP</a>(码云)或 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdrinkjava2%2Freactmrp" target="_blank">ReactMRP</a>(Github)，它的界面截图如下：</p> 
<p><img height="645" src="https://oscimg.oschina.net/oscnet/up-4b5d43506d142bdd619a9b8e967c9058ee4.png" width="1031" referrerpolicy="no-referrer"></p> 
<p><img height="725" src="https://oscimg.oschina.net/oscnet/up-0e4d6f33954549601c1eec694ee721044a6.png" width="1196" referrerpolicy="no-referrer"></p> 
<h3>附：MyServerless简介 | Description</h3> 
<p>MyServerless项目原名为GoSqlGo，表示可以直接在前端写SQL的意思，后来考虑到它的开发模式有点类似于serverless，后端不参与业务，而是将业务转给前端来开发，所以项目更名为MyServerless。</p> 
<p>MyServerless与通常大厂的Serverless服务相比，主要区别是：<br> 1.通常的Serverless是将代码放在云服务器上管理和运行，而MyServerless则是直接将SQL或Java源码写在前端，由前端负责保存和维护。  <br> 2)云Serverless服务不区分开发期和布署期，而MyServerless因为安全原因，分为开发和布署两个阶段，开发期源码写在前端，布署期利用工具将前端的源码和SQL抽取到后端。</p> 
<h3>使用</h3> 
<p>以下使用介绍基于实际示范项目ReactMRP展开，该项目主页位于这里：<a href="https://gitee.com/drinkjava2/reactmrp">ReactMRP</a>, 它把所有业务都写在前端，目前正在开发中，已完成登录和用户管理模块。 基于MyServerless的项目分为后端和前端两部分，开发阶段要同时启动后端和前端服务。</p> 
<h2>后端启动</h2> 
<p>运行ReactMRP的backend目录下的run-server.bat即可启动后端的MyServerless服务，服务启动后会自动打开浏览器访问 <a href="https://gitee.com/link?target=http%3A%2F%2Flocalhost%3A8001">http://localhost:8001</a></p> 
<h2>前端启动</h2> 
<p>运行frontend目录下的: npm install (仅第一次运行)<br> run_npm_start.bat 启动完成后会自动打开浏览器访问 <a href="https://gitee.com/link?target=http%3A%2F%2Flocalhost%3A3000">http://localhost:3000</a></p> 
<h2>打包和发布</h2> 
<ol> 
 <li>运行backend目录下的go-backend.bat，把SQL和Java抽取到后端，以实现安全性。</li> 
 <li>运行npm run build 生成发布包，并上传到生产服务器</li> 
</ol> 
<h3>方法说明 | Methods</h3> 
<p>在前端引入myserverless.js这个javascript文件后，就可以直接在前端调用以下方法执行后端业务：</p> 
<pre><span>$java(String, Object...) 在后端执行Java，第一个参数是Java源码，后续参数是业务参数，在Java源码里用$1,$2...来代表。  </span>
<span>$javaTx(String, Object...) 在后端执行Java并开启事务，如果有异常发生，事务自动回滚。  </span>
<span>$qryString(String, Object...) 将SQL查询结果的第一行第一列值转为字符串返回，第一个参数是SQL，后面是SQL参数，下同  </span>
<span>$qryObject(String, Object...) 将SQL查询结果的第一行第一列值对象返回，第一个参数是SQL，后面是SQL参数，下同  </span>
<span>$qryArray(String, Object...)  返回SQL查询的第一行数据，以Javascript数组对象格式返回  </span>
<span>$qryArrayList(String, Object...)  返回多行查询结果，以数组列表格式返回    </span>
<span>$qryTitleArrayList(String, Object...)  返回多行查询结果，以数组列表格式返回,第一行内容是各个列的标题  </span>
<span>$qryMap(String, Object...) 返回SQL查询的第一行数据，为Map 格式  </span>
<span>$qryMapList(String, Object...)  返回SQL查询的多行数据，为List格式</span>
<span>$qryEntity(String, Object...)  返回第一行数据为实体对象，SQL写法是实体类名+逗号+SQL, 示例:$qryEntity(`#admin a.b.Demo, select * from demo`); </span>
<span>$qryEntityList(String, Object...)  返回多行数据为List<实体>对象，SQL写法是实体类名+逗号+SQL, 示例:$qryEntityList(`#public a.b.Demo, select * from demo`);   </span>
<span>$executeSql(String, Object...) 执行一个SQL，返回SQL影响行数  </span></pre> 
<p>注意事项:<br> 1.以上方法Java源码或SQL文本，要使用键盘ESC下方的单引号，这是Javascript的特殊引号，支持多行文本。<br> 2.以上方法并不是MyServerless自带的，而是项目自定义的，用户对每个项目可以自定义和登记自己的方法，具体细节请参见项目src/main/resources/template下的方法模板和InitConfig类。<br> 3.每个方法都要起一个方法ID，方法ID名允许重复，方法ID的作用是为了权限配置。例如下面这个方法定义了一个名为ReadUserAmount的方法ID</p> 
<pre><span> $java('#ReadUserAmount </span>
<span>    import abc.DemoUser; </span>
<span>    return new DemoUser().loadById($1).getAmount();</span>
<span> ', 123); </span></pre> 
<p>4.方法默认是异步的，返回值是一个json对象，如 &#123;code:200, data:"123", msg:""&#125; 5.每个方法可在前面加前缀改变它的返回值, 每个方法有4种变体：</p> 
<pre><span>        $java(`#xxxx return 123;`);  // 异步方法，返回 &#123;code:200, data:123, msg:""&#125;，返回后要在promise的then方法里接收值</span>
<span>    data$java(`#xxxx return 123;`);  // 异步方法，返回 json的data字段，即123这个值， 返回后要在promise的then方法里接收值</span>
<span>    sync$java(`#xxxx return 123;`);  // 同步阻塞方法，返回 &#123;code:200, data:123, msg:""&#125;</span>
<span>syncData$java(`#xxxx return 123;`);  // 同步阻塞方法，返回 json的data字段，即123这个值</span></pre> 
<p>下面以一个实例来解说如何在前端使用MyServerless：</p> 
<pre><span>import * as my from "@/myserverless/myserverless.js"</span>

<span>export function tableList(query) &#123; </span>
<span>   return my.data$java(`#public</span>
<span>            Map m=(Map) $1;</span>
<span>            Object[] sql=new Object[]&#123;" from sample where 1=1 ",</span>
<span>                    noBlank(" and title like ?","%",m.get("title"),"%"),</span>
<span>                    notBlank(" and star=?",  m.get("star")),</span>
<span>                    notBlank(" and status=?", m.get("status"))</span>
<span>                    &#125;;</span>
<span>            List items=DB.qryMapList("select * ",sql,  pagin((int)m.get("pageNumber"), (int)m.get("pageSize")));</span>
<span>            int total=DB.qryIntValue("select count(*) ",sql);</span>
<span>            m.clear();</span>
<span>            m.put("items", items);</span>
<span>            m.put("total", total);</span>
<span>            return m;</span>
<span>      `, query);</span></pre> 
<p>1.首先在js/ts/jsx文件里引入myserverless.js<br> 2.方法ID为public，说明这个方法的用户权限是public，即无需登录即可使用，但是因为是动态代码，实际只有两种情况才允许执行，即以developer权限登录的用户，或代码已抽取并布署到服务器上。<br> 3.这个方法传入了一个参询对象query, 在java方法里<span><span><span><span><span><span>1</span><span><span><span><span>代</span></span></span></span><span><span><span><span>表</span></span></span></span><span><span><span><span>这</span></span></span></span><span><span><span><span>第</span></span></span></span><span><span><span><span>一</span></span></span></span><span><span><span><span>个</span></span></span></span><span><span><span><span>参</span></span></span></span><span><span><span><span>数</span></span></span></span><span><span><span><span>，</span></span></span></span><span><span><span><span>这</span></span></span></span><span><span><span><span>段</span></span></span></span><span><span><span><span>代</span></span></span></span><span><span><span><span>码</span></span></span></span><span><span><span><span>逻</span></span></span></span><span><span><span><span>辑</span></span></span></span><span><span><span><span>是</span></span></span></span><span><span><span><span>根</span></span></span></span><span><span><span><span>据</span></span></span></span><span><span><span><span>参</span></span></span></span><span><span><span><span>数</span></span></span></span><span><span><span><span>动</span></span></span></span><span><span><span><span>态</span></span></span></span><span><span><span><span>分</span></span></span></span><span><span><span><span>页</span></span></span></span><span><span><span><span>查</span></span></span></span><span><span><span><span>询</span></span></span></span><span><span><span><span>，</span></span></span></span><span><span><span><span>返</span></span></span></span><span><span><span><span>回</span></span></span></span><span><span><span><span>列</span></span></span></span><span><span><span><span>表</span></span></span></span><span><span><span><span>和</span></span></span></span><span><span><span><span>符</span></span></span></span><span><span><span><span>合</span></span></span></span><span><span><span><span>条</span></span></span></span><span><span><span><span>件</span></span></span></span><span><span><span><span>的</span></span></span></span><span><span><span><span>总</span></span></span></span><span><span><span><span>记</span></span></span></span><span><span><span><span>录</span></span></span></span><span><span><span><span>数</span></span></span></span><span>4.</span><em>m</em><em>y</em><span>.</span><em>d</em><em>a</em><em>t</em><em>a</em></span></span></span></span></span><em>$</em>java()这个方法变体，说明返回的是一个值,即方法中的m变量，而且这是一个异步方法，要用promise形式来调用：</p> 
<pre><span>      //异步方法要用.then来处理</span>
<span>      tableList(query).then((map) => &#123;</span>
<span>        if(map)&#123; </span>
<span>            const list = map.items;</span>
<span>            const total = map.total;</span>
<span>            if (this._isMounted) &#123;</span>
<span>                this.setState(&#123; list, total &#125;);</span>
<span>            &#125;</span>
<span>        &#125; </span></pre> 
<h3>配置</h3> 
<p>在类根目录(项目的resources目录)下，有一个名为myserverless.properties的配置文件，可以进行配置，例如配置deploy目录、设定开发/生产阶段、打包时是否生成API文档等，详见它的注释。</p> 
<h1>安全</h1> 
<p>安全是重头戏，放在最后讲：</p> 
<ol> 
 <li>开发期用具有developer权限的账户登录，可在前端任意写SQL和Java，并发送到后端动态编译执行。项目需要写一个实现了TokenSecurity接口的类，在这个类里针对token、方法ID、用户权限来判断是否可以执行，具体参见ProjectTokenSecurity示例。</li> 
 <li>开发期对于每一个方法，由前端赋一个方法ID，比如 my.$executeSql(<code>#ReadUser drop table tb_user if exists</code>); 这个ReadUser方法ID说明登录用户必须服务端配置有ReadUser权限才能运行，用这种方式可以精确控制每个方法的执行权限。无须登录的公开方法必须起名为public前缀。如方法ID省略，系统默认起名为default。</li> 
 <li>发布前进行命名检查，防止方法ID要求的权限与它的代码内容不符，比如上面这个ReadUser方法ID，它的代码是在删库，和命名不符，所以要修改代码或者修改方法ID名。</li> 
 <li>发布前，用MyServerless提供的打包工具将前端SQL和java代码抽取到后端，这样线上运行时前端是看不到SQL和Java源码的，而且线上运行配置成拒绝动态编译执行。</li> 
 <li>方法也可以采用传统前后分离模式直接写在后端，参见项目中PublicBackend$TokenLogin示例，签权依然是统一按方法ID来判断。</li> 
</ol> 
<p>关于MyServerless的安全设计，大家可以启动ReactMRP用developer和admin、guest账号登录体验一下就知道了，除了developer账号，其余账号都无权动态执行前端的SQL和Java。也就是说当你可以为所欲为的时候，你是开发者身份，当你想捣乱的时候，你却没有执行权限。 <br> 欢迎大家来找出MyServerless项目的安全漏洞，虽然理论上是不存在的。</p> 
<p>MyServerless该说的重点都说完了，所以这篇介绍本身就是它的全部用户手册了，如果还有不清楚的，可以把ReactMRP实际跑一下，把后端部分研究一下就可以了。</p> 
<h1>缘起</h1> 
<p>对了，最后上一张图来说一下我为什么开发这个项目，我承经有过2个预言，第一个是2017年人工智能将越过奇点，很遗憾这个预言没有实现。第二个预言就是下面这张图，虽然作为一个预言家，自己实现自己的预言脸皮太厚了，但好在看来这第二个预言不会再失败了，因为道理很简单，我没有给它加上时间限制，哈哈。。。。。。<br> <img alt="origin" src="https://gitee.com/drinkjava2/myserverless/raw/master/origin.png" referrerpolicy="no-referrer"></p> 
<h2>相关开源项目 | Related Projects</h2> 
<ul> 
 <li><a href="https://gitee.com/drinkjava2/jSqlBox">ORM数据库工具 jSqlBox</a></li> 
</ul> 
<h2>期望 | Futures</h2> 
<p>如对MyServerless感兴趣请点个赞</p> 
<h2>版权 | License</h2> 
<p><a href="https://gitee.com/link?target=http%3A%2F%2Fwww.apache.org%2Flicenses%2FLICENSE-2.0">Apache 2.0</a></p> 
<h2>关注我 | About Me</h2> 
<p><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdrinkjava2">Github</a> <a href="https://gitee.com/drinkjava2">码云</a> 微信:yong99819981(加群请留言"drinkjava2开源技术群")</p>
                                        </div>
                                      
</div>
            