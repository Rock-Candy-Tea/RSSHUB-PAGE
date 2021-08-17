
---
title: 'JAP 1.0.4 正式发布，支持自定 token、自定义验证 client_secret 等新特性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4026'
author: 开源中国
comments: false
date: Mon, 16 Aug 2021 18:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4026'
---

<div>   
<div class="content">
                                                                                            <h1>更新内容</h1> 
<ul> 
 <li>fix: [jap-ids] 支持生成自定义 token（包含 access_token 和 refresh_token）。 (Gitee<a href="https://gitee.com/fujieid/jap/issues/I3U1ON">#I3U1ON:把assess-token换成自己服务的</a>)</li> 
 <li>fix: [jap-ids] 支持自定义验证 <code>client_secret</code>，适配多种场景，如：BCrypt 等。 (Gitee<a href="https://gitee.com/fujieid/jap/issues/I44032">#I44032:【jap-ids】 支持自定义校验 client_secret 的方法</a>)</li> 
 <li>feat: [jap-ids] 当启用 <code>IdsConfig#enableDynamicIssuer</code> 时，支持自定义 <code>context-path</code></li> 
 <li>fix: [jap-ids] 解决“刷新token后，用新的access_token无法获取用户信息”问题。 (Gitee<a href="https://gitee.com/fujieid/jap/issues/I3XHTK">#I3XHTK:jap-ids 1.0.2刷新token后，用新的access_token无法获取用户信息</a>)</li> 
 <li>feat: [jap-oauth2] <code>Oauth2Strategy</code> 支持使用以下方法： <code>refreshToken</code>、<code>revokeToken</code>、<code>getUserInfo</code></li> 
 <li>fix: [jap-social] 无法同时自定义<code>SocialStrategy</code>的 <code>JapCache</code> and <code>AuthStateCache</code>.(Github<a href="https://gitee.com/fujieid/jap/issues/I3V15K">#6:报错 'token' of undefined</a>)</li> 
 <li>fix: [jap-core] 修复 <code>userId</code> 为空时 NPE 异常. (Github<a href="https://gitee.com/fujieid/jap/issues/I3U1ON">#5:把assess-token换成自己服务的</a>)</li> 
 <li>doc: 更改 issue 和 pr 的模板</li> 
</ul>
                                        </div>
                                      
</div>
            