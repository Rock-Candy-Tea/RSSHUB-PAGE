
---
title: 'SpringMVC_boot-CSRF安全方案 ｜ 八月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1421'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 01:18:19 GMT
thumbnail: 'https://picsum.photos/400/300?random=1421'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1. CSRF原理与防御方案概述</h1>
<h2 data-id="heading-1">一. 原理</h2>
<ol>
<li>
<p>增删改的接口参数值都有规律可循，可以被人恶意构造增删改接口</p>
</li>
<li>
<p>将恶意构造的增删改接口发给对应特定用户，让特定用户点击</p>
</li>
<li>
<p>特定用户使用自己的认证信息对该接口发起了请求，可能被新增危险信息(比如管理员账号)，修改敏感信息(比如退款金额)，删除关键信息(比如删除差评)</p>
</li>
</ol>
<h2 data-id="heading-2">二. 防御方案概述</h2>
<ol>
<li>
<p>参数不可猜解，发起请求时在参数中增加随机token参数</p>
</li>
<li>
<p>token参数在后台与保存在cookie,session,tair中的token参数进行比对，若不匹配或者没有该参数，则校验不通过</p>
</li>
<li>
<p>黑客无法获取到特定用户的随机token值，所以杜绝CSRF的危害</p>
</li>
</ol>
<h1 data-id="heading-3">2 ali修复方案</h1>
<h2 data-id="heading-4">一 <strong>.</strong> 确认应用类型</h2>
<p>若为正常业务，提供数据/文件等增删改服务，则需要配置CSRF，请继续看下去</p>
<p>若应用不是Web应用，或者只是HSF服务或者给其他应用服务器调用的API接口服务(纯内网的纯Server to Server，不是通过Login获取登陆态的接口，而是通过AKSK加签名验证签名) ，则不需要配置CSRF，请提供相应加签验签代码给对应答疑或者安全工程师进行确认并关闭漏洞。</p>
<h2 data-id="heading-5">二 <strong>.</strong> 安全包引入</h2>
<h3 data-id="heading-6"><strong>Step1.</strong> 配置扩展包<strong>POM</strong>依赖</h3>
<p>注意:SpringMVC扩展安全包引入后会默认开启一系列开关，包括XSS开关，CSRF开关等，从而导致业务短暂出现异常(前端页面乱码，接口访问返回403状态码等)，只需要继续按照文档操作下去，业务最终会恢复正常。</p>
<p><strong>1. SpringMVC</strong>扩展包</p>
<p>请参考网上SpringMVC安全扩展引入文档</p>
<p><strong>2 SpringBoot</strong>扩展包 <strong>(starter)</strong></p>
<p>请参考网上SpringBoot安全扩展引入文档</p>
<p><strong>Step2.</strong> 查看是否依赖成功</p>
<p>POM配置完成后，在IDEA的External Libraries中查找是否以下包存在</p>
<pre><code class="copyable">//SpringMVC仅检查这个包
com.alibaba.security:security-spring-webmvc

//SpringBoot仅检查这个包
com.alibaba.security:security-spring-boot-starter
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">三 <strong>. CSRF</strong>开关配置</h2>
<h3 data-id="heading-8"><strong>Step1.</strong> 显式配置<strong>CSRF</strong>开关</h3>
<p>虽然CSRF在安全包引入之后，会自动开启CSRF拦截，但是为了确保配置可读性以及后续问题排查方便，请在resources下的"application.properties" (若没有，请创建)文件中协商如下配置：</p>
<pre><code class="copyable">spring.security.csrf.enabled = true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注：开启了该开关之后，所有访问请求都会因为没有token带入被拦截导致访问不成功，需要继续配置下去，让业务恢复正常</p>
<h3 data-id="heading-9"><strong>Step2.</strong> 将<strong>token</strong>带给前端</h3>
<p>配置好开关之后，安全包会生成一个随机字符串，我们称为CSRF_Token，该token会被默认存入cookie中。若使用VM，则可以通过VM调用相关接口获得。</p>
<p>这个Token需要在前端的每个增删改接口请求中作为参数带入给服务器用于校验安全性</p>
<p>不同前端技术方案有不同带入方式:</p>
<h4 data-id="heading-10"><strong>1 VM</strong>后端模板</h4>
<p>a.  VM后端模板有三种token带入请求的配置方式:</p>
<ul>
<li>在application.properties中统一配置</li>
<li>CSRF Token 自动生成的URL映射列表，多值使用逗号分隔（默认值为空）</li>
<li>当前URL风格为ant风格，风格值由配置项 spring.security.csrf.url.style 决定</li>
</ul>
<pre><code class="copyable"> spring.security.csrf.token.urls = /csrf_token/**
<span class="copy-code-btn">复制代码</span></code></pre>
<p>b. 在Controller类级别使用注解@CsrfTokenModel配置</p>
<pre><code class="copyable">    @Controller
    @RequestMapping("/csrf")
    @CsrfTokenModel
    public class CsrfController &#123;
        @RequestMapping("/form") 
       public String form() &#123;
            return "csrf_form";
         &#125;
     &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>c.在Controller类级别使用注解配置</p>
<p>此种情况可以使得该controller下所有模板渲染。都可以通过宏获取token的参数名称和值</p>
<p>在方法级别使用注解@CsrfTokenModel配置</p>
<pre><code class="copyable">@Controller
@RequestMapping("/csrf")
public class CsrfController &#123;
    @RequestMapping("/form")
    @CsrfTokenModel
    public String form() &#123;
        return "csrf_form";
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果需要CSRF Token校验的Controller或者方法过多时，当前框架还提供一种便利的方式， 即URL映射级别的自动生成方式，只需在application.properties文件中增加如下配置：</p>
<ul>
<li>
<p>CSRF Token 自动生成的URL映射列表，多值使用逗号分隔（默认值为空）</p>
</li>
<li>
<p>当前URL风格为正则表达式，风格值由配置项 spring.security.csrf.url.style 决定</p>
</li>
</ul>
<pre><code class="copyable"> spring.security.csrf.token.urls = /csrf_token/**
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>CSRF Token 模型属性名称</li>
</ul>
<pre><code class="copyable">spring.security.csrf.token.model.attribute = csrfToken
<span class="copy-code-btn">复制代码</span></code></pre>
<p>后端配置好之后，在VM模板中，针对所有请求form表单，增加对应字段，确保每次请求都能带上</p>
<ul>
<li>Velocity Template Code</li>
</ul>
<pre><code class="copyable">     <form method="post" action="/form/submit">
         <input type="hidden" name="$&#123;csrfToken.parameterName&#125;"      value="$&#123;csrfToken.token&#125;">
         <input type="text" name="name"/>
         <br>
         <input type="submit" value="Submit"/>
     </form>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>渲染后的HTML</li>
</ul>
<pre><code class="copyable"><form method="post" action="/form/submit">
    <input type="hidden" name="_csrf" value="bfe23341-b28c-41a3-bed8-dfbd65385fc8">
    <input type="text" name="name"/>
    <br>
    <input type="submit" value="Submit"/>
</form>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>正常情况下如上图所示，渲染后，字段name为p_csrf, value为随机生成的值，同时会在cookie中放入对应字段。请注意，token的字段名一定是要从csrftoken这个obj中取出来的，不能在前端自定义，若要在后端更换字段名，请参考下面的『CSRF定制化功能』</p>
<h4 data-id="heading-11"><strong>2. ajax</strong>前后端分离</h4>
<p>ajax发起请求的情况下，token无法直接渲染到页面上，通过下方途径解决该问题。</p>
<ul>
<li>在cookie中读取token，将其带入到ajax请求的参数中。然后传到后端(Cookie中token的key默认为XSRF-TOKEN)</li>
<li>若cookie中的XSRF-TOKEN值无法被js读取，请检查该值httponly属性未true，若为true，请在"application.properties"中新增一个配置项，如下:</li>
<li>如果是在参数中携带，默认Token名称是_csrf，如果是在header中携带，默认Token名称是<strong>X-XSRF-TOKEN</strong></li>
</ul>
<pre><code class="copyable">spring.security.csrf.cookieHttpOnly = false
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>设置完成之后，请清除浏览器缓存之后重新尝试获取XSRF-TOKEN值</li>
</ul>
<h4 data-id="heading-12"><strong>3.</strong> 跨域下的<strong>token</strong>传输</h4>
<p>在一般业务场景下，安全包会将token种到服务端对应的域名cookie下，可以被前端js调用和植入到header或者参数中。但是在跨域场景下，前端页面与后端服务端不是同一个域名，导致无法取到服务端域名下的cookie。</p>
<p>假设aaaa.com要跨域访问bbbb.com的接口，bbbb.com的接口做了csrf校验。此时按照如下步骤进行token交互:</p>
<p>开启<strong>CORS</strong>跨域头的业务解决方案如下：</p>
<h5 data-id="heading-13">1.  <strong>bbbb.com</strong>新增一个接口，返回自身的<strong>csrf token</strong></h5>
<p>该接口实现示例如下:</p>
<pre><code class="copyable">    @RequestMapping(value = "/ajax", produces = MediaType.APPLICATION_JSON_VALUE)
    @CrossOrigin(origins = "http://aaaaaa.com:7001", maxAge = 3600)
    @ResponseBody
    public CsrfToken getCsrfToken(HttpServletRequest request, HttpServletResponse response) &#123;
        CsrfToken csrfToken = csrfTokenRepository.loadToken(request);
        if (csrfToken == null) &#123;
            csrfToken = csrfTokenRepository.generateToken(request);
            csrfTokenRepository.saveToken(csrfToken, request, response);
        &#125;
        return csrfToken;

    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-14">2.  <strong>aaaa.com</strong>携带<strong>with-credentials</strong>的头部来获取该<strong>token</strong></h5>
<pre><code class="copyable">function callOtherDomain()&#123;
       var xhr = new XMLHttpRequest();
        if(xhr) &#123;
            xhr.open('GET', 'http://bbbbbb.com:7001/csrf/ajax', true);
            xhr.withCredentials = true;
            xhr.onload = function () &#123;
                result.innerHTML = xhr.responseText;
                var json = JSON.parse(xhr.responseText);
                token_key = json.paramterName;
                token = json.token;
            &#125;;
            xhr.send(null);
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-15">3.  将获取到的token存放在客户端上(比如localstorage，或者页面隐藏字段中)</h5>
<h5 data-id="heading-16">4.  aaaa.com 访问bbbb.com其他接口的时候，获取token作为接口参数/头部参数传递给bbbb.com，同时访问该接口时应该设置withcredentials = true:</h5>
<pre><code class="copyable">function buttonClick(token_key, token)&#123;
        var xhr = new XMLHttpRequest();
        xhr.open('GET', 'http://bbbbbb.com:7001/csrf/cors/check');
        xhr.withCredentials = true;
        xhr.onload = function () &#123;
            result.innerHTML = xhr.responseText;
        &#125;;
        xhr.onerror = function () &#123;
            result.innerHTML = "Error!";
        &#125;
        xhr.send(token_key + '=' + token + '&' + otherparams)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Step3.</strong> 后端进行<strong>Token</strong>校验</p>
<p>后端进行token校验，目前只提供全局url检查方式，在没有显式配置情况下默认对所有POST请求进行token检查，为了更好的对业务进行支持，建议在classpath下的application.properties进行显式配置，如下:</p>
<pre><code class="copyable">//根据业务需求进行配置是否拦截GET请求,安全要求POST请求必须拦截

spring.security.csrf.supportedMethods = POST,GET

//使用ant风格配置需要进行token检查的url(安全要求对所有增删改进行token校验)

spring.security.csrf.url.included = /** 

//使用ant风格配置无需需要进行token检查的url,只能对查询接口进行excluded

spring.security.csrf.url.excluded = /csrf/nocheck
<span class="copy-code-btn">复制代码</span></code></pre>
<p>校验之后，若成功，则会顺利执行对应后台功能，若失败，则会返回403的状态码或者301跳转taobao.error的情况，如下:</p>
<pre><code class="copyable">status : 403
message : Invalid CSRF Token '' was found on the request parameter 'p_csrf' or header 'h_csrf'.
=== 
status: 301
location: err2.taobao.com
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            