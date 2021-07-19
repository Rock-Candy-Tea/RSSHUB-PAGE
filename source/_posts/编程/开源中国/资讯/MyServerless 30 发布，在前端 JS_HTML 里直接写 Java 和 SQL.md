
---
title: 'MyServerless 3.0 发布，在前端 JS_HTML 里直接写 Java 和 SQL'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6231'
author: 开源中国
comments: false
date: Mon, 19 Jul 2021 10:33:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6231'
---

<div>   
<div class="content">
                                                                    
                                                        <h3>MyServerless(原GoSqlGo)简介 | Description</h3> 
<p>天下武功，唯快不破，MyServerless能让前端直接在HTML或Javascript里写业务代码和SQL，不需要后端程序员参与，从而实现快速开发。<br> MyServerless主页：<a href="https://gitee.com/drinkjava2/myserverless">https://gitee.com/drinkjava2/myserverless</a><br> <br> <strong>本次更新内容:</strong></p> 
<p>1.项目原名为GoSqlGo，现从3.0即本版起更名为MyServerless。<br> 2.myserverless.properties文件中新增web_files选项，可以指定在哪些前端文件中允许直接书写远程Java脚本和SQL，默认是html,htm,js,jsp,php这几种。<br> 3.myserverless.properties文件中新增api_export_file选项，可以指定一个输出文件名，当运行go-server.bat进行打包布署时，可以按指定的文件名自动将页面所有Java和SQL生成一个API汇总文档。<br> 4.原项目中出现.gsg调用的地方统一更改为myserverless.do调用。<br> 5.升级它的DAO工具jSqlBox到5.0.6.jre8版，这个版本添加了一个camelHandler,用于将JDBC查询结果Map/Array/List对象中的下划线格式的键值名称转为驼峰式，如下面这行SQL调用：<br>   List<Map<String, Object>> result = DB.qryMapList("select user_name from users where age>", que(10), " order by id ", pagin(1, 10), new CamelHander());<br>  在添加了CamelHander之后返回结果中的键名user_name将转换为userName。<br> 6.修正了jSqlBox中jDialects子项目达梦数据库支持以及从数据库生成Java源码的bug。<br> <br> MyServerless项目原名为GoSqlGo，但这个命名不太贴切，因为它不光是可以直接在前端写SQL，还可以直接写Java源码，考虑到它的这个开发模式有点类似于serverless，后端不参与具体业务开发，只提供硬件平台和基础的API供调用，开发都可以远程进行，而且都是以方法作为最小且唯一的功能单元，所以从3.0版起项目更名为MyServerless，原项目GoSqlGo不再维护。</p> 
<p>MyServerless与通常大厂的Serverless服务相比，主要区别是：<br> 1.使用免费。通常大厂的Serverless服务是按调用来按需收费，而MyServerless是用户自己布署的，调用不收费，还是按传统租用空间方式收费。<br> 2.可定制，无依赖。开发者拥有全部的MyServerless服务端源码，可以自行定制后端服务，如选择不同的签权方式、DAO工具等，不与具体的云服务商绑定。<br> 3.技术极简。大厂的Serverless服务通常较复杂，很难上手。而MyServerless核心源码只有几千行，采用标准Java脚本语言和SQL，极易上手，通常前端只需要了学会SQL即尝试进行开发。<br> 4.功能极度简化。MyServerless的定位是用最少的代价开通前端访问数据库能力。相比与大厂的Serverless服务，它在功能上有缺失：<br> 1)目前不提供源码管理和IDE插件，后端源码就直接保存在前端。<br> 2)目前不提供高可用性、后端自动缩扩容这些功能。<br> 3)目前只整合了一个DAO工具，专注于数据库访问，不支持一些特殊功能如文件上传等。<br> 4)大厂Serverless服务通常不区分开发期和布署期，而MyServerless因为安全原因，分为开发和布署两个阶段，开发期源码写在前端，源码远程发送到服务器执行，布署期必须利用打包工具将前端的源码和SQL抽取到后端。</p> 
<h3>适用场合 | Applications</h3> 
<p>MyServerless适用于原型、快速、简单业务开发，以及前后端都是同一个人开发的场合，因为MyServerless是没有API的，也就不存在前后端沟通问题，所以开发效率高。</p> 
<h3>不适用场合 | Not Applicable</h3> 
<p>MyServerless不适用于复杂业务开发(比如脚本源码超过50行)，原因是因为目前不具备IDE插件可以调试存放在前端的Java脚本，调试效率低，如果业务复杂时，在调试上花的时间还不如直接让传统后端程序员提供API和文档。</p> 
<p>通常网站的API是由绝大多数的简单CRUD和少部分的复杂业务API组成，大项目可以考虑用MyServerless结合传统API方式来开发，开启一个MyServerless服务支撑简单的CRUD功能，剩下的复杂业务依然由传统后端程序员提供API和文档，这样可以节省后端程序员大部分的开发工作量。</p> 
<h3>使用 | Usage</h3> 
<p>用实例来说明MyServerless的使用，以下示例直接在前端写SQL和Java脚本，实测通过，文件位于<a href="https://gitee.com/drinkjava2/myserverless/blob/master/server/src/main/webapp/page/demo1.html">这里</a>。</p> 
<div> 
 <div> 
  <pre><html>
<head>
<meta charset="utf-8">
<script src="/js/jquery-1.11.3.min.js"></script>
<script src="/js/jquery-ajax-ext.js"></script>
<script src="/js/myserverless-3.0.js"></script>
</head>
<body>
      
    <script>document.write($java(`return new WebBox("/WEB-INF/menu.html");`)); </script>
    <h2>Transaction demo, use jQuery</h2>
    
    <script> 
  function getUserListHtml()&#123;
  var users=$qryMapList(`select * from account where amount>=? order by id`,0);
  var html="User List:<br/>";
  for(var i=0;i<users.length;i++) 
  html+="User ID:" +  users[i].ID+", AMOUNT:"+ users[i].AMOUNT+"<br/>"; 
      return html;   
  &#125;
</script>
   
<div id="msgid" class="msg"></div> 
<p id="Users">
    <script>document.write(getUserListHtml());</script>   
</p>

<section>
<header>Account A</header>
<div id="A" class="amount">
<script>
document.write($qryObject(`select amount from account where id=? and amount>=?`, 'A',0));
</script>
</div>
</section>
<section>
<header>Account B</header>
<div id="B" class="amount">
<script>
    account=$qryEntity(`com.demo.entity.Account, select * from account where id=?`, 'B');
document.write(account.amount);
</script>
</div>
</section>
<script>
  function transfer(from, to, money)&#123; 
var rst = $$javaTx(`#AccountTransfer         
//参数说明   $1:账号A的id  $2:账号B的id $3:要转账的金额
int money = Integer.parseInt($3);
if (money <= 0)
     return new JsonResult(0, "Error: Illegal input.");
Account a = DB.entityLoadById(Account.class, $1);
if (a.getAmount() < money)
     return new JsonResult(0, "Error:No enough balance!");
a.setAmount(a.getAmount()-money).update();
DB.exe("update account set amount=amount+?",par(money)," where id=?",par($2));
    return new JsonResult(200, "Transfer success!");
        `, from,to,money); 
  $("#msgid").text(rst.msg);
  if(rst.code==200) 
       $("#msgid").css("background", "#dfb");
  else 
                     $("#msgid").css("background", "#ffbeb8");
      $("#"+from).text($qryObject(`select amount from account where id=?`,'A'));
       $("#"+to).text($qryObject(`select amount from account where id=?`,'B'));
       $("#Users").html(getUserListHtml());
&#125;
</script>
<section>
<header>Transfer</header>
<form onsubmit="return false" action="##" method="post">
<input id="amount" name="amount" value="100" class="amount">
<button name="btnA2B" value="true" onclick="transfer('A','B', $('#amount').val())">From account A to account B</button>
<button name="btnB2A" value="true" onclick="transfer('B','A',$('#amount').val())">From account B to account A</button>
</form>
</section>
</body>
</html></pre> 
 </div> 
</div> 
<p>另外还有两个演示:<br> <a href="https://gitee.com/drinkjava2/myserverless/blob/master/server/src/main/webapp/page/demo2.html">演示2</a>：MyServerless结合Vue的使用。<br> <a href="https://gitee.com/drinkjava2/myserverless/blob/master/server/src/main/webapp/page/demo3.html">演示3</a>: 演示直接在前端进行表单的输入检查并保存到数据库</p> 
<h3>运行 | Dependency and Run</h3> 
<p>MyServerless分为server和core两个目录，server目录是一个示范项目，使用时只需要将server项目作一些修改，如更改数据库连接和重写签权逻辑，即可以用于实际开发 。core目录是内核源码，除非要定制后端，用户一般不需要关心。<br> 在windows下点击server目录下的run_server.bat批处理，即可进入上例的演示界面，使用用户名demo、密码123登录。<br> 演示项目是把Web和后端做在一起，实际开发时前端可以在单独的项目里远程开发，所有改动即时生效，不需重启后端。</p> 
<h3>方法说明 | Methods</h3> 
<p>在前端引入myserverless-3.0.js这个javascript库后，就可以直接在前端调用以下远程函数执行后端业务：</p> 
<div> 
 <div> 
  <pre>$java(String, Object...) 在后端执行Java脚本，第一个参数是Java脚本源码，后续参数是业务参数，在Java脚本源码里可以用$1,$2...来代表。  
$javaTx(String, Object...) 在后端执行Java脚本并开启事务，如果有异常发生，事务回滚。  
$qryObject(String, Object...) 将SQL查询结果的第一行第一列值返回，第一个参数是SQL，后面是SQL参数，下同  
$qryArray(String, Object...)  返回SQL查询的第一行数据，以Javascript数组对象格式返回  
$qryArrayList(String, Object...)  返回多行查询结果，以数组列表格式返回    
$qryTitleArrayList(String, Object...)  返回多行查询结果，以数组列表格式返回,第一行内容是各个列的标题  
$qryMap(String, Object...) 返回SQL查询的第一行数据，为Map 格式  
$qryMapList(String, Object...)  返回SQL查询的多行数据，为List<Map>格式  
$qryEntity(String, Object...)  返回第一行数据为实体对象，SQL写法是实体类名+逗号+SQL, 示例:$qryEntity(`a.b.Demo, select * from demo`); 
$qryEntityList(String, Object...)  返回多行数据为List<实体>对象，SQL写法是实体类名+逗号+SQL, 示例:$qryEntityList(`a.b.Demo, select * from demo`);   </pre> 
 </div> 
</div> 
<p>注意以上远程函数调用的第一个参数是Java源码或SQL文本，要用键盘ESC下方的单引号括起来，这是Javascript的特殊单引号，支持多行文本。<br> 以上方法都是自定义的，用户也可以自定义自己的方法。以上方法还可以用$$开头返回JSON对象。JSON对象有&#123;code, msg, data, debugInfo&#125; 4个字段，但debugInfo字段仅当服务端配置为debug_info=true时才有值。<br> MyServerless方法可以添加以下两类特殊语句：</p> 
<ol> 
 <li>#xxxxx 形式的ID，用来自定义方法ID，如没有这个ID，方法缺省ID为"Default"。这个方法ID的命名很重要，在用户的签权类里，要根据这个ID来判断用户是否有权限执行这个方法</li> 
 <li>import开头的语句，这个等同于标准的Java包引入语法<br> 例如下面这个方法调用定义了一个名为ReadUserAmount的方法ID，并引入了一个名为abc.DemoUser的Java包:</li> 
</ol> 
<div> 
 <div> 
  <pre>$java('#ReadUserAmount import abc.DemoUser; return new DemoUser().loadById($1).getAmount();', 'u1');   </pre> 
 </div> 
</div> 
<h3>开发和布署 | Develop & Deploy</h3> 
<p>在类根目录(项目的resources目录)下，有一个名为myserverless.properties的配置文件，可以进行配置，例如配置deploy目录、设定开发/生产阶段、设定develop_token和debug_inifo、打包时是否生成API等，详见它的注释。</p> 
<p>开发阶段：MyServerless示范项目在服务端运行，它自带一个动态Java脚本编译功能，前端发来的SQL和Java脚本，被动态编译为实际的Java类，并执行这个Java类，最后返回JSON对象。</p> 
<div> 
 <div> 
  <pre>如果javascript方法前是两个$符号，如$$java，则返回一个JSON对象，它的data字段保存了返回结果。如果javascript方法前只有一个$符号，如$java，则返回的值直接就是Json的data字段。  </pre> 
 </div> 
</div> 
<p>布署阶段：双击server目录下的批处理文件go-server.bat，即可将前端所有的SQL和原生Java片段抽取到服务端去，转变为Java源文件，原有前端的SQl和JAVA代码在转换后将成为类似于$callDeployed('Xxxx_C9GK90J27','A');之类的通过ID进行的调用，以防止非法访问， 实现安全性。<br> server目录下还有一个文件名为go-front.bat，这个是逆操作，可以将后端的Java代码移回到前端。</p> 
<h3>安全 | Security</h3> 
<p>在项目的myserverless.properties文件里，有以下关于安全的设计：<br> 1.当stage设定为product阶段时，不再动态编译前端传来的SQL和Java片段，以实现运行期的安全。<br> 2.当stage设定为develop时，deveop_token必须设定一个密码，在开发阶段会 执行前端传来的任意SQL和Java代码，后端会检查前端传来的develop_token密码与服务器的设定是否一致，否则拒绝访问，这样可以排除开发期的非法访问。<br> 3.token_security设定，这是用来登记用户自定义的登录检查类，使用详见示范项目，MyServerless并没有集成第三方权限框架，所以需要用户根据自已的项目实现自定义的登录和token验证类。通常是根据token和方法ID来判定是否允许执行MyServerless远程方法。</p> 
<h3>常见问题 | FAQ</h3> 
<ul> 
 <li> <p>安全上有没有问题?<br> 架构上没有安全问题，MyServerless通过token和方法ID，结合自定义签权方法来检查每一个方法ID的执行权限。当然用户写的签权方法或Java脚本中有可能出现安全漏洞，但这与本项目的架构无关。</p> </li> 
 <li> <p>为什么采用Java作为业务脚本语言而不是Javascript/C#/Go等语言? 因为作者只对Java熟悉，没有精力象大厂的Serverless服务一样提供多种语言实现，以前做过Node.js的尝试，但最终还是决定放弃。用户如果对其它语言熟悉，也可以仿照MyServerless的思路编写自己的serverless服务，原理不复杂，无非就是源码保存在远程动态编译执行，布署时再抽取出来以保证安全。</p> </li> 
 <li> <p>为什么默认server项目采用jSqlBox这么小众的DAO工具?<br> 因为jSqlBox是本人写的DAO工具，打广告用的，它的SQL写法很多。如果前端对jSqlBox不感冒，可以仿照示例改造成使用不同的DAO工具如MyBatis等。MyServerless重点在于提供了一个动态编译执行远程Java源码的框架和打包工具，并不拘泥于具体的某个Java或SQL技术。</p> </li> 
 <li> <p>(小鹏提出)Java写在HTML/Javascript里没有错误检查、语法提示，及重构功能，不利于复杂业务开发。<br> 这个将来可以通过开发IDE插件解决。但目前的解决办法是只能运行go-server.bat批处理将Sql/Java抽取成Java源码类，在Eclipse/Idea等IDE里找错、更正后再用go-front.bat批处理塞回到HTML里去，也可以干脆就不塞回去了，后者就对应传统的前后端分离API开发了。</p> </li> 
 <li> <p>业务有变动，前端代码或SQL需要修改怎么办?<br> 开发期直接在前端修改Java代码或SQL即可，即改即生效，不需要重启后端服务器。布署时由运维布署并重启后端服务器。</p> </li> 
 <li> <p>前端业务代码需要复用(如多处调用或测试)怎么办?<br> 需要复用的业务代码和SQL写在公共JavaScript库里，前端其它地方调用这些公共库里的方法。</p> </li> 
 <li> <p>与GraphQL或XXX-API等项目的区别？<br> GraphQL等项目着重于API及文档的创建。而MyServerless是直接在前端写Java脚本和SQL，参数和业务注释直接写在源码即可，根本就不创建API, 也不需要写文档。个人认为文档的作用应该是用来学习而不是沟通。<br> 如果一定要MyServerless生成API文档，可以在配置里加入api_export_file=xxx.html即可汇总所有前端源码和SQL成一个API文档，但这个文档仅用于复核，并不是开发必不可缺的文档。</p> </li> 
</ul> 
<h2>相关开源项目 | Related Projects</h2> 
<ul> 
 <li><a href="https://gitee.com/drinkjava2/jSqlBox">ORM数据库工具 jSqlBox</a></li> 
</ul> 
<h2>期望 | Futures</h2> 
<p>如对MyServerless感兴趣请点个赞，或发issue提出完善意见</p> 
<h2>版权 | License</h2> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.apache.org%2Flicenses%2FLICENSE-2.0" target="_blank">Apache 2.0</a></p> 
<h2>关注我 | About Me</h2> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdrinkjava2" target="_blank">Github</a><br> <a href="https://gitee.com/drinkjava2">码云</a></p>
                                        </div>
                                      
</div>
            