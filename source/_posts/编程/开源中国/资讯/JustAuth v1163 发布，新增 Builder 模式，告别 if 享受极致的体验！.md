
---
title: 'JustAuth v1.16.3 发布，新增 Builder 模式，告别 if 享受极致的体验！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6662'
author: 开源中国
comments: false
date: Mon, 16 Aug 2021 10:21:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6662'
---

<div>   
<div class="content">
                                                                                            <h1>更新内容</h1> 
<ul> 
 <li>发布 v1.16.3</li> 
 <li>新增 
  <ul> 
   <li>集成“企业微信的第三方应用”平台登录</li> 
  </ul> </li> 
 <li>PR 
  <ul> 
   <li><code>AuthRequst</code> 增加 <code>Builder</code> 构建方式，使用起来更简单。 ( <a href="https://gitee.com/yadong.zhang/JustAuth/pulls/27" target="_blank">gitee *27</a>)</li> 
   <li>使用 Github Action 添加发布快照的 workflow。 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjustauth%2FJustAuth%2Fpull%2F126" target="_blank">#126</a>)</li> 
   <li>新增了企业微信的第三方应用登录，<code>AuthWeChatEnterpriseThirdQrcodeRequest</code>。 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjustauth%2FJustAuth%2Fpull%2F127" target="_blank">#127</a>)</li> 
   <li>添加快照版本对应更详细的文档。 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjustauth%2FJustAuth%2Fpull%2F128" target="_blank">#128</a>)</li> 
  </ul> </li> 
 <li>修改 
  <ul> 
   <li>在 Gitee PR (<a href="https://gitee.com/yadong.zhang/JustAuth/pulls/27" target="_blank">*27</a>) 的基础上重构代码，增加 Builder 方式创建 AuthRequest</li> 
   <li>解决 Line 登录的错误。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjustauth%2FJustAuth%2Fissues%2F122" target="_blank">#122</a></li> 
  </ul> </li> 
</ul> 
<p> </p> 
<h1>Builder 方式使用介绍</h1> 
<h2 style="text-align:left">Builder 方式一</h2> 
<p style="text-align:left">静态配置 <code>AuthConfig</code></p> 
<div style="text-align:left"> 
 <div> 
  <pre><strong>AuthRequest</strong> authRequest = <strong>AuthRequestBuilder</strong>.<span style="color:#008080">builder</span>()
    .<span style="color:#008080">source</span>(<span style="color:#dd2200">"github"</span>)
    .<span style="color:#008080">authConfig</span>(<strong>AuthConfig</strong>.<span style="color:#008080">builder</span>()
        .<span style="color:#008080">clientId</span>(<span style="color:#dd2200">"clientId"</span>)
        .<span style="color:#008080">clientSecret</span>(<span style="color:#dd2200">"clientSecret"</span>)
        .<span style="color:#008080">redirectUri</span>(<span style="color:#dd2200">"redirectUri"</span>)
        .<span style="color:#008080">build</span>())
    .<span style="color:#008080">build</span>();</pre> 
 </div> 
</div> 
<h2 style="text-align:left">Builder 方式二</h2> 
<p style="text-align:left">动态获取并配置 <code>AuthConfig</code></p> 
<div style="text-align:left"> 
 <div> 
  <pre><strong>AuthRequest</strong> authRequest = <strong>AuthRequestBuilder</strong>.<span style="color:#008080">builder</span>()
    .<span style="color:#008080">source</span>(<span style="color:#dd2200">"gitee"</span>)
    .<span style="color:#008080">authConfig</span>((source) -> &#123;
        <span style="color:#888888">// 通过 source 动态获取 AuthConfig</span>
        <span style="color:#888888">// 此处可以灵活的从 sql 中取配置也可以从配置文件中取配置</span>
        <strong>return</strong> <strong>AuthConfig</strong>.<span style="color:#008080">builder</span>()
            .<span style="color:#008080">clientId</span>(<span style="color:#dd2200">"clientId"</span>)
            .<span style="color:#008080">clientSecret</span>(<span style="color:#dd2200">"clientSecret"</span>)
            .<span style="color:#008080">redirectUri</span>(<span style="color:#dd2200">"redirectUri"</span>)
            .<span style="color:#008080">build</span>();
    &#125;)
    .<span style="color:#008080">build</span>();</pre> 
 </div> 
</div> 
<h2 style="text-align:left">Builder 方式支持自定义的平台</h2> 
<div style="text-align:left"> 
 <div> 
  <pre><strong>AuthRequest</strong> authRequest = <strong>AuthRequestBuilder</strong>.<span style="color:#008080">builder</span>()
    <span style="color:#888888">// 关键点：将自定义实现的 AuthSource 配置上</span>
    .<span style="color:#008080">extendSource</span>(<strong>AuthExtendSource</strong>.<span style="color:#008080">values</span>())
    <span style="color:#888888">// source 对应 AuthExtendSource 中的枚举 name</span>
    .<span style="color:#008080">source</span>(<span style="color:#dd2200">"other"</span>)
    <span style="color:#888888">// ... 其他内容不变，参考上面的示例</span>
    .<span style="color:#008080">build</span>();</pre> 
 </div> 
</div>
                                        </div>
                                      
</div>
            