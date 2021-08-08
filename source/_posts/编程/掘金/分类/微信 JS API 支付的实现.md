
---
title: '微信 JS API 支付的实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f9615cf256a4d1ca45296d86bf91574~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 08 Aug 2021 00:57:11 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f9615cf256a4d1ca45296d86bf91574~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第8天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<blockquote>
<p>本期带来 微信 JSAPI 支付 (即微信浏览器内支付或微信公众号支付) 的前端开发</p>
</blockquote>
<blockquote>
<p>文中支付相关的信息，包括但不限于支付ID，微信签名，公众号ID均已做错误处理。</p>
</blockquote>
<blockquote>
<p>更多文章在我的github及个人公众号【全栈道路】上，欢迎观赏<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fprogrammer-zhang%2Ffront-end" title="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fprogrammer-zhang%2Ffront-end" target="_blank">【前端知识点】</a>，如有受益，不要钱，小手点个Star</p>
</blockquote>
<h2 data-id="heading-0">阅读本文您将收获</h2>
<ul>
<li>微信支付权限开通</li>
<li>微信支付前端如何处理</li>
<li>微信支付相关问题解决</li>
</ul>
<h2 data-id="heading-1">前期工作</h2>
<h3 data-id="heading-2">微信支付权限开通</h3>
<ul>
<li>微信申请支付授权</li>
<li>注意是开通 JSAPI 支付，不是H5支付</li>
<li>附 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fpay.weixin.qq.com%2Fwiki%2Fdoc%2Fapi%2Fjsapi.php%3Fchapter%3D3_1" target="_blank" rel="nofollow noopener noreferrer" title="https://pay.weixin.qq.com/wiki/doc/api/jsapi.php?chapter=3_1" ref="nofollow noopener noreferrer">官方开通授权文档</a>，请正确填写相关信息。</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f9615cf256a4d1ca45296d86bf91574~tplv-k3u1fbpfcp-watermark.image" alt="wechat-pay-auth.png" loading="lazy" referrerpolicy="no-referrer"></p>
<div>图-微信支付权限开通(图片来源：微信官方)</div>
<h3 data-id="heading-3">微信公众平台配置信息</h3>
<ul>
<li>设置支付目录(请正确填写相关信息)
<ul>
<li>配置路径: 商户平台 --> 产品中心 --> 开发配置</li>
</ul>
</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1a4baecbccf4100905d889e6eaeb9fd~tplv-k3u1fbpfcp-watermark.image" alt="wechat-pay-conf.png" loading="lazy" referrerpolicy="no-referrer"></p>
<div>图-微信JSAPI支付-支付目录配置(图片来源：微信官方)</div>
<ul>
<li>配置授权支付域名
<ul>
<li>配置域名除了要在微信公众平台进行配置外，还需要将微信提供的密钥文件放在配置域名的根目录，也就是服务器的根目录，在浏览器中访问能直接访问到就好。</li>
</ul>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bdd204d4b8d048189b6ec1630e4d5481~tplv-k3u1fbpfcp-watermark.image" alt="wechat-pay-host.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75e1fdd98a8d43439f1045398c3f43ec~tplv-k3u1fbpfcp-watermark.image" alt="wechat-pay-host2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<div>图-微信网页授权域名设置(图片来源：微信官方)</div>
<h2 data-id="heading-4">开发</h2>
<h3 data-id="heading-5">微信支付流程</h3>
<ul>
<li>
<p>技术流程</p>
<ul>
<li>前端微信授权 => 提交订单给后端 => 后端生成订单id => 前端接收订单参数包含订单id等 => 调用微信JDK => 传送相关参数给微信 => 调起微信支付 => 微信支付 callback => 前端结束 => 用户支付成功后端收到微信回调(前端和后端的微信支付成功回调未必同时同步)</li>
</ul>
</li>
<li>
<p>业务流程时序图(图片来自微信官方)</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6af7614a0a14bf29bfc5fafd01c3009~tplv-k3u1fbpfcp-watermark.image" alt="wechat-pay-uml.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">前端微信授权</h3>
<ul>
<li><a href="https://juejin.cn/post/6993694640612474917/" target="_blank" title="https://juejin.cn/post/6993694640612474917/">前端微信授权</a>请看我的这篇文章</li>
</ul>
<h3 data-id="heading-7">前端发起生成订单请求</h3>
<ul>
<li>前端向后端发起 <code>生成订单</code> 请求</li>
<li>创建订单成功拿到订单 微信同一订单接口订单id后调起微信支付</li>
</ul>
<h3 data-id="heading-8">前端调起微信支付</h3>
<ul>
<li>
<p>微信支付传参</p>
<ul>
<li><code>appId</code> : <code>"wx2421b1c4370ec12a",     //公众号名称，由商户传入</code></li>
<li><code>timeStamp</code> : <code>"1395712654",         //时间戳，自1970年以来的秒数</code></li>
<li><code>nonceStr</code> : <code>"e61463f8efa94090b1f366cccfbbb555", //随机串</code></li>
<li><code>package</code> : <code>"prepay_id=u802345jgfjsddgsdg888",     // 传递参数，prepay_id即为微信订单id</code></li>
<li><code>signType</code> : <code>"MD5",         //微信签名方式</code></li>
<li><code>paySign</code> : <code>"70EA570631E4BB79628FBCA99534C63FF7FADD89" //微信签名</code></li>
</ul>
</li>
<li>
<p>调起微信支付</p>
</li>
</ul>
<pre><code class="copyable">invokeWxPay(wxPayData) &#123;
let self = this
WeixinJSBridge.invoke('getBrandWCPayRequest', JSON.parse(wxPayData), function(res)&#123;
    if(res.err_msg == "get_brand_wcpay_request:ok" )&#123;
        // 使用以上方式判断前端返回,微信团队郑重提示：
        // res.err_msg将在用户支付成功后返回ok，但并不保证它绝对可靠。
    &#125; else if (res.err_msg == "get_brand_wcpay_request:cancel") &#123;
// 支付取消回调
        &#125; else &#123;
// 支付失败回调
        &#125;
&#125;)
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">设置前端支付回调</h3>
<ul>
<li>支付成功建议跳转至共同的订单状态页，正常情况下，微信给予后端的订单成功确认会很快，但是异常情况难免存在，建议增加订单状态确认页去确认订单。</li>
</ul>
<h2 data-id="heading-10">Q&A</h2>
<h3 data-id="heading-11"><code>response_type</code> 参数错误</h3>
<ul>
<li>原因： <code>vue hash</code> 模式会带有一个 <code>#</code> 号，如果回调地址中含有 <code>#</code> 而没有做转义，授权时就会报错</li>
<li>解决方案：<code>redirect_uri</code> 使用 <code>encodeURIComponent()</code> 进行转码</li>
</ul>
<h3 data-id="heading-12">支付失败缺少参数</h3>
<ul>
<li>原因：若检查过确实参数都齐全，则是传参格式的问题，微信调起支付 <code>WeixinJSBridge.invoke</code> 传参为 JSON 格式</li>
<li>解决方案：将后端 <code>response</code> 进行解析后传入</li>
</ul>
<h3 data-id="heading-13">微信登录失效，没有scope权限</h3>
<ul>
<li>原因：服务号未认证 或 <code>APPID</code> 填写错误 或 微信支付认证过期</li>
<li>解决方案：重新认证服务号 、检查 <code>APPID</code> 是否填写错误、更换登录授权方式</li>
</ul>
<h3 data-id="heading-14">当前页面URL未注册</h3>
<ul>
<li>原因：未在微信开放平台设置支付目录 或 支付域名</li>
<li>解决方案：下单接口使用的商户号在商户平台配置对应的支付目录</li>
</ul>
<h2 data-id="heading-15">写在最后</h2>
<p>如果你觉得这篇文章对你有益，烦请点赞以及分享给更多需要的人！</p>
<h5 data-id="heading-16">欢迎关注【全栈道路】及微信公众号【全栈道路】，获取更多好文及免费书籍！</h5>
<h5 data-id="heading-17">有需要【百度】&【字节跳动】&【京东】&【猿辅导】内推的也请留言哦，你将享受VIP级极速内推服务~</h5>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c14fed1c40c414093ee3d1a203a2806~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"> <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/49482570e618471a86be90ccd1d5757e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-18">往期好文</h2>
<p><a href="https://juejin.cn/post/6991424007069237262" title="https://juejin.cn/post/6991424007069237262" target="_blank">创建个性化的 Github 个人主页</a></p>
<p><a href="https://juejin.cn/post/6901104219995635725" title="https://juejin.cn/post/6901104219995635725" target="_blank">面试官问你<code><img></code>是什么元素时你怎么回答</a></p>
<p><a href="https://juejin.cn/post/6922727457212612621" title="https://juejin.cn/post/6922727457212612621" target="_blank">特殊的JS 浮点数的存储与计算</a></p>
<p><a href="https://juejin.cn/post/6844904116267778055" title="https://juejin.cn/post/6844904116267778055" target="_blank">[万字长文]百度和好未来面试经含答案 | 掘金技术征文</a></p>
<p><a href="https://juejin.cn/post/6879418373365563399" title="https://juejin.cn/post/6879418373365563399" target="_blank">前端实用正则表达式&小技巧，一股脑全丢给你🏆 掘金技术征文|双节特别篇</a></p>
<p><a href="https://juejin.cn/post/6888924266008412167" title="https://juejin.cn/post/6888924266008412167" target="_blank">冷门的 HTML tabindex 详解</a></p>
<p><a href="https://juejin.cn/post/6885952653075939335" title="https://juejin.cn/post/6885952653075939335" target="_blank">几行代码教你解决微信生成海报及二维码</a></p>
<p><a href="https://juejin.cn/post/6878097147649064974" title="https://juejin.cn/post/6878097147649064974" target="_blank">Vue3.0 响应式数据原理：ES6 Proxy</a></p>
<p><a href="https://juejin.cn/post/6844904078615511054" title="https://juejin.cn/post/6844904078615511054" target="_blank">[前端面试]前端缓存问题看这篇，让面试官爱上你</a></p>
<p><a href="https://juejin.cn/post/6992184390210027527" title="https://juejin.cn/post/6992184390210027527" target="_blank">如何优雅地画一条细线</a></p>
<p><a href="https://juejin.cn/post/6844904065688666119" title="https://juejin.cn/post/6844904065688666119" target="_blank">[三分钟小文]前端性能优化-HTML、CSS、JS部分</a></p>
<p><a href="https://juejin.cn/post/6844904065688682510" title="https://juejin.cn/post/6844904065688682510" target="_blank">[三分钟小文]前端性能优化-页面加载速度优化</a></p>
<p><a href="https://juejin.cn/post/6844904065692860424" title="https://juejin.cn/post/6844904065692860424" target="_blank">[三分钟小文]前端性能优化-网络传输层优化</a></p></div>  
</div>
            