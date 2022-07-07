
---
title: 'Redkale 2.7.0 发布，Java 分布式微服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-eaf9a7f1d464bb28812ff7d6d973f6ba02f.png'
author: 开源中国
comments: false
date: Thu, 07 Jul 2022 07:44:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-eaf9a7f1d464bb28812ff7d6d973f6ba02f.png'
---

<div>   
<div class="content">
                                                                                            <p>Redkale 2.7.0 发布。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Redkale， 一个Java分布式微服务框架，1.6M的jar可以代替传统几十M的第三方。包含TCP/UDP、HTTP、RPC、依赖注入、序列化与反序列化、数据库操作、WebSocket等功能。  一方面模块高度整合，极大的简化业务开发代码，一方面暴露大量底层，方便二次框架开发。  </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Java并不臃肿， 臃肿的是你自己的设计思维！</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>本次版本更新内容</strong>：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#24292f">  1、【新增】增加ConvertCoder功能，可以自定义字段的序列化</span><br> <span style="background-color:#ffffff; color:#24292f">  2、【新增】增加JsonMultiDecoder、JsonMultiObjectDecoder、OneOrList功能</span><br> <span style="background-color:#ffffff; color:#24292f">  3、【新增】JsonConvert全面兼容<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjson5.org" target="_blank">JSON5</a></span><br> <span style="background-color:#ffffff; color:#24292f">  4、【新增】增加redkale命令行</span><br> <span style="background-color:#ffffff; color:#24292f">  5、【新增】增加HttpRpcAuthenticator功能</span><br> <span style="background-color:#ffffff; color:#24292f">  6、【新增】MessageAgent增加配置MessageCoder功能</span><br> <span style="background-color:#ffffff; color:#24292f">  7、【新增】实现LoggingSearchHandler功能</span><br> <span style="background-color:#ffffff; color:#24292f">  8、【新增】ConvertFactory增加mapFieldFunc、ignoreMapColumns功能</span><br> <span style="background-color:#ffffff; color:#24292f">  9、【新增】增加PropertiesAgent功能</span><br> <span style="background-color:#ffffff; color:#24292f"> 10、【新增】增加链路ID Traces</span><br> <span style="background-color:#ffffff; color:#24292f"> 11、【新增】增加ResourceListener.different功能</span><br> <span style="background-color:#ffffff; color:#24292f"> 12、【新增】增加Environment类</span><br> <span style="background-color:#ffffff; color:#24292f"> 13、【新增】增加RestLocale功能</span><br> <span style="background-color:#ffffff; color:#24292f"> 14、【优化】优化PrepareServlet中HttpRender的初始化顺序</span><br> <span style="background-color:#ffffff; color:#24292f"> 15、【优化】日志支持java.util.logging.ConsoleHandler.denyreg配置</span><br> <span style="background-color:#ffffff; color:#24292f"> 16、【优化】FilterColumn支持least=0时空字符串也参与过滤</span><br> <span style="background-color:#ffffff; color:#24292f"> 17、【优化】HttpRequest兼容参数名为空字符串</span><br> <span style="background-color:#ffffff; color:#24292f"> 18、【优化】移除CryptColumn、CryptHandler功能</span><br> <span style="background-color:#ffffff; color:#24292f"> 19、【优化】PrepareServlet 更名为 DispatcherServlet</span><br> <span style="background-color:#ffffff; color:#24292f"> 20、【优化】@WebServlet合并url</span><br> <span style="background-color:#ffffff; color:#24292f"> 21、【修复】</span><span style="background-color:#ffffff; color:#202124">修复HttpResponse.finish结果status=404时按200输出的bug</span><br> <span style="background-color:#ffffff; color:#24292f"> 22、【修复】修复HttpMessageLocalClient创建request时没有赋值给currentUserid值</span><br> <span style="background-color:#ffffff; color:#24292f"> 23、【修复】修复Rest.createRestServlet带特定泛型问题</span><br> <span style="background-color:#ffffff; color:#24292f"> 24、【修复】修复Convert模块中父类含public field，subclass不传父类会导致NoSuchFieldError的bug</span><br> <span style="background-color:#ffffff; color:#24292f"> 25、【修复】修复ApiDocCommand在没有运行时不能生成doc的bug</span><br> <span style="background-color:#ffffff; color:#24292f"> 26、【修复】修复JsonWriter.writeWrapper按latin1编码写的bug</span><br> <span style="background-color:#ffffff; color:#24292f"> 27、【修复】修复JsonDynEncoder在定制字段情况下会被全量字段的动态类覆盖的bug</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>更新详情介绍</strong>：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Json 序列化功能增强:</strong></p> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><span style="color:#333333">   1、</span><span style="color:#24292f">支持</span><span style="background-color:#ffffff; color:#24292f"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjson5.org" target="_blank">JSON5</a></span></p> 
<pre><code class="language-json">&#123;
   intval1: 0xa,         //支持十六进制， 值转成10
   intval2: +100,        //支持+开头， 值转成100
   longval1: NaN,        //支持NaN， 值转成0
   longval2: Infinity,   //值转成Long.MAX_VALUE
   floatval1: NaN,       //支持NaN， 值转成Float.NaN
   doubleval: -Infinity, //值转成Double.NEGATIVE_INFINITY
   //这是一个单行注释
   name : "haha",
   /* 这是一个多行注释
      这是一个多行注释 */
   desc : "哈哈",
   ints: [1,2,3,4,]      //兼容对象尾部多一个','
&#125;</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">   以上json字符串能正确反解析成Java对象。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">   2、<span style="background-color:#ffffff; color:#24292f">OneOrList </span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#24292f">     </span>当一个对象字段可能是单个对象，也可能是对象集合时，可以设定字段类型为 <span style="background-color:#ffffff; color:#24292f">OneOrList<T></span></p> 
<pre><code class="language-java">    public class JavaBean &#123;
        
        public String name;
        
        public OneOrList<String> address;        
    &#125;</code></pre> 
<pre><code class="language-json">    &#123;"name":"redkale", "address": "wuhan"&#125;

    &#123;"name":"redkale", "address": ["wuhan","hubei","china"]&#125;</code></pre> 
<p>    上面两个json字符串都可以正确解析成JavaBean对象,  也可以 直接用OneOrList的泛型来反序列化对象:</p> 
<pre><code class="language-java">    JsonConvert convert = JsonConvert.root();
    Type type = new TypeToken<OneOrList<String>>() &#123;&#125;.getType();
    OneOrList<String> one = convert.convertFrom(type, "haha");
    OneOrList<String> list = convert.convertFrom(type, "['haha','hehe']");
    System.out.println(convert.convertTo(type, one));   //输出: "haha"
    System.out.println(convert.convertTo(type, list));  //输出: ["haha","hehe"]</code></pre> 
<p>    <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fplayground.open-rpc.org%2F%3FschemaUrl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fethereum%2Feth1.0-apis%2Fassembled-spec%2Fopenrpc.json%26uiSchema%255BappBar%255D%255Bui%3AsplitView%255D%3Dfalse%26uiSchema%255BappBar%255D%255Bui%3Ainput%255D%3Dfalse%26uiSchema%255BappBar%255D%255Bui%3AexamplesDropdown%255D%3Dfalse" target="_blank">以太坊JSON-RPC规范接口</a> 某些接口中的字段存在这种需求:</p> 
<p><img height="1198" src="https://oscimg.oschina.net/oscnet/up-eaf9a7f1d464bb28812ff7d6d973f6ba02f.png" width="1273" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">   3、<span style="background-color:#ffffff; color:#24292f">ConvertImpl</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#24292f">     </span>当一个对象字段类型是抽象类，反序列化时根据识别子类独有的字段转换成对应的子类， 需要使用<span style="background-color:#ffffff; color:#24292f">ConvertImpl</span></p> 
<pre><code class="language-java">    @ConvertImpl(types = &#123;Bean123.class, Bean23.class, Bean234.class&#125;)
    publicabstract class AbstractBean &#123;

    &#125;

    public class Bean123 extends AbstractBean &#123;

        public String a1;

        public String a2;

        public String a3;
    &#125;

    public class Bean23 extends AbstractBean &#123;

        public String a2;

        public String a3;
    &#125;

    public class Bean234 extends AbstractBean &#123;

        public String a2;

        public String a3;

        public String a4;
    &#125;



    JsonConvert convert = JsonConvert.root();
    String json1 = "&#123;'a1':'111', 'a2':'222', 'a3':'333'&#125;";
    AbstractBean bean1 = convert.convertFrom(AbstractBean.class, json1); 
    System.out.println(bean1);  //Bean123对象
        
    String json2 = "&#123;'a2':'222', 'a4':'444', 'a3':'333'&#125;";
    AbstractBean bean2 = convert.convertFrom(AbstractBean.class, json2); 
    System.out.println(bean2);  //Bean234对象
        
    String json3 = "&#123;'a3':'333'&#125;";
    AbstractBean bean3 = convert.convertFrom(AbstractBean.class, json3); 
    System.out.println(bean3);  //Bean23对象， 无子类独有的字段，优先匹配特定字段数最少的子类
        
    String json4 = "&#123;'a1':'111', 'a2':'222', 'a3':'333', 'a4':'444'&#125;";
    AbstractBean bean4 = convert.convertFrom(AbstractBean.class, json4); 
    System.out.println(bean4);  //Bean123对象, a1字段在前面，优先匹配Bean123类</code></pre> 
<p>   <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fplayground.open-rpc.org%2F%3FschemaUrl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fethereum%2Feth1.0-apis%2Fassembled-spec%2Fopenrpc.json%26uiSchema%255BappBar%255D%255Bui%3AsplitView%255D%3Dfalse%26uiSchema%255BappBar%255D%255Bui%3Ainput%255D%3Dfalse%26uiSchema%255BappBar%255D%255Bui%3AexamplesDropdown%255D%3Dfalse" target="_blank">以太坊JSON-RPC规范接口</a> 某些接口同样存在这种需求。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">   4、<span style="background-color:#ffffff; color:#24292f">JsonMultiDecoder</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#24292f">     </span>当一个数组的元素是不同的数据类型时，反序列化时需要使用<span style="background-color:#ffffff; color:#24292f">JsonMultiDecoder(通过JsonConvert调用)</span></p> 
<pre><code>        JsonConvert convert = JsonConvert.root();
        String json = "['aaaa', ['hehe','haha']]";
        Type[] types = new Type[]&#123;String.class, String[].class&#125;;
        Object[] objs = convert.convertFrom(types, json);
        System.out.println(objs[0]); //String对象  "aaaa"
        System.out.println(objs[1]); //String数组  ["hehe","haha"]</code></pre> 
<p>         注意:  json数组元素的个数必须与Type数组的长度一致。  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jsonrpc.org%2Fspecification" target="_blank">JSON-RPC</a> 的批量操作接口存在这种需求。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>redkale命令行:</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">    bin下新增了redkale脚本， 通过脚本命令行可以更方便的操作: </p> 
<pre><code class="language-bash">
# 启动redkale进程，无参数
./bin/redkale

# 启动redkale进程
./bin/redkale  start  

# 关闭redkale进程
./bin/redkale  shutdown

# 重启redkale进程
./bin/redkale  restart

# 生成openapi文档
./bin/redkale  apidoc</code></pre> 
<p>    以上是redkale内置的命令，开发者可以通过@Command 自定义命令： </p> 
<pre><code class="language-java">    public class CommandTestService implements Service &#123;

        @Command("say") //只接收say命令
        public String say(String cmd, String[] params) &#123;
            System.out.println("say接收命令: " + cmd + ", 参数: " + Arrays.toString(params));
            return "say done";
        &#125;

        @Command("hi") //只接收hi命令
        public String hi(String cmd, String[] params) &#123;
            System.out.println("hi接收命令: " + cmd + ", 参数: " + Arrays.toString(params));
            return "hi done";
        &#125;

        @Command  //会接收到所有命令
        public String all(String cmd, String[] params) &#123;
            System.out.println("all接收命令: " + cmd + ", 参数: " + Arrays.toString(params));
            return "all done";
        &#125;
    &#125;
</code></pre> 
<p><img height="1064" src="https://oscimg.oschina.net/oscnet/up-948e52a1f5ebe03826b11887081fe638743.png" width="1423" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            