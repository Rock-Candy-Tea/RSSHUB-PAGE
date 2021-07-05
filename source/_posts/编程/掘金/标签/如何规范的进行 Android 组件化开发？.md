
---
title: '如何规范的进行 Android 组件化开发？'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a281f821da9465ab3d86614b9e0174f~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 23:15:23 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a281f821da9465ab3d86614b9e0174f~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>现在大厂的开发基本上都是组件化的，所以，还不会组件化的朋友可以多学下。今天和大家分享的就是关于Android 组件化的规范开发。</p>
<p>原文地址：<a href="https://juejin.cn/post/6981337095331659783">www.jianshu.com/p/7bc170d29…</a></p>
</blockquote>
<h2 data-id="heading-0">正文</h2>
<p>进行组件化开发有一段时间了，不久后就要开始一个新项目了，为此整理了目前项目中使用的组件化开发规范，方便在下一个项目上使用。本文的重点是介绍规范和项目架构，仅提供示例代码举例，目前不打算提供示例Demo。如果你还不了解什么是组件化以及如何进行组件化开发的话，建议请先看下面这个文章。</p>
<p><a href="https://www.jianshu.com/p/4603aa41a751" target="_blank" rel="nofollow noopener noreferrer">Android组件化：我们到底该怎样学习和运用组件化？</a></p>
<p><a href="https://www.jianshu.com/p/6b595455dc08" target="_blank" rel="nofollow noopener noreferrer">Android组件化初探【含Demo】</a></p>
<h2 data-id="heading-1">定义</h2>
<p>组件是 <code>Android</code> 项目中一个相对独立的功能模块，是一个抽象的概念，<code>module</code> 是 <code>Android</code> 项目中一个相对独立的代码模块。</p>
<p>在组件化开发的早期，一个组件就只有一个 <code>module</code>，导致很多代码和资源都会下沉到 <code>common</code> 中，导致 <code>common</code> 会变得很臃肿。有的文章说，专门建立一个 <code>module</code> 来存放通用资源，我感觉这样是治标不治本，直到后面看到<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2F6Q818XA5FaHd7jJMFBG60w" target="_blank" rel="nofollow noopener noreferrer">微信Android模块化架构重构实践</a>这篇文章，里面的"模块的一般组织方式"一节提到一个模块应该有多个工程，然后开始在项目对 <code>module</code> 进行拆分。</p>
<p>一般情况下，一个组件有两个 <code>module</code>，一个轻量级的 <code>module</code> 提供外部组件需要和本组件进行交互的接口方法及一些外部组件需要的资源，另一个重量级的 <code>module</code> 完成组件实际的功能和实现轻量级 <code>module</code> 定义的接口方法。</p>
<p><code>module</code> 的命名规范请参考<a href="https://juejin.cn/post/6981337095331659783#module%E5%90%8D">module名</a>，在下文中使用 <code>module-api</code> 代表轻量级的 <code>module</code>，使用 <code>module-impl</code> 代表重量级的 <code>module</code>。</p>
<h2 data-id="heading-2">common组件</h2>
<p><code>common</code> 是一个特殊的组件，不区分轻量级和重量级，它是项目中最底层的组件，基本上所有的其他组件都会依赖 <code>common</code> 组件，<code>common</code> 中放项目中所有弱业务逻辑的代码和解决循环依赖的代码和资源。</p>
<p>一个完整的项目的架构如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a281f821da9465ab3d86614b9e0174f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">弱业务逻辑代码</h3>
<p>何为弱业务逻辑代码？简单来说，就是有一定的业务逻辑，但是这个业务逻辑对于项目中其他组件来说通用的。</p>
<p>比如在 <code>common</code> 组件集成网络请求库，创建一个 <code>HttpTool</code> 工具类，负责初始化网络请求框架，定义网络请求方法，实现组装通用请求参数以及处理全局通用错误等，对于其他组件直接通过这个工具类进行网络请求就可以了。</p>
<p>比如定义界面基类，处理一些通用业务逻辑，比如接入统计分析框架。</p>
<h3 data-id="heading-4">解决循环依赖的代码和资源</h3>
<p>何为解决循环依赖的代码和资源？比如说 <code>module-a-api</code> 有一个类 <code>C</code>，<code>module-b-api</code> 中有一个类 <code>D</code>，在 <code>module-a-api</code> 中需要使用 <code>D</code>，在 <code>module-b-api</code> 中需要使用 <code>C</code>，这样就会造成 <code>module-a-api</code> 需要依赖 <code>module-b-api</code>，而 <code>module-b-api</code> 也会依赖 <code>module-a-api</code>，这就造成了循环依赖，在 <code>Android Studio</code> 中会编译失败。</p>
<p>解决循环依赖的方案就是将 <code>C</code> 和 <code>D</code> 其中的一个，或者两个都下沉到 <code>common</code> 组件中，因为 <code>module-a-api</code> 和 <code>module-b-api</code> 都依赖了 <code>common</code> 组件，至于具体下沉几个，这个根据具体的情况而定，但是原则是<strong>下沉到 <code>common</code> 组件的东西越少越好。</strong></p>
<p>上面的举的例子是代码，资源文件同样也可能会有这个问题。</p>
<h2 data-id="heading-5">module代码结构</h2>
<p>一个组件通常含有一个或多个功能点，比如对于用户组件，它有关于界面、意见反馈、修改账户密码等功能点，在 <code>module</code> 中为每一个功能点创建一个路径，里面放实现该功能的代码，比如 <code>Activity</code>、<code>Dialog</code> 、<code>Adapter</code> 等。除此之外，为了集中管理组件内部资源和统一编码习惯，特地将一部分的通用功能路径固定下来。这些路径包括 <code>api</code>、<code>provider</code>、<code>tool</code> 等。</p>
<p>一般情况下 <code>module</code> 的代码架构如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ec9759b66324697b7c11b3c40e0ad3e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">api</h3>
<p>该路径下放 <code>module</code> 内部使用到的所有网络请求路径和方法，一般使用一个类就够了，比如：<code>UserApi</code>：</p>
<pre><code class="copyable">object UserApi &#123;

    /**
     * 获取个人中心数据
     */
    fun getPersonCenterData(): GetRequest &#123;
        return HttpTool.get(ApiVersion.v1_0_0 + "authUser/myCenter")
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>ApiVersion</code> 全局管理目前项目中使用的所有 <code>api</code> 版本，应当定义在 <code>common</code> 组件的 <code>api</code> 路径下：</p>
<pre><code class="copyable">object ApiVersion &#123;
    const val v1_0_0 = "v1/"
    const val v1_1_0 = "v1_1/"
    const val v1_2_2 = "v1_2_2/"
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">entity</h3>
<p>该路径下放 <code>module</code> 内部使用到的所有实体类（网络请求返回的数据类）。</p>
<p>对于所有从服务器获取的字段，全部定义在构造函数中，且实体类应当实现 <code>Parcelable</code> ，并使用 <code>@Parcelize</code> 注解。对于客户端使用而自己定义的字段，基本上定义为普通成员字段，并使用 <code>@IgnoredOnParcel</code> 注解，如果需要在界面间传递客户端定义的字段，可以将该字段定义在构造函数中，但是必须注明是客户端定义的字段。</p>
<p>示例如下：</p>
<pre><code class="copyable">@Parcelize
class ProductEntity(
    // 产品名称
    var name: String = "",

    // 产品图标
    var icon: String = "",

    // 产品数量（客户端定义字段）
    var count: Int = 0
) : Parcelable &#123;
    // 用户是否选择本产品
    @IgnoredOnParcel
    var isSelected = false
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中 <code>name</code> 和 <code>icon</code> 是从服务器获取的字段，而 <code>count</code> 和 <code>isSelected</code> 是客户端自己定义的字段。</p>
<h3 data-id="heading-8">event</h3>
<p>该路径下放 <code>module</code> 内部使用的事件相关类。对于使用了 <code>EventBus</code> 及类似框架的项目，放事件类，对于使用了 <code>LiveEventBus</code> 的项目，里面只需要放一个类就好，比如：<code>UserEvent</code>：</p>
<pre><code class="copyable">object UserEvent &#123;

    /**
     * 更新用户信息成功事件
     */
    val updateUserInfoSuccessEvent: LiveEventBus.Event<Unit>
        get() = LiveEventBus.get("user_update_user_info_success")
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：对于使用 <code>LiveEventBus</code> 的项目，事件的命名必须用组件名作为前缀，防止事件名重复。</p>
</blockquote>
<h3 data-id="heading-9">route</h3>
<p>该路径下放 <code>module</code> 内部所使用到的界面路径和跳转方法，一般使用一个类就够了，比如：<code>UserRoute</code>：</p>
<pre><code class="copyable">object UserRoute &#123;
    // 关于界面
    const val ABOUT = "/user/about"
    // 常见问题（H5）
    private const val FAQ = "FAQ/"

    /**
     * 跳转至关于界面
     */
    fun toAbout(): RouteNavigation &#123;
        return RouteNavigation(ABOUT)
    &#125;

    /**
     * 跳转至常见问题（H5）
     */
    fun toFAQ(): RouteNavigation? &#123;
        return RouteUtil.getServiceProvider(IH5Service::class.java)
            ?.toH5Activity(FAQ)
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：对于组件内部会跳转的H5界面链接也应当写在路由类中。</p>
</blockquote>
<h3 data-id="heading-10">provider</h3>
<p>该路径下放对外部 <code>module</code> 提供的服务，一般使用一个类就够了。在 <code>module-api</code> 中是一个接口类，在 <code>module-impl</code> 中是该接口类的实现类。</p>
<p>目前采用 <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Falibaba%2FARouter" target="_blank" rel="nofollow noopener noreferrer">ARouter</a> 作为组件化的框架，为了解耦，对其进行了封装，封装示例代码如下：</p>
<pre><code class="copyable">typealias Route = com.alibaba.android.arouter.facade.annotation.Route

object RouteUtil &#123;

    fun <T> getServiceProvider(service: Class<out T>): T? &#123;
        return ARouter.getInstance().navigation(service)
    &#125;
&#125;

class RouteNavigation(path: String) &#123;

    private val postcard = ARouter.getInstance().build(path)

    fun param(key: String, value: Int): RouteNavigation &#123;
        postcard.withInt(key, value)
        return this
    &#125;
    ...
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">示例</h4>
<p>这里介绍如何在外部 <code>module</code> 和 <code>user-impl</code> 跳转至用户组件中的关于界面。</p>
<h5 data-id="heading-12">准备工作</h5>
<p>在 <code>user-impl</code> 中创建路由类，编写关于界面的路由和服务路由及跳转至关于界面方法：</p>
<pre><code class="copyable">object UserRoute &#123;
    // 关于界面
    const val ABOUT = "/user/about"
    // 用户组件服务
    const val USER_SERVICE = "/user/service"

    /**
     * 跳转至关于界面
     */
    fun toAbout(): RouteNavigation &#123;
        return RouteNavigation(ABOUT)
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在关于界面使用路由：</p>
<pre><code class="copyable">@Route(path = UserRoute.ABOUT)
class AboutActivity : MyBaseActivity() &#123;
    ...
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>user-api</code> 中定义跳转界面方法：</p>
<pre><code class="copyable">interface IUserService : IServiceProvider &#123;

    /**
     * 跳转至关于界面
     */
    fun toAbout(): RouteNavigation
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>user-impl</code> 中实现跳转界面方法：</p>
<pre><code class="copyable">@Route(path = UserRoute.USER_SERVICE)
class UserServiceImpl : IUserService &#123;

    override fun toAbout(): RouteNavigation &#123;
        return UserRoute.toAbout()
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-13">界面跳转</h5>
<p>在 <code>user-impl</code> 中可以直接跳转到关于界面：</p>
<pre><code class="copyable">UserRoute.toAbout().navigation(this)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>假设 <code>module-a</code> 需要跳转到关于界面，那么先在 <code>module-a</code> 中配置依赖：</p>
<pre><code class="copyable">dependencies &#123;
    ...
    implementation project(':user-api')
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>module-a</code> 中使用 <strong><code>provider</code></strong> 跳转到关于界面：</p>
<pre><code class="copyable">RouteUtil.getServiceProvider(IUserService::class.java)
    ?.toAbout()
    ?.navigation(this)

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-14">module依赖关系</h5>
<p>此时各个 <code>module</code> 的依赖关系如下：</p>
<pre><code class="copyable">common：基础库、第三方库
user-api：common
user-impl：common、user-api
module-a：common、user-api
App壳：common、user-api、user-impl、module-a、...

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">tool</h3>
<p>该路径下放 <code>module</code> 内部使用的工具方法，一般一个类就够了，比如：<code>UserTool</code>：</p>
<pre><code class="copyable">object UserTool &#123;

    /**
     * 该用户是否是会员
     * @param gradeId 会员等级id
     */
    fun isMembership(gradeId: Int): Boolean &#123;
        return gradeId > 0
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">cache</h3>
<p>该路径下放 <code>module</code> 使用的缓存方法，一般一个类就够了，比如：<code>UserCache</code>：</p>
<pre><code class="copyable">object UserCache &#123;

    // 搜索历史记录列表
    var searchHistoryList: ArrayList<String>
        get() &#123;
            val cacheStr = CacheTool.userCache.getString(SEARCH_HISTORY_LIST)
            return if (cacheStr == null) &#123;
                ArrayList()
            &#125; else &#123;
                JsonUtil.parseArray(cacheStr, String::class.java) ?: ArrayList()
            &#125;
        &#125;
        set(value) &#123;
            CacheTool.userCache.put(SEARCH_HISTORY_LIST, JsonUtil.toJson(value))
        &#125;

    // 搜索历史记录列表
    private const val SEARCH_HISTORY_LIST = "user_search_history_list"
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：</p>
<ol>
<li>缓存Key的命名必须用组件名作为前缀，防止缓存Key重复。</li>
<li><code>CacheTool.userCache</code> 并不是指用户组件的缓存，而是用户的缓存，即当前登录账号的缓存，每个账号会单独存一份数据，相互之间没有干扰。与之对应的是 <code>CacheTool.globalCache</code>，全局缓存，所有的账号会共用一份数据。</li>
</ol>
</blockquote>
<h2 data-id="heading-17">两种module的区别</h2>
<p><code>module-api</code> 中放的都是外部组件需要的，或者说外部组件和 <code>module-impl</code> 都需要的，其他的都应当放在 <code>module-impl</code> 中，对于外部组件需要的但是能通过 <strong><code>provider</code></strong> 方式提供的，都应当把具体的实现放在 <code>module-impl</code> 中，<code>module-api</code> 中只是放一个接口方法。</p>
<p>下表列举项目开发中哪些东西能否放 <code>module-api</code> 中：</p>




























































<table><thead><tr><th>类型</th><th>能否放 <code>module-api</code></th><th>备注</th></tr></thead><tbody><tr><td>功能界面(Activity、Fragment、Dialog)</td><td>不能</td><td>通过 <strong><code>provider</code></strong> 方式提供使用</td></tr><tr><td>基类界面</td><td>部分能</td><td>外部 <code>module</code> 需要使用的可以，其他的放 <code>module-impl</code> 中</td></tr><tr><td>adapter</td><td>部分能</td><td>外部 <code>module</code> 需要使用的可以，其他的放 <code>module-impl</code> 中</td></tr><tr><td>provider</td><td>部分能</td><td>只能放接口类，实现类放 <code>module-impl</code> 中</td></tr><tr><td>tool</td><td>部分能</td><td>外部 <code>module</code> 需要使用的可以，其他的放 <code>module-impl</code> 中</td></tr><tr><td>api、route、cache</td><td>不能</td><td>通过 <strong><code>provider</code></strong> 方式提供使用</td></tr><tr><td>entity</td><td>部分能</td><td>外部 <code>module</code> 需要使用的可以，其他的放 <code>module-impl</code> 中</td></tr><tr><td>event</td><td>部分能</td><td>对使用 <code>EventBus</code> 及类似框架的项目，外部组件需要的可以，其他还是放 <code>module-impl</code> 中</td></tr><tr><td>对于使用了 <code>LiveEventBus</code> 的项目不能，通过 <strong><code>provider</code></strong> 方式提供使用</td><td></td><td></td></tr><tr><td>资源文件和资源变量</td><td>部分能</td><td>需要在 <code>xml</code> 文件中使用的可以， 其他的通过 <strong><code>provider</code></strong> 方式提供使用</td></tr></tbody></table>
<blockquote>
<p>注意：如果仅在 <code>module-impl</code> 中存在工具类，则该工具类命名为 <code>xxTool</code>。如果 <code>module-api</code> 和 <code>module-impl</code> 都存在工具类，则 <code>module-api</code> 中的命名为 <code>xxTool</code>，<code>module-impl</code> 中的命名为 <code>xxTool2</code>。</p>
</blockquote>
<h2 data-id="heading-18">组件单独调试</h2>
<p>在开发过程中，为了查看运行效果，需要运行整个App，比较麻烦，而且可能依赖的其他组件也在开发中，App可能运行不到当前开发的组件。为此可以采用组件单独调试的模式进行开发，减少其他组件的干扰，等开发完成后再切换回 <code>library</code> 的模式。</p>
<p>在组件单独调试模式下，可以增加一些额外的代码来方便开发和调试，比如新增一个入口 <code>Actvity</code>，作为组件单独运行时的第一个界面。</p>
<h3 data-id="heading-19">示例</h3>
<p>这里介绍在 <code>user-impl</code> 中进行组件单独调试。</p>
<p>在项目根目录下的 <code>gradle.properties</code> 文件中新增变量 <code>isDebugModule</code>，通过该变量控制是否进行组件单独调试：</p>
<pre><code class="copyable"># 组件单独调试开关，为ture时进行组件单独调试
isDebugModule = false

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>user-impl</code> 的 <code>build.gradle</code> 的顶部增加以下代码来控制 <code>user-impl</code> 在 <code>Applicaton</code> 和 <code>Library</code> 之间进行切换：</p>
<pre><code class="copyable">if (isDebugModule.toBoolean()) &#123;
    apply plugin: 'com.android.application'
&#125; else &#123;
    apply plugin: 'com.android.library'
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>user-impl</code> 的 <code>src/main</code> 的目录下创建两个文件夹 <code>release</code> 和 <code>debug</code>，<code>release</code> 中放 <code>library</code> 模式下的 <code>AndroidManifest.xml</code>，<code>debug</code> 放 <code>application</code> 模式下的 <code>AndroidManifest.xml</code>、代码和资源，如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/854dd69da73546ffb8ed590ecad570f6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 <code>user-impl</code> 的 <code>build.gradle</code> 中配置上面的创建的代码和资源路径：</p>
<pre><code class="copyable">android &#123;
    ...
    sourceSets &#123;
        if (isDebugModule.toBoolean()) &#123;
            main.manifest.srcFile 'src/main/debug/AndroidManifest.xml'
            main.java.srcDirs += 'src/main/debug'
            main.res.srcDirs += 'src/main/debug'
        &#125; else &#123;
            main.manifest.srcFile 'src/main/release/AndroidManifest.xml'
        &#125;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：完成上述配置后，在 <code>library</code> 模式下，<code>debug</code> 中的代码和资源不会合并到项目中。</p>
</blockquote>
<p>最后在 <code>user-impl</code> 的 <code>build.gradle</code> 中配置 <code>applicationId</code>：</p>
<pre><code class="copyable">android &#123;
    defaultConfig &#123;
        if (isDebugModule.toBoolean()) &#123;
            applicationId "cc.tarylorzhang.demo"
        &#125;
        ...
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：如果碰到65536的问题，在 <code>user-impl</code> 的 <code>build.gradle</code> 中新增以下配置：</p>
<pre><code class="copyable">android &#123;
    defaultConfig &#123;
        ...
        if (isDebugModule.toBoolean()) &#123;
            multiDexEnabled true
        &#125;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上工作都完成后，将 <code>isDebugModule</code> 的值改为 <code>true</code>，则可以开始单独调试用户组件。</p>
<h2 data-id="heading-20">命名规范</h2>
<h3 data-id="heading-21">module名</h3>
<p>组件名如果是单个单词的，直接使用该单词 + <code>api</code> 或 <code>impl</code> 的后缀作为 <code>module</code> 名，如果是多个单词的，多个单词小写使用 <code>-</code> 字符作为连接符，然后在其基础上加 <code>api</code> 或 <code>impl</code> 的后缀作为 <code>module</code> 名。</p>
<h4 data-id="heading-22">示例</h4>
<p>用户组件(<code>User</code>)，它的 <code>module</code> 名为 <code>user-api</code> 和 <code>user-impl</code>；会员卡组件(<code>MembershipCard</code>)，它的 <code>module</code> 名为 <code>membership-card-api</code> 和 <code>membership-card-impl</code>。</p>
<h3 data-id="heading-23">包名</h3>
<p>在应用的 <code>applicationId</code> 的基础上增加组件名后缀作为组件基础包名。</p>
<p>在代码中的包名 <code>module-api</code> 和 <code>module-impl</code> 都直接使用基础包名即可，但是在 <code>Android</code> 中项目 <code>AndroidManifest.xml</code> 文件中的 <code>package</code> 不能重复，否则编译不通过。所以 <code>module-impl</code> 中的 <code>package</code> 使用基础包名，而 <code>module-impl</code> 中的 <code>package</code> 使用基础包名 + <code>api</code> 后缀。</p>
<blockquote>
<p>package 重复的时候，会报 Type package.BuildConfig is defined multiple times 的错误。</p>
</blockquote>
<h4 data-id="heading-24">示例</h4>
<p>应用的 <code>applicationId</code> 为 <code>cc.taylorzhang.demo</code>，对于用户组件(<code>user</code>)，组件基础包名为 <code>cc.taylorzhang.demo.user</code>，则实际包名如下表：</p>




















<table><thead><tr><th></th><th>代码中的包名</th><th>AndroidManifest.xml中的包名</th></tr></thead><tbody><tr><td><code>user-api</code></td><td><code>cc.taylorzhang.demo.user</code></td><td><code>cc.taylorzhang.demo.userapi</code></td></tr><tr><td><code>user-impl</code></td><td><code>cc.taylorzhang.demo.user</code></td><td><code>cc.taylorzhang.demo.user</code></td></tr></tbody></table>
<p>对于多单词的会员卡组件(<code>MembershipCard</code>)，其组件基础包名为 <code>cc.taylorzhang.demo.membershipcard</code>。</p>
<h3 data-id="heading-25">资源文件和资源变量</h3>
<p>所有的资源文件：布局文件、图片等全部要增加组件名作为前缀，所有的资源变量：字符串、颜色等也全部要增加组件名作为前缀，防止资源名重复。</p>
<h4 data-id="heading-26">示例</h4>
<ul>
<li>用户组件(<code>User</code>)，关于界面布局文件命名为：<code>user_activity_about.xml</code>；</li>
<li>用户组件(<code>User</code>)，关于界面标题字符串命名为：<code>user_about_title</code>；</li>
<li>会员卡组件(<code>MembershipCard</code>)，会员卡详情界面布局文件，文件名为：<code>membership_card_activity_detail</code>；</li>
<li>会员卡组件(<code>MembershipCard</code>)，会员卡详情界面标题字符串，文件名为：<code>membership_card_detail_title</code>；</li>
</ul>
<h3 data-id="heading-27">类名</h3>
<p>对于类名没必要增加前缀，比如 <code>UserAboutActivity</code>，因为对资源文件和资源变量增加前缀主要是为了避免重复定义资源导致资源被覆盖的问题，而上面的包名命名规范已经避免了类重复的问题，直接命名 <code>AboutActivity</code> 即可。</p>
<h2 data-id="heading-28">全局管理App环境</h2>
<p><code>App</code> 环境一般分为开发、测试和生产环境，不同环境下使用的网络请求地址大概率是不一样的，甚至一些UI都不一样，在打包的时候手动修改很容易有遗漏，产生不必要的 <code>BUG</code>。应当使用 <code>buildConfigField</code> 在打包的时候将当前环境写入 <code>App</code> 中，在代码中根据读取环境变量，根据不同的环境执行不同的操作。</p>
<h3 data-id="heading-29">示例</h3>
<h4 data-id="heading-30">准备工作</h4>
<p>在 <code>App</code> 壳 的 <code>build.gradle</code> 中给每个<code>buildType</code> 都配置 <code>APP_ENV</code>：</p>
<pre><code class="copyable">android &#123;
    ...
    buildTypes &#123;
        debug &#123;
            buildConfigField "String", "APP_ENV", '\"dev\"'
            ...
        &#125;
        release &#123;
            buildConfigField "String", "APP_ENV", '\"release\"'
            ...
        &#125;
        ctest &#123;
            initWith release

            buildConfigField "String", "APP_ENV", '\"test\"'
            matchingFallbacks = ['release']
        &#125;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：测试环境的 <code>buildType</code> 不能使用 <code>test</code> 作为名字，<code>Android Studio</code> 会报 <code>ERROR: BuildType names cannot start with 'test'</code>，这里在 <code>test</code> 前增加了一个 <code>c</code>。</p>
</blockquote>
<p>在 <code>common</code> 的 <code>tool</code> 路径下创建一个App环境工具类：</p>
<pre><code class="copyable">object AppEnvTool &#123;

    /** 开发环境 */
    const val APP_ENV_DEV = "dev"
    /** 测试环境 */
    const val APP_ENV_TEST = "test"
    /** 生产环境 */
    const val APP_ENV_RELEASE = "release"

    /** 当前App环境，默认为开发环境 */
    private var curAppEnv = APP_ENV_DEV

    fun init(env: String) &#123;
        curAppEnv = env
    &#125;

    /** 当前是否处于开发环境 */
    val isDev: Boolean
        get() = curAppEnv == APP_ENV_DEV

    /** 当前是否处于测试环境 */
    val isTest: Boolean
        get() = curAppEnv == APP_ENV_TEST

    /** 当前是否处于生产环境 */
    val isRelease: Boolean
        get() = curAppEnv == APP_ENV_RELEASE

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>Application</code> 中初始化App环境工具类：</p>
<pre><code class="copyable">class DemoApplication : Application() &#123;

    override fun onCreate() &#123;
        super.onCreate()

        // 初始化App环境工具类
        AppEnvTool.init(BuildConfig.APP_ENV)
        ...
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-31">使用App环境工具类</h4>
<p>这里介绍根据App环境使用不同的网络请求地址：</p>
<pre><code class="copyable">object CommonApi &#123;

    // api开发环境地址
    private const val API_DEV_URL = "https://demodev.taylorzhang.cc/api/"
    // api测试环境地址
    private const val API_TEST_URL = "https://demotest.taylorzhang.cc/api/"
    // api生产环境地址
    private const val API_RELEASE_URL = "https://demo.taylorzhang.cc/api/"
    // api地址
    val API_URL = getUrlByEnv(API_DEV_URL, API_TEST_URL, API_RELEASE_URL)

    // H5开发环境地址
    private const val H5_DEV_URL = "https://demodev.taylorzhang.cc/m/"
    // H5测试环境地址
    private const val H5_TEST_URL = "https://demotest.taylorzhang.cc/m/"
    // H5生产环境地址
    private const val H5_RELEASE_URL = "https://demo.taylorzhang.cc/m/"
    // H5地址
    val H5_URL = getUrlByEnv(H5_DEV_URL, H5_TEST_URL, H5_RELEASE_URL)

    private fun getUrlByEnv(devUrl: String, testUrl: String, releaseUrl: String): String &#123;
        return when &#123;
            AppEnvTool.isDev -> devUrl
            AppEnvTool.isTest -> testUrl
            else -> releaseUrl
        &#125;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-32">打包</h4>
<p>通过不同的命令打包，打出对应的App环境包：</p>
<pre><code class="copyable"># 打开发环境包
./gradlew clean assembleDebug

# 打测试环境包
./gradlew clean assembleCtest

# 打生产环境包
./gradlew clean assembleRelease

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-33">全局管理版本信息</h2>
<p>项目中的 <code>module</code> 变多之后，如果要修改第三方库和App使用的SDK版本是一件很蛋疼的事情。应当建立一个配置文件进行管理，其他地方使用配置文件中设置的版本。</p>
<h3 data-id="heading-34">示例</h3>
<p>在项目根目录下创建一个配置文件 <code>config.gradle</code>，里面放版本信息：</p>
<pre><code class="copyable">ext &#123;
    compile_sdk_version = 28
    min_sdk_version = 17
    target_sdk_version = 28

    arouter_compiler_version = '1.2.2'
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在项目根目录下的 <code>build.gradle</code> 文件中的最上方使用以下代码引入配置文件：</p>
<pre><code class="copyable">apply from: "config.gradle"

<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建 <code>module</code> 后，修改该 <code>module</code> 中的 <code>build.gradle</code> 文件，将 <code>SDK</code> 版本默认值换成配置文件中的变量，按需添加第三方依赖，并使用 <code>$</code> + 配置文件中的变量作为第三方库的版本：</p>
<pre><code class="copyable">android &#123;
    ...
    compileSdkVersion compile_sdk_version

    defaultConfig &#123;
        ...
        minSdkVersion min_sdk_version
        targetSdkVersion target_sdk_version
    &#125;
&#125;

dependencies &#123;
    ...
    kapt "com.alibaba:arouter-compiler:$arouter_compiler_version"
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-35">混淆</h2>
<p>混淆文件不应该在 <code>App</code> 壳中集中定义，应当在每个 <code>module</code> 中各自定义自己的混淆。</p>
<h3 data-id="heading-36">示例</h3>
<p>这里介绍配置 <code>user-impl</code> 的混淆，先在 <code>user-impl</code> 的 <code>build.gradle</code> 中配置消费者混淆文件：</p>
<pre><code class="copyable">android &#123;
    defaultConfig &#123;
        ...
        consumerProguardFiles 'proguard-rules.pro'
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>proguard-rules.pro</code> 文件中写入该 <code>module</code> 的混淆：</p>
<pre><code class="copyable"># 实体类
-keepclassmembers class cc.taylorzhang.demo.user.entity.** &#123; *; &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-37">总结</h2>
<p>组件化开发应当遵守"高内聚，低耦合"的原则，尽量少的对外暴露细节。如果用一句话来总结的话，就是代码和资源能放 <code>module-impl</code> 里面的就都放在 <code>module-impl</code>，因为代码隔离问题实在不能放 <code>module-impl</code> 里面的才放 <code>module-api</code>，最后因为涉及到循环依赖问题的才往 <code>common</code> 中放。</p>
<h2 data-id="heading-38">最后</h2>
<p>想要进行Android组件化专项学习的朋友可以观摩下前面写的两篇文章：</p>
<p><a href="https://www.jianshu.com/p/4603aa41a751" target="_blank" rel="nofollow noopener noreferrer">Android组件化：我们到底该怎样学习和运用组件化？</a></p>
<p><a href="https://www.jianshu.com/p/6b595455dc08" target="_blank" rel="nofollow noopener noreferrer">Android组件化初探【含Demo】</a></p>
<p><a href="https://www.jianshu.com/p/d20c8e39c703" target="_blank" rel="nofollow noopener noreferrer">Android组件化：得到APP，代码隔离也难不倒组件的按序初始化</a></p>
<p>或者，大家也可以去B站看这个阿婆主的搬运视频：<a href="https://space.bilibili.com/549975384" target="_blank" rel="nofollow noopener noreferrer">Android开发骆驼</a></p>
<p><strong>长风破浪会有时，直挂云帆济沧海。加油~</strong></p></div>  
</div>
            