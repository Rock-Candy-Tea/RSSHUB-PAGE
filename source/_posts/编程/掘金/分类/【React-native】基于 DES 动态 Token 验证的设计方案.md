
---
title: '【React-native】基于 DES 动态 Token 验证的设计方案'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46cd5b6c0d24490692dcedfaf93e0066~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 21:48:43 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46cd5b6c0d24490692dcedfaf93e0066~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>​</p>
<p>前提：由于现有框架已经形成，但是需要增加在每次调用api的时候，进行token认证，认证通过才能允许访问接口。以防止<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Flucky_wss%2Farticle%2Fdetails%2F78683928" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/lucky_wss/article/details/78683928" ref="nofollow noopener noreferrer">越权访问</a>。所以，准备在代价最小的情况下，进行修改。</p>
<hr>
<h2 data-id="heading-0">总体思路：</h2>
<blockquote>
<p>1，在<strong>app</strong>登录成功后，服务端<strong>生成一个长达200的字符序列</strong>（不重复，当然也可以是<strong>500</strong>，<strong>1000</strong>）存入数据库，同时<strong>返回给app</strong>。</p>
<p>2，<strong>app</strong>拿到序列后，每次访问接口，在header里用该序列中的一个加上用户id（<strong>密码+用户id</strong>）进行<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2Fdes%25E5%25AF%25B9%25E7%25A7%25B0%25E5%258A%25A0%25E5%25AF%2586%2F9002660%3Ffr%3Daladdin" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/des%E5%AF%B9%E7%A7%B0%E5%8A%A0%E5%AF%86/9002660?fr=aladdin" ref="nofollow noopener noreferrer">des加密</a>后生成token。</p>
<p>3，服务端拦截器获取该token，进行校验，如果通过，则允许访问接口，并且在数据库中删除该序列中的该密码（<strong>防止重复使用</strong>）。</p>
</blockquote>
<hr>
<h2 data-id="heading-1">详细设计：</h2>
<h3 data-id="heading-2">一，新建数据库表</h3>
<p>数据库新增一张<strong>USER_AUTHORITY</strong>表，用于存储用户<strong>id</strong>和对于的密码序列，不必担心数据量大，在用户退出删除该记录，在用户登录之前，会重置一次该序列。</p>
<p>表结构很简单，如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46cd5b6c0d24490692dcedfaf93e0066~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://juejin.cn/post/6995044931052470309" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer">​</p>
<hr>
<h3 data-id="heading-3">二，密码序列的生成</h3>
<p>对于密码序列的生成，这里是截取UUID的前八位，然后需要的长度是在调用的时候输入（<strong>当然，你可以把这个长度设置放到数据库或者配置文件里，如果以后不够，可以轻松的增长。</strong> ）。如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">private <span class="hljs-keyword">static</span> <span class="hljs-built_in">Set</span><<span class="hljs-built_in">String</span>> <span class="hljs-function"><span class="hljs-title">productAuthoritys</span>(<span class="hljs-params">int num</span>)</span>&#123;
<span class="hljs-built_in">Set</span><<span class="hljs-built_in">String</span>> setString = <span class="hljs-keyword">new</span> TreeSet<<span class="hljs-built_in">String</span>>();
<span class="hljs-keyword">for</span>(int i = setString.size() ;i<num;i++) &#123;
setString.add(UUID.randomUUID().toString().replace(<span class="hljs-string">"-"</span>, <span class="hljs-string">""</span>).substring(<span class="hljs-number">0</span>, <span class="hljs-number">8</span>));
&#125;
<span class="hljs-keyword">return</span> setString;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995044931052470309" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里直接明文返回给<strong>app</strong>端即可，因为<strong>app</strong>端会对此密码进行再加密后使用。 </p>
<hr>
<h3 data-id="heading-4">三，APP存储密码序列</h3>
<p>登录成功后，<strong>app</strong>对获取到的密码序列进行存储，这里使用的是<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcloud.tencent.com%2Fdeveloper%2Fsection%2F1373126" target="_blank" rel="nofollow noopener noreferrer" title="https://cloud.tencent.com/developer/section/1373126" ref="nofollow noopener noreferrer">AsyncStorage</a>存储到本地。</p>
<p>由于<strong>AsyncStorage</strong>存储的是字符串，故这里做了一点转换。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> AsyncStorage.setItem(<span class="hljs-string">"AuthorityPools"</span>, <span class="hljs-built_in">JSON</span>.stringify(responseData.AuthorityPools).replace(<span class="hljs-regexp">/"/g</span>,<span class="hljs-string">""</span>).replace(<span class="hljs-string">"["</span>,<span class="hljs-string">""</span>).replace(<span class="hljs-string">"]"</span>,<span class="hljs-string">""</span>), <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error</span>) </span>&#123;
                <span class="hljs-keyword">if</span> (error) &#123;
                    alert(<span class="hljs-string">'存储失败'</span>);
                &#125; <span class="hljs-keyword">else</span> &#123;
                    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'chenggong'</span>);
                &#125;&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995044931052470309" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h3 data-id="heading-5">四，请求header中加入token </h3>
<p>在每次访问时，<strong>header</strong>里面加入<strong>token</strong>。</p>
<p>每次需要获取新的<strong>authorityCode</strong>加入<strong>token</strong>中，(此<strong>处DES为加密方法，这里每个人的DES均不同，就不贴了，如有需要，可以留言或联系我</strong>）。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//通用请求中header</span>
<span class="hljs-keyword">const</span> _getHeader = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> authorityCode = getServerTime();
    <span class="hljs-comment">//未加密前的数据</span>
    <span class="hljs-keyword">let</span> proCode = DES.encryptForToken(AppStore.getUserID());
    <span class="hljs-keyword">let</span> token = DES.encryptForToken(<span class="hljs-built_in">this</span>.authorityCode + <span class="hljs-string">'@'</span> + proCode);
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-string">'Accept'</span>: <span class="hljs-string">'application/json'</span>,
        <span class="hljs-string">'Content-Type'</span>: <span class="hljs-string">'application/x-www-form-urlencoded;application/json;'</span>,
        <span class="hljs-string">'Token'</span>: token,
    &#125;;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995044931052470309" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>成功之后，会把该<strong>AuthorityPools（密码序列）</strong> 中的一个<strong>authorityCode</strong>拿出来进行使用，然后删除该<strong>authorityCode</strong>后重新存储。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//授权码</span>
<span class="hljs-built_in">this</span>.authorityCode = <span class="hljs-string">""</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getServerTime</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">//调用接口增加 token ，从本地存储获取，避免越权。</span>
    <span class="hljs-keyword">let</span> AuthorityPools = AsyncStorage.getItem(<span class="hljs-string">'AuthorityPools'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error, result</span>) </span>&#123;
        result = result == <span class="hljs-literal">null</span> ? <span class="hljs-string">""</span> :result;
        <span class="hljs-built_in">this</span>.authorityCode = result.split(<span class="hljs-string">","</span>)[<span class="hljs-number">0</span>];
        AsyncStorage.setItem(<span class="hljs-string">"AuthorityPools"</span>, result.replace(<span class="hljs-built_in">this</span>.authorityCode + <span class="hljs-string">","</span>, <span class="hljs-string">""</span>), <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error</span>) </span>&#123;
            <span class="hljs-keyword">if</span> (error) &#123;
                Alert.alert(
                    <span class="hljs-string">'错误'</span>,
                    <span class="hljs-string">'获取token数据失败'</span>,
                    [
                        &#123;
                            <span class="hljs-attr">text</span>: <span class="hljs-string">'重新登录'</span>,
                            <span class="hljs-attr">onPress</span>: <span class="hljs-function">() =></span> AppDispatcher.dispatch(&#123;<span class="hljs-attr">actionType</span>: AppConstants.FORCE_LOGOUT&#125;),
                            <span class="hljs-attr">type</span>: <span class="hljs-string">'plain-text'</span>
                        &#125;,
                        &#123;<span class="hljs-attr">text</span>: <span class="hljs-string">'取消'</span>, <span class="hljs-attr">onPress</span>: <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'取消'</span>), <span class="hljs-attr">style</span>: <span class="hljs-string">'cancel'</span>&#125;
                    ]
                );
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'get authorityCode success！'</span>);
            &#125;
        &#125;);
    &#125;)
    <span class="hljs-keyword">return</span> AuthorityPools;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995044931052470309" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h3 data-id="heading-6">五，服务端<strong>Filter</strong>进行拦截校验。</h3>
<p>这里，可以对<strong>get</strong>进行进行放行，只拦截除了<strong>get</strong>以外的请求。如下，获取<strong>header</strong>中<strong>token</strong>。</p>
<pre><code class="hljs language-java copyable" lang="java">String token = DES.quickDecrypt(req.getHeader(<span class="hljs-string">"Token"</span>) == <span class="hljs-keyword">null</span> ? <span class="hljs-string">""</span> : req.getHeader(<span class="hljs-string">"Token"</span>))
.toLowerCase().trim();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6995044931052470309" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此后，就取出数据库中该用户的密码序列进行比较，比较成功后，放行，不成功则拒绝访问。</p>
<p><strong>注：用户id取决于token中携带的用户id而不是session中的id。</strong></p>
<hr>
<h3 data-id="heading-7">六，可能会遇到的问题</h3>
<p>1，由于<strong>AsyncStorage</strong>是异步存储，可以会出现上一次访问的密码序列，在本次才会进行调用。我这里的解决方案是在登录成功后，任意调用一个get接口一次即可解决异步。当然，还有<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.liaoxuefeng.com%2Fwiki%2F0014316089557264a6b348958f449949df42a6d3a2e542c000%2F00144661533005329786387b5684be385062a121e834ac7000" target="_blank" rel="nofollow noopener noreferrer" title="https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00144661533005329786387b5684be385062a121e834ac7000" ref="nofollow noopener noreferrer">async/await </a>的方式，但我试了没有用，可能我版本太低。</p>
<hr>
<p>总结，这个方案搞了三天，之前走了很多弯路子。如每次访问之前请求一次时间戳（太卡，而且请求是回调请求，获取的时间戳不同步。）</p>
<p>此方案可以说很好的解决了我的问题，此外还有其他的加密方式，如<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fyan7%2Fp%2F7857833.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/yan7/p/7857833.html" ref="nofollow noopener noreferrer">JWT</a>，但是<strong>JWT</strong>不能实时的变化，如果该访问被拦截后，使用该<strong>Token</strong>可以继续进行访问。</p>
<p><strong>Bingo~</strong></p>
<p>​</p></div>  
</div>
            