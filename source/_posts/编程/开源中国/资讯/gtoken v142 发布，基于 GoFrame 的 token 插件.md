
---
title: 'gtoken v1.4.2 发布，基于 GoFrame 的 token 插件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9528'
author: 开源中国
comments: false
date: Mon, 05 Jul 2021 16:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9528'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start"><strong>本次更新：</strong></p> 
<p style="text-align:left">此版本主要对GoFrame最新版本进行了升级测试，没有任何兼容性问题，同时对测试代码进行了完善；</p> 
<p style="text-align:left">欢迎大家加入GoFrame建设中：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114133" target="_blank">https://goframe.org/pages/viewpage.action?pageId=1114133</a></p> 
<h1 style="text-align:start">gtoken</h1> 
<h2 style="text-align:start">介绍</h2> 
<p style="text-align:start">基于<code>GoFrame</code>框架的token插件，通过服务端验证方式实现token认证；已完全可以支撑线上token认证，通过Redis支持集群模式；使用简单，大家可以放心使用；</p> 
<ul> 
 <li>github地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoflyfox%2Fgtoken" target="_blank">https://github.com/goflyfox/gtoken</a></li> 
 <li>gitee地址：<a href="https://gitee.com/goflyfox/gtoken">https://gitee.com/goflyfox/gtoken</a></li> 
</ul> 
<h2 style="text-align:start">gtoken优势</h2> 
<ol> 
 <li>gtoken支撑单点应用使用内存存储，也支持集群使用redis存储；完全适用于企业生产级使用；</li> 
 <li>有效的避免了jwt服务端无法退出问题；</li> 
 <li>解决jwt无法作废已颁布的令牌，只能等到令牌过期问题；</li> 
 <li>通过用户扩展信息存储在服务端，有效规避了jwt携带大量用户扩展信息导致降低传输效率问题；</li> 
 <li>有效避免jwt需要客户端实现续签功能，增加客户端复杂度；支持服务端自动续期，客户端不需要关心续签逻辑；</li> 
</ol> 
<h2 style="text-align:start">特性说明</h2> 
<ol> 
 <li>支持token认证，不强依赖于session和cookie，适用jwt和session认证所有场景；</li> 
 <li>支持单机gcache和集群gredis模式；</li> 
</ol> 
<div style="text-align:start"> 
 <pre><code># 缓存模式 1 gcache 2 gredis
CacheMode = 2
</code></pre> 
</div> 
<ol> 
 <li>支持服务端缓存自动续期功能</li> 
</ol> 
<div style="text-align:start"> 
 <pre><code>// 注：通过MaxRefresh，默认当用户第五天访问时，自动续期
// 超时时间 默认10天
Timeout int
// 缓存刷新时间 默认为超时时间的一半
MaxRefresh int
</code></pre> 
</div> 
<ol> 
 <li>支持分组拦截、全局拦截、深度路径拦截，便于根据个人需求定制拦截器；<strong>建议使用分组拦截方式；</strong></li> 
 <li>框架使用简单，只需要设置登录验证方法以及登录、登出路径即可；</li> 
 <li>在<code>gtoken v1.4.0</code>版本开始支持分组中间件方式实现，但依然兼容全局和深度中间件实现方式；</li> 
</ol> 
<h2 style="text-align:start">安装教程</h2> 
<ul> 
 <li>gopath模式: <code>go get github.com/goflyfox/gtoken</code></li> 
 <li>或者 使用go.mod添加 :<code>require github.com/goflyfox/gtoken latest</code></li> 
</ul> 
<h2 style="text-align:start">分组中间件实现</h2> 
<p style="text-align:start">GoFrame官方推荐使用Group方式实现路由和中间件；</p> 
<h3 style="text-align:start">使用说明</h3> 
<p style="text-align:start">推荐使用分组方式实现</p> 
<div style="text-align:start"> 
 <pre>// 启动gtoken
gfToken := <span style="color:var(--color-prettylights-syntax-keyword)">&</span>gtoken.GfToken&#123;
LoginPath:        <span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>/login<span style="color:var(--color-prettylights-syntax-string)">"</span></span>,
LoginBeforeFunc:  loginFunc,
LogoutPath:       <span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>/user/logout<span style="color:var(--color-prettylights-syntax-string)">"</span></span>,
&#125;
s.Group(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>/admin<span style="color:var(--color-prettylights-syntax-string)">"</span></span>, func(group <span style="color:var(--color-prettylights-syntax-keyword)">*</span>ghttp.RouterGroup) &#123;
group.Middleware(CORS)
gfToken.Middleware(group)

group.ALL(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>/system/user<span style="color:var(--color-prettylights-syntax-string)">"</span></span>, func(r <span style="color:var(--color-prettylights-syntax-keyword)">*</span>ghttp.Request) &#123;
r.Response.WriteJson(gtoken.Succ(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>system user<span style="color:var(--color-prettylights-syntax-string)">"</span></span>))
&#125;)
………………
&#125;)</pre> 
</div> 
<p style="text-align:start">登录方法实现，通过username返回空或者r.ExitAll()\r.Exit()处理认证失败；</p> 
<p style="text-align:start">特别提示：<strong>这里注册的路径严格按照GF group方式，所以注册的路径是<code>/admin/login</code>和<code>/admin/user/logout</code></strong></p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">Login</span>(r <span style="color:var(--color-prettylights-syntax-constant)">*</span>ghttp.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Request</span>) (<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span>, <span style="color:var(--color-prettylights-syntax-keyword)">interface</span>&#123;&#125;) &#123;
username <span style="color:var(--color-prettylights-syntax-constant)">:=</span> r.<span style="color:var(--color-prettylights-syntax-entity)">GetPostString</span>(<span style="color:var(--color-prettylights-syntax-string)">"username"</span>)
passwd <span style="color:var(--color-prettylights-syntax-constant)">:=</span> r.<span style="color:var(--color-prettylights-syntax-entity)">GetPostString</span>(<span style="color:var(--color-prettylights-syntax-string)">"passwd"</span>)

<span style="color:var(--color-prettylights-syntax-comment)">// TODO 进行登录校验</span>
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> username <span style="color:var(--color-prettylights-syntax-constant)">==</span> <span style="color:var(--color-prettylights-syntax-string)">""</span> <span style="color:var(--color-prettylights-syntax-constant)">||</span> passwd <span style="color:var(--color-prettylights-syntax-constant)">==</span> <span style="color:var(--color-prettylights-syntax-string)">""</span> &#123;
r.<span style="color:var(--color-prettylights-syntax-constant)">Response</span>.<span style="color:var(--color-prettylights-syntax-entity)">WriteJson</span>(gtoken.<span style="color:var(--color-prettylights-syntax-entity)">Fail</span>(<span style="color:var(--color-prettylights-syntax-string)">"账号或密码错误."</span>))
r.<span style="color:var(--color-prettylights-syntax-entity)">ExitAll</span>()
&#125;

<span style="color:var(--color-prettylights-syntax-comment)">// 第一个字段是用户唯一标识，第二个字段是扩展参数user data</span>
<span style="color:var(--color-prettylights-syntax-keyword)">return</span> username, <span style="color:var(--color-prettylights-syntax-string)">""</span>
&#125;</pre> 
</div> 
<p style="text-align:start">通过<code>gtoken.GetTokenData(r)</code>获取登录信息</p> 
<h3 style="text-align:start">路径拦截规则</h3> 
<div style="text-align:start"> 
 <pre>    AuthExcludePaths: g.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">SliceStr</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"/user/info"</span>, <span style="color:var(--color-prettylights-syntax-string)">"/system/user/*"</span>&#125;, <span style="color:var(--color-prettylights-syntax-comment)">// 不拦截路径  /user/info,/system/user/info,/system/user,</span></pre> 
</div> 
<ol> 
 <li>分组中间件实现，不需要设置<code>AuthPaths</code>认证路径，设置也没有作用，<strong>需要认证路径为该分组下所有路由</strong>；</li> 
 <li>使用分组拦截的是通过GoFrame的<code>group.Middleware(authMiddleware)</code>方法，对该分组下的所有路由进行拦截；</li> 
 <li>对登录接口路径<code>loginPath</code>和登出接口路径<code>logoutPath</code>做拦截认证放行，登出放行是为了避免认证过期无法登出情况；</li> 
 <li>严格按照GoFrame分组中间件拦截优先级；如果使用跨域中间件，建议放在跨域中间件之后；</li> 
 <li>如果配置<code>AuthExcludePaths</code>路径，会将配置的不拦截路径排除；</li> 
</ol> 
<h3 style="text-align:start">逻辑测试</h3> 
<p style="text-align:start">参考sample项目，先运行main.go，然后可运行api_test.go进行测试并查看结果；验证逻辑说明：</p> 
<ol> 
 <li>访问用户信息，提示未携带token</li> 
 <li>调用登录后，携带token访问正常</li> 
 <li>调用登出提示成功</li> 
 <li>携带之前token访问，提示未登录</li> 
</ol> 
<div style="text-align:start"> 
 <pre>=== RUN   TestAdminSystemUser
    api_admin_test.go:<span style="color:var(--color-prettylights-syntax-constant)">22</span>: <span style="color:var(--color-prettylights-syntax-constant)">1</span>. not login and visit user
    api_admin_test.go:<span style="color:var(--color-prettylights-syntax-constant)">29</span>: &#123;<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>code<span style="color:var(--color-prettylights-syntax-string)">"</span></span>:<span style="color:var(--color-prettylights-syntax-constant)">-401</span>,<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>msg<span style="color:var(--color-prettylights-syntax-string)">"</span></span>:<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>请求错误或登录超时<span style="color:var(--color-prettylights-syntax-string)">"</span></span>,<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>data<span style="color:var(--color-prettylights-syntax-string)">"</span></span>:<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span><span style="color:var(--color-prettylights-syntax-string)">"</span></span>&#125;
    api_admin_test.go:<span style="color:var(--color-prettylights-syntax-constant)">42</span>: <span style="color:var(--color-prettylights-syntax-constant)">2</span>. execute login and visit user
    api_admin_test.go:<span style="color:var(--color-prettylights-syntax-constant)">45</span>: &#123;<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>code<span style="color:var(--color-prettylights-syntax-string)">"</span></span>:<span style="color:var(--color-prettylights-syntax-constant)">0</span>,<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>msg<span style="color:var(--color-prettylights-syntax-string)">"</span></span>:<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>success<span style="color:var(--color-prettylights-syntax-string)">"</span></span>,<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>data<span style="color:var(--color-prettylights-syntax-string)">"</span></span>:<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>system user<span style="color:var(--color-prettylights-syntax-string)">"</span></span>&#125;
    api_admin_test.go:<span style="color:var(--color-prettylights-syntax-constant)">51</span>: <span style="color:var(--color-prettylights-syntax-constant)">3</span>. execute logout
    api_admin_test.go:<span style="color:var(--color-prettylights-syntax-constant)">54</span>: &#123;<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>code<span style="color:var(--color-prettylights-syntax-string)">"</span></span>:<span style="color:var(--color-prettylights-syntax-constant)">0</span>,<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>msg<span style="color:var(--color-prettylights-syntax-string)">"</span></span>:<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>success<span style="color:var(--color-prettylights-syntax-string)">"</span></span>,<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>data<span style="color:var(--color-prettylights-syntax-string)">"</span></span>:<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>Logout success<span style="color:var(--color-prettylights-syntax-string)">"</span></span>&#125;
    api_admin_test.go:<span style="color:var(--color-prettylights-syntax-constant)">60</span>: <span style="color:var(--color-prettylights-syntax-constant)">4</span>. visit user
    api_admin_test.go:<span style="color:var(--color-prettylights-syntax-constant)">65</span>: &#123;<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>code<span style="color:var(--color-prettylights-syntax-string)">"</span></span>:<span style="color:var(--color-prettylights-syntax-constant)">-401</span>,<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>msg<span style="color:var(--color-prettylights-syntax-string)">"</span></span>:<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>请求错误或登录超时<span style="color:var(--color-prettylights-syntax-string)">"</span></span>,<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>data<span style="color:var(--color-prettylights-syntax-string)">"</span></span>:<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span><span style="color:var(--color-prettylights-syntax-string)">"</span></span>&#125;</pre> 
</div> 
<h2 style="text-align:start">全局中间件实现</h2> 
<h3 style="text-align:start">使用说明</h3> 
<p style="text-align:start">只需要配置登录路径、登出路径、拦截路径以及登录校验实现即可</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-comment)">// 启动gtoken</span>
gtoken <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">&</span>gtoken.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">GfToken</span>&#123;
<span style="color:var(--color-prettylights-syntax-constant)">LoginPath</span>:       <span style="color:var(--color-prettylights-syntax-string)">"/login"</span>,
<span style="color:var(--color-prettylights-syntax-constant)">LoginBeforeFunc</span>: loginFunc,
<span style="color:var(--color-prettylights-syntax-constant)">LogoutPath</span>:      <span style="color:var(--color-prettylights-syntax-string)">"/user/logout"</span>,
<span style="color:var(--color-prettylights-syntax-constant)">AuthPaths</span>:        g.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">SliceStr</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"/user"</span>, <span style="color:var(--color-prettylights-syntax-string)">"/system"</span>&#125;, <span style="color:var(--color-prettylights-syntax-comment)">// 这里是按照前缀拦截，拦截/user /user/list /user/add ...</span>
<span style="color:var(--color-prettylights-syntax-constant)">GlobalMiddleware</span>: <span style="color:var(--color-prettylights-syntax-constant)">true</span>,                           <span style="color:var(--color-prettylights-syntax-comment)">// 开启全局拦截，默认关闭</span>
&#125;
gtoken.<span style="color:var(--color-prettylights-syntax-entity)">Start</span>()</pre> 
</div> 
<p style="text-align:start">登录方法实现，通过username返回空或者r.ExitAll()\r.Exit()处理认证失败；</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">Login</span>(r <span style="color:var(--color-prettylights-syntax-constant)">*</span>ghttp.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Request</span>) (<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span>, <span style="color:var(--color-prettylights-syntax-keyword)">interface</span>&#123;&#125;) &#123;
username <span style="color:var(--color-prettylights-syntax-constant)">:=</span> r.<span style="color:var(--color-prettylights-syntax-entity)">GetPostString</span>(<span style="color:var(--color-prettylights-syntax-string)">"username"</span>)
passwd <span style="color:var(--color-prettylights-syntax-constant)">:=</span> r.<span style="color:var(--color-prettylights-syntax-entity)">GetPostString</span>(<span style="color:var(--color-prettylights-syntax-string)">"passwd"</span>)

<span style="color:var(--color-prettylights-syntax-comment)">// TODO 进行登录校验</span>
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> username <span style="color:var(--color-prettylights-syntax-constant)">==</span> <span style="color:var(--color-prettylights-syntax-string)">""</span> <span style="color:var(--color-prettylights-syntax-constant)">||</span> passwd <span style="color:var(--color-prettylights-syntax-constant)">==</span> <span style="color:var(--color-prettylights-syntax-string)">""</span> &#123;
r.<span style="color:var(--color-prettylights-syntax-constant)">Response</span>.<span style="color:var(--color-prettylights-syntax-entity)">WriteJson</span>(gtoken.<span style="color:var(--color-prettylights-syntax-entity)">Fail</span>(<span style="color:var(--color-prettylights-syntax-string)">"账号或密码错误."</span>))
r.<span style="color:var(--color-prettylights-syntax-entity)">ExitAll</span>()
&#125;

<span style="color:var(--color-prettylights-syntax-comment)">// 第一个字段是用户唯一标识，第二个字段是扩展参数user data</span>
<span style="color:var(--color-prettylights-syntax-keyword)">return</span> username, <span style="color:var(--color-prettylights-syntax-string)">""</span>
&#125;</pre> 
</div> 
<p style="text-align:start">通过<code>gtoken.GetTokenData(r)</code>获取登录信息</p> 
<h3 style="text-align:start">路径拦截规则</h3> 
<div style="text-align:start"> 
 <pre>    AuthPaths:        g.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">SliceStr</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"/user"</span>, <span style="color:var(--color-prettylights-syntax-string)">"/system"</span>&#125;,             <span style="color:var(--color-prettylights-syntax-comment)">// 这里是按照前缀拦截，拦截/user /user/list /user/add ...</span>
    AuthExcludePaths: g.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">SliceStr</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"/user/info"</span>, <span style="color:var(--color-prettylights-syntax-string)">"/system/user/*"</span>&#125;, <span style="color:var(--color-prettylights-syntax-comment)">// 不拦截路径  /user/info,/system/user/info,/system/user,</span>
    GlobalMiddleware: <span style="color:var(--color-prettylights-syntax-constant)">true</span>,                           <span style="color:var(--color-prettylights-syntax-comment)">// 开启全局拦截，默认关闭</span></pre> 
</div> 
<ol> 
 <li><code>GlobalMiddleware:true</code>全局拦截的是通过GF的<code>BindMiddleware</code>方法创建拦截<code>/*</code></li> 
 <li><code>GlobalMiddleware:false</code>路径拦截的是通过GF的<code>BindMiddleware</code>方法创建拦截<code>/user*和/system/*</code></li> 
 <li>按照中间件优先级路径拦截优先级很高；如果先实现部分中间件在认证前处理需要切换成全局拦截器，严格按照注册顺序即可；</li> 
 <li>程序先处理认证路径，如果满足；再排除不拦截路径；</li> 
 <li>如果只想用排除路径功能，将拦截路径设置为<code>/*</code>即可；</li> 
</ol> 
<h3 style="text-align:start">逻辑测试</h3> 
<p style="text-align:start">参考sample1项目，先运行main.go，然后可运行api_test.go进行测试并查看结果；验证逻辑说明：</p> 
<ol> 
 <li>访问用户信息，提示未携带token</li> 
 <li>调用登录后，携带token访问正常</li> 
 <li>调用登出提示成功</li> 
 <li>携带之前token访问，提示未登录</li> 
</ol> 
<div style="text-align:start"> 
 <pre>=== RUN   TestSystemUser
    api_test.go:<span style="color:var(--color-prettylights-syntax-constant)">43</span>: <span style="color:var(--color-prettylights-syntax-constant)">1</span>. not login and visit user
    api_test.go:<span style="color:var(--color-prettylights-syntax-constant)">50</span>: &#123;<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>code<span style="color:var(--color-prettylights-syntax-string)">"</span></span>:<span style="color:var(--color-prettylights-syntax-constant)">-401</span>,<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>msg<span style="color:var(--color-prettylights-syntax-string)">"</span></span>:<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>请求错误或登录超时<span style="color:var(--color-prettylights-syntax-string)">"</span></span>,<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>data<span style="color:var(--color-prettylights-syntax-string)">"</span></span>:<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span><span style="color:var(--color-prettylights-syntax-string)">"</span></span>&#125;
    api_test.go:<span style="color:var(--color-prettylights-syntax-constant)">63</span>: <span style="color:var(--color-prettylights-syntax-constant)">2</span>. execute login and visit user
    api_test.go:<span style="color:var(--color-prettylights-syntax-constant)">66</span>: &#123;<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>code<span style="color:var(--color-prettylights-syntax-string)">"</span></span>:<span style="color:var(--color-prettylights-syntax-constant)">0</span>,<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>msg<span style="color:var(--color-prettylights-syntax-string)">"</span></span>:<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>success<span style="color:var(--color-prettylights-syntax-string)">"</span></span>,<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>data<span style="color:var(--color-prettylights-syntax-string)">"</span></span>:<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>system user<span style="color:var(--color-prettylights-syntax-string)">"</span></span>&#125;
    api_test.go:<span style="color:var(--color-prettylights-syntax-constant)">72</span>: <span style="color:var(--color-prettylights-syntax-constant)">3</span>. execute logout
    api_test.go:<span style="color:var(--color-prettylights-syntax-constant)">75</span>: &#123;<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>code<span style="color:var(--color-prettylights-syntax-string)">"</span></span>:<span style="color:var(--color-prettylights-syntax-constant)">0</span>,<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>msg<span style="color:var(--color-prettylights-syntax-string)">"</span></span>:<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>success<span style="color:var(--color-prettylights-syntax-string)">"</span></span>,<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>data<span style="color:var(--color-prettylights-syntax-string)">"</span></span>:<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>Logout success<span style="color:var(--color-prettylights-syntax-string)">"</span></span>&#125;
    api_test.go:<span style="color:var(--color-prettylights-syntax-constant)">81</span>: <span style="color:var(--color-prettylights-syntax-constant)">4</span>. visit user
    api_test.go:<span style="color:var(--color-prettylights-syntax-constant)">86</span>: &#123;<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>code<span style="color:var(--color-prettylights-syntax-string)">"</span></span>:<span style="color:var(--color-prettylights-syntax-constant)">-401</span>,<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>msg<span style="color:var(--color-prettylights-syntax-string)">"</span></span>:<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>请求错误或登录超时<span style="color:var(--color-prettylights-syntax-string)">"</span></span>,<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>data<span style="color:var(--color-prettylights-syntax-string)">"</span></span>:<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span><span style="color:var(--color-prettylights-syntax-string)">"</span></span>&#125;</pre> 
</div> 
<h2 style="text-align:start">返回码及配置项</h2> 
<ol> 
 <li>正常操作成功返回0</li> 
 <li>未登录访问需要登录资源返回401</li> 
 <li>程序异常返回-99，如编解码错误等</li> 
</ol> 
<div style="text-align:start"> 
 <pre>SUCCESS      <span style="color:var(--color-prettylights-syntax-constant)">=</span> <span style="color:var(--color-prettylights-syntax-constant)">0</span>  <span style="color:var(--color-prettylights-syntax-comment)">// 正常</span>
FAIL         <span style="color:var(--color-prettylights-syntax-constant)">=</span> <span style="color:var(--color-prettylights-syntax-constant)">-</span><span style="color:var(--color-prettylights-syntax-constant)">1</span>  <span style="color:var(--color-prettylights-syntax-comment)">// 失败</span>
ERROR        <span style="color:var(--color-prettylights-syntax-constant)">=</span> <span style="color:var(--color-prettylights-syntax-constant)">-</span><span style="color:var(--color-prettylights-syntax-constant)">99</span>  <span style="color:var(--color-prettylights-syntax-comment)">// 异常</span>
UNAUTHORIZED <span style="color:var(--color-prettylights-syntax-constant)">=</span> <span style="color:var(--color-prettylights-syntax-constant)">-</span><span style="color:var(--color-prettylights-syntax-constant)">401</span>  <span style="color:var(--color-prettylights-syntax-comment)">// 未认证</span></pre> 
</div> 
<h3 style="text-align:start">配置项说明</h3> 
<p style="text-align:start">具体可参考<code>GfToken</code>结构体，字段解释如下：</p> 
<table cellspacing="0" style="width:max-content"> 
 <thead> 
  <tr> 
   <th>名称</th> 
   <th>配置字段</th> 
   <th>说明</th> 
   <th>分组中间件</th> 
   <th>全局中间件</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>服务名</td> 
   <td>ServerName</td> 
   <td>默认空即可</td> 
   <td>支持</td> 
   <td>支持</td> 
  </tr> 
  <tr> 
   <td>缓存模式</td> 
   <td>CacheMode</td> 
   <td>1 gcache 2 gredis 默认1</td> 
   <td>支持</td> 
   <td>支持</td> 
  </tr> 
  <tr> 
   <td>缓存key</td> 
   <td>CacheKey</td> 
   <td>默认缓存前缀<code>GToken:</code></td> 
   <td>支持</td> 
   <td>支持</td> 
  </tr> 
  <tr> 
   <td>超时时间</td> 
   <td>Timeout</td> 
   <td>默认10天（毫秒）</td> 
   <td>支持</td> 
   <td>支持</td> 
  </tr> 
  <tr> 
   <td>缓存刷新时间</td> 
   <td>MaxRefresh</td> 
   <td>默认为超时时间的一半（毫秒）</td> 
   <td>支持</td> 
   <td>支持</td> 
  </tr> 
  <tr> 
   <td>Token分隔符</td> 
   <td>TokenDelimiter</td> 
   <td>默认<code>_</code></td> 
   <td>支持</td> 
   <td>支持</td> 
  </tr> 
  <tr> 
   <td>Token加密key</td> 
   <td>EncryptKey</td> 
   <td>默认<code>12345678912345678912345678912345</code></td> 
   <td>支持</td> 
   <td>支持</td> 
  </tr> 
  <tr> 
   <td>认证失败提示</td> 
   <td>AuthFailMsg</td> 
   <td>默认<code>请求错误或登录超时</code></td> 
   <td>支持</td> 
   <td>支持</td> 
  </tr> 
  <tr> 
   <td>是否支持多端登录</td> 
   <td>MultiLogin</td> 
   <td>默认false</td> 
   <td>支持</td> 
   <td>支持</td> 
  </tr> 
  <tr> 
   <td>中间件类型</td> 
   <td>MiddlewareType</td> 
   <td>1、Group 2、Bind 3 、Global；<br> 使用分组模式不需要设置</td> 
   <td>支持</td> 
   <td>支持</td> 
  </tr> 
  <tr> 
   <td>登录路径</td> 
   <td>LoginPath</td> 
   <td>登录接口路径</td> 
   <td>支持</td> 
   <td>支持</td> 
  </tr> 
  <tr> 
   <td>登录验证方法</td> 
   <td>LoginBeforeFunc</td> 
   <td>登录验证需要用户实现方法</td> 
   <td>支持</td> 
   <td>支持</td> 
  </tr> 
  <tr> 
   <td>登录返回方法</td> 
   <td>LoginAfterFunc</td> 
   <td>登录完成后调用</td> 
   <td>支持</td> 
   <td>支持</td> 
  </tr> 
  <tr> 
   <td>登出地址</td> 
   <td>LogoutPath</td> 
   <td>登出接口路径</td> 
   <td>支持</td> 
   <td>支持</td> 
  </tr> 
  <tr> 
   <td>登出验证方法</td> 
   <td>LogoutBeforeFunc</td> 
   <td>登出接口前调用</td> 
   <td>支持</td> 
   <td>支持</td> 
  </tr> 
  <tr> 
   <td>登出返回方法</td> 
   <td>LogoutAfterFunc</td> 
   <td>登出接口完成后调用</td> 
   <td>支持</td> 
   <td>支持</td> 
  </tr> 
  <tr> 
   <td>拦截地址</td> 
   <td>AuthPaths</td> 
   <td>此路径列表进行认证</td> 
   <td>不需要</td> 
   <td>支持</td> 
  </tr> 
  <tr> 
   <td>拦截排除地址</td> 
   <td>AuthExcludePaths</td> 
   <td>此路径列表不进行认证</td> 
   <td>支持</td> 
   <td>支持</td> 
  </tr> 
  <tr> 
   <td>认证验证方法</td> 
   <td>AuthBeforeFunc</td> 
   <td>拦截认证前后调用</td> 
   <td>支持</td> 
   <td>支持</td> 
  </tr> 
  <tr> 
   <td>认证返回方法</td> 
   <td>AuthAfterFunc</td> 
   <td>拦截认证完成后调用</td> 
   <td>支持</td> 
   <td>支持</td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="text-align:start">文档</h2> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fitician.org%2Fpages%2Fviewpage.action%3FpageId%3D1115974" target="_blank">https://itician.org/pages/viewpage.action?pageId=1115974</a></p> 
<h2 style="text-align:start">感谢</h2> 
<ol> 
 <li>gf框架 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgogf%2Fgf" target="_blank">https://github.com/gogf/gf</a></li> 
</ol>
                                        </div>
                                      
</div>
            