
---
title: 'XPage系列_是时候抛弃ButterKnife了'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/128b3b893d264708810f0da677e17a0e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 10:57:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/128b3b893d264708810f0da677e17a0e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<blockquote>
<p>作为 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fxuexiangjys.blog.csdn.net%2Farticle%2Fdetails%2F102639857" target="_blank" rel="nofollow noopener noreferrer" title="https://xuexiangjys.blog.csdn.net/article/details/102639857" ref="nofollow noopener noreferrer">X-Library系列框架</a> 的灵魂所在，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxuexiangjys%2FXPage" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xuexiangjys/XPage" ref="nofollow noopener noreferrer">XPage</a> 开源两年以来，一直致力于降低Fragment使用的难度，努力实现一个Activity多Fragment的Android开发模式。</p>
</blockquote>
<p>前段时间, 在观望了许久之后, 我终于更新了<strong>Android Studio的最新版本(北极狐)</strong>, 发现项目中使用ButterKnife注解id的代码出现了警告，警告信息如下:</p>
<blockquote>
<p>Resource IDs will be non-final in Android Gradle Plugin version 5.0, avoid using them as annotation attributes</p>
</blockquote>
<p>警告信息告诉我们在Gradle 5.0的插件中Resource 的Id值将不会再是final类型，因此应该避免在注解属性中使用Id。这意味着如果我们把Gradle插件升级到5.0版本之后ButterKnife将无法再被使用！而且在ButterKnife的官方文档上也看到了<strong>ButterKnife被标注弃用</strong>的信息：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/128b3b893d264708810f0da677e17a0e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>因为当初设计XPage是为了能够更方便的使用Fragment, 所以就默认集成了ButterKnife. 如果我还想继续使用XPage的话, 就不得不把Gradle插件降到5.0版本以下, 这在ButterKnife被废弃, Viewbinding取而代之的大趋势下, 显然是不合适的.</p>
<p>果不其然, 我的XPage的开源项目很快就被使用者提了<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxuexiangjys%2FXPage%2Fissues%2F23" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xuexiangjys/XPage/issues/23" ref="nofollow noopener noreferrer">去除ButterKnife的issue</a>, 具体如下:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/995068efaae64c1990ab8c8adbf1ba5c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样看来, XPage去除ButterKnife依赖是势在必行的, 于是就有了这次<strong>XPage 3.3.0版本</strong>的升级.</p>
<h2 data-id="heading-1">升级后有什么变化</h2>
<blockquote>
<p>这次升级主要包含了两个部分: <strong>使用gson代替fastjson</strong> 和 <strong>去除butterknife依赖</strong>, 全方面向Google看齐。</p>
</blockquote>
<h3 data-id="heading-2">使用gson代替fastjson</h3>
<p>为什么使用gson代替fastjson呢? 我主要是出于以下两点考虑:</p>
<ul>
<li>fastjson之前就经常爆出了好几次比较严重的安全漏洞, 安全性方面存在缺陷.</li>
<li>目前Android项目使用gson的居多, 并且是Google开源维护的,充分相信Google的实力.</li>
</ul>
<h3 data-id="heading-3">去除butterknife依赖</h3>
<p>去除butterknife依赖, 使用ViewBinding代替是趋势所向. 那么使用ViewBinding代替有哪些好处呢? 下面我简单列举一下:</p>
<ul>
<li>
<p><strong>类型安全</strong>: ViewBinding会基于布局中的View生成类型正确的属性。比如，在布局中放入了一个 TextView ，视图绑定就会暴露出一个 TextView 类型的属性供开发中使用。</p>
</li>
<li>
<p><strong>空安全</strong>: ViewBinding会检测某个视图是不是只在一些配置下存在，并依据结果生成带有 @Nullable 注解的属性。所以即使在多种配置下定义的布局文件，视图绑定依然能够保证空安全。</p>
</li>
<li>
<p><strong>减少控件变量的定义</strong>: ViewBinding会自动生成一个绑定类, 我们可以直接通过这个绑定对象去访问布局中的控件, 无需再为每个控件的访问去定义一个个的变量.</p>
</li>
</ul>
<h2 data-id="heading-4">升级3.3.0版本注意事项</h2>
<h3 data-id="heading-5">依赖发生变化</h3>
<blockquote>
<p>3.3.0版本之后无需依赖butterknife.</p>
</blockquote>
<ul>
<li>3.3.0及以上版本，只需要在项目中依赖XPage即可.</li>
</ul>
<pre><code class="copyable">dependencies &#123;
  ...
  implementation 'com.github.xuexiangjys.XPage:xpage-lib:3.3.0'
  annotationProcessor 'com.github.xuexiangjys.XPage:xpage-compiler:3.3.0'
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>3.2.0及以下版本，除需要在项目中依赖XPage以外, 还需要依赖butterknife.</li>
</ul>
<pre><code class="copyable">dependencies &#123;
  ...
  // XPage
  implementation 'com.github.xuexiangjys.XPage:xpage-lib:3.2.0'
  annotationProcessor 'com.github.xuexiangjys.XPage:xpage-compiler:3.2.0'
  // ButterKnife的sdk
  implementation 'com.jakewharton:butterknife:10.1.0'
  annotationProcessor 'com.jakewharton:butterknife-compiler:10.1.0'
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">接口发生变化</h3>
<blockquote>
<p>为了能够让XPage更好地使用上ViewBinding, 我对XPageFragment以及XPageActivity的部分接口做出了调整.</p>
</blockquote>
<ul>
<li>删除了<strong>XPageFragment</strong>中的<code>getLayoutId</code>抽象方法, 取而代之的是<code>inflateView</code>抽象方法.</li>
</ul>
<pre><code class="copyable">    /**
     * 加载控件
     *
     * @param inflater  inflater
     * @param container 容器
     * @return 根布局
     */
    protected abstract View inflateView(LayoutInflater inflater, ViewGroup container);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>删除了<strong>XPageActivity</strong>中的<code>getLayoutId</code>抽象方法, 取而代之的是<code>getCustomRootView</code>方法.</li>
</ul>
<pre><code class="copyable">    /**
     * 获取自定义根布局
     *
     * @return 自定义根布局
     */
    protected View getCustomRootView() &#123;
        return null;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">混淆配置发生变化</h3>
<blockquote>
<p>由于此次XPage升级使用gson代替了fastjson, 因此混淆配置需要进行修改.</p>
</blockquote>
<ul>
<li>3.2.0及以上版本，使用的是gson进行序列化的，所以配置如下：</li>
</ul>
<pre><code class="copyable"># gson
-keepattributes Signature
-keepattributes *Annotation*
-dontwarn sun.misc.**
-keep class com.google.gson.examples.android.model.** &#123; <fields>; &#125;
-keep class * extends com.google.gson.TypeAdapter
-keep class * implements com.google.gson.TypeAdapterFactory
-keep class * implements com.google.gson.JsonSerializer
-keep class * implements com.google.gson.JsonDeserializer
-keepclassmembers,allowobfuscation class * &#123;
  @com.google.gson.annotations.SerializedName <fields>;
&#125;
-keep,allowobfuscation,allowshrinking class com.google.gson.reflect.TypeToken
-keep,allowobfuscation,allowshrinking class * extends com.google.gson.reflect.TypeToken

# xpage
-keep class com.xuexiang.xpage.annotation.** &#123; *; &#125;
-keep class com.xuexiang.xpage.config.** &#123; *; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>3.1.1及以下版本，使用的是fastjson进行序列化的，所以配置如下：</li>
</ul>
<pre><code class="copyable"># fastjson
-dontwarn com.alibaba.fastjson.**
-keep class com.alibaba.fastjson.** &#123; *; &#125;
-keepattributes Signature

# xpage
-keep class com.xuexiang.xpage.annotation.** &#123; *; &#125;
-keep class com.xuexiang.xpage.config.** &#123; *; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">模板工程</h2>
<p>以上的升级内容, 我已在最新的模板工程中做了相应的更新, 想偷懒的同学可以直接拿模板工程使用.</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxuexiangjys%2FTemplateAppProject" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xuexiangjys/TemplateAppProject" ref="nofollow noopener noreferrer">Android应用空壳模板工程</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxuexiangjys%2FTemplateSimpleProject" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xuexiangjys/TemplateSimpleProject" ref="nofollow noopener noreferrer">简化版Android空壳模板工程</a></li>
</ul>
<h2 data-id="heading-9">相关链接</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fxuexiangjys.blog.csdn.net%2Farticle%2Fdetails%2F109085587" target="_blank" rel="nofollow noopener noreferrer" title="https://xuexiangjys.blog.csdn.net/article/details/109085587" ref="nofollow noopener noreferrer">史上最方便的Android页面框架XPage使用指南</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fxuexiangjys.blog.csdn.net%2Farticle%2Fdetails%2F108923027" target="_blank" rel="nofollow noopener noreferrer" title="https://xuexiangjys.blog.csdn.net/article/details/108923027" ref="nofollow noopener noreferrer">Navigation和XPage框架相比谁更香</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxuexiangjys%2FXPage" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xuexiangjys/XPage" ref="nofollow noopener noreferrer">XPage项目地址：https://github.com/xuexiangjys/XPage</a></li>
</ul>
<h2 data-id="heading-10">最后</h2>
<p>非常感谢大家对<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxuexiangjys%2FXPage" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xuexiangjys/XPage" ref="nofollow noopener noreferrer">XPage</a> 的支持，喜欢的小伙伴可以到项目的Github主页：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxuexiangjys%2FXPage" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xuexiangjys/XPage" ref="nofollow noopener noreferrer">github.com/xuexiangjys…</a> 点击star支持一下哦！</p>
<blockquote>
<p>我是xuexiangjys，一枚热爱学习，爱好编程，致力于Android架构研究以及开源项目经验分享的技术up主。获取更多资讯，欢迎微信搜索公众号：<strong>【我的Android开源之旅】</strong></p>
</blockquote></div>  
</div>
            