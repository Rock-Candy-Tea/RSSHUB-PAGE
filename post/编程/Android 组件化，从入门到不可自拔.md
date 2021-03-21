
---
title: Android 组件化，从入门到不可自拔
categories: 
    - 编程
    - 掘金 - 标签
author: 掘金 - 标签
comments: false
date: Mon, 15 Mar 2021 05:33:59 GMT
thumbnail: https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/231a5f546f8d4ef289043412670f36af~tplv-k3u1fbpfcp-watermark.image
---

<div>   
<div class="markdown-body"><style>.markdown-body{color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%}.markdown-body p{color:#595959;font-size:15px;line-height:2;font-weight:400}.markdown-body p+p{margin-top:16px}.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6{padding:30px 0;margin:0;color:#135ce0}.markdown-body h1{position:relative;text-align:center;font-size:22px;margin:50px 0}.markdown-body h1:before{position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)}.markdown-body h2{position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0}.markdown-body h3{font-size:16px}.markdown-body ul{list-style:disc outside;margin-left:2em;margin-top:1em}.markdown-body li{line-height:2;color:#595959}.markdown-body img.loaded{margin:0 auto;display:block}.markdown-body blockquote{background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5}.markdown-body blockquote p{color:#666;line-height:2}.markdown-body a{color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none}.markdown-body em strong,.markdown-body strong{color:#036aca}.markdown-body hr{border-top:1px solid #135ce0}.markdown-body pre{overflow:auto}.markdown-body code,.markdown-body pre{overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace}.markdown-body pre>code{font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8}.markdown-body code{word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em}.markdown-body table{border-collapse:collapse;margin:1rem 0;overflow-x:auto}.markdown-body table td,.markdown-body table th{border:1px solid #dfe2e5;padding:.6em 1em}.markdown-body table tr{border-top:1px solid #dfe2e5}.markdown-body table tr:nth-child(2n){background-color:#f6f8fa}</style><blockquote>
<p><strong>提醒：本文很长，建议先关注和收藏。</strong></p>
</blockquote>
<h1 data-id="heading-0">前言</h1>
<p>组件化技术，在 Android 开发中有着举足轻重的作用。</p>
<p>随着时间推移，软件项目很多都会变得越来越庞杂。此时，采用组件化技术，对项目进行改造，是一种较优的方案。</p>
<p>本文对组件化技术进行了分析和总结，并搭建了一个基础的组件化项目Demo，源码在 Github 上：<a href="https://github.com/ZuoHailong/AndroidModuleDemo" target="_blank" rel="nofollow noopener noreferrer">点这里点这里</a></p>
<h1 data-id="heading-1">谈谈模块化</h1>
<p>要聊组件化，惯例是要谈谈模块化的，毕竟它与组件化确实有一些相同点，在组件化的项目中它也会与组件化发生关联。</p>
<h2 data-id="heading-2">什么是模块化</h2>
<p>模块化开发，是每个开发者都熟悉的。</p>
<p>即将常用的UI、网络请求、数据库操作、第三方库的使用等公共部分抽离封装成基础模块，或者将大的业务上拆分为多个小的业务模块，这些业务模块又依赖于公共基础模块的开发方式。</p>
<p>更宏观上，又会将这些不同的模块组合为一个整体，打包成一个完成的项目。</p>
<h2 data-id="heading-3">模块化的好处</h2>
<p>模块化有哪些好处呢？</p>
<p><strong>复用</strong></p>
<p>首先，基础模块，可为业务模块所复用；</p>
<p>其次，子业务模块，可为父业务模块，甚至不同的项目所复用。</p>
<p><strong>解耦</strong></p>
<p>降低模块间的耦合，避免出现一处代码修改，牵一发而动全身的尴尬局面。</p>
<p><strong>协同开发</strong></p>
<p>项目越来越大，团队人数越来越多，模块化开发可在尽量解耦的情况下，使不同的开发人员专注于自己负责的业务，同步开发，显著提供开发效率。</p>
<h2 data-id="heading-4">模块化的弊端</h2>
<p>那，模块化开发有没有什么弊端呢？</p>
<p>有。</p>
<p>任凭模块化做得多么好，还是跳不出是组合在单一项目下的。随着项目的发展与迭代，模块化开发渐渐显现了以下的问题：</p>
<p><strong>项目代码量越来越大</strong></p>
<p>每次的编译速度越来越慢，哪怕几行代码的修改，都需要花费好几分钟的时间，等着编译器编译运行结束后，才能查看代码的执行结果，这极大的降低了开发效率；</p>
<p><strong>业务模块越来越多</strong></p>
<p>不可避免地产生越来越多且复杂的耦合，哪怕一次小的功能更新，也需要对修改代码耦合的模块进行充分测试；</p>
<p><strong>团队人数越来越多</strong></p>
<p>这就要求开发人员了解与之业务相关的每一个业务模块，防止出现某位开发人员修改代码导致其他模块出现 bug 的情况，这个要求对于开发人员显然是不友好的；</p>
<p>那怎样解决模块化开发的这些弊端呢？</p>
<p>当然是组件化喽！</p>
<h1 data-id="heading-5">聊聊组件化</h1>
<p>组件化可以说是 Android 中级开发工程师必备技能了，能有效解决许多单一项目下开发中出现的问题。</p>
<p>并且我要强调的是，组件化真的不难，还没搞过的小伙伴不要怂。</p>
<h2 data-id="heading-6">什么是组件化</h2>
<p>组件，顾名思义，“组装的零件”，术语上叫做软件单元，可用于组装在应用程序中。</p>
<p>所以，组件化，要更关注可复用性、更注重关注点分离、功能单一、高内聚、粒度更小、是业务上能划分的最小单元，毕竟是“组装的零件”嘛！</p>
<p>从这个角度上看，组件化的粒度，似乎要比模块化的粒度更小。</p>
<p>不过，我个人认为，要把组件化拆分到如此小的粒度，不可能，也没有必要。在组件化项目的实际开发中，组件化的粒度，是要比模块化的粒度更大的。</p>
<h2 data-id="heading-7">组件化的好处</h2>
<p>首先要说的是，上述模块化的好处，组件化都有，不再赘述；上述模块化的弊端，组件化都给解决了，具体如下：</p>
<ol>
<li>
<p>组件，既可以作为 library，又可以单独作为 application，便于单独编译单独测试，大大的提高了编译和开发效率；</p>
</li>
<li>
<p>（业务）组件，可有自己独立的版本，业务线互不干扰，可单独编译、测试、打包、部署；</p>
</li>
<li>
<p>各业务线共有的公共模块可开发为组件，作为依赖库供各业务线调用，减少重复代码编写，减少冗余，便于维护；</p>
</li>
<li>
<p>通过 gradle 配置文件，可对第三方库进行统一管理，避免版本冲突，减少冗余；</p>
</li>
<li>
<p>通过 gradle 配置文件，可实现 application 与 library 灵活组合与拆分，可以更快速的响应需求方对功能模块的选择。</p>
</li>
</ol>
<h1 data-id="heading-8">组件化实践</h1>
<p>首先要说明的是，下述是一个简单的不能再简单的组件化案例，只求帮助大家搭建起组件化的架构，功能上极其简约。</p>
<p>九层之台，起于累土。我们这就开始搭组件化的架构吧！</p>
<h2 data-id="heading-9">组件化架构</h2>
<p>先上一张组件化项目整体架构图
<img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/231a5f546f8d4ef289043412670f36af~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
其中的“业务组件”，既可以作为 application 单独打包为 apk，又可以作为 library 灵活组合为综合一些的应用程序。</p>
<p>大多数开发者做组件化时面对的业务需求，都是上面这种情况。</p>
<p>我司的需求略有不同，不是将子业务组件组合为整体应用程序，而是反其道而行之，需要将已上线项目拆分给不同的业务公司使用，在不同业务系统中，项目的逻辑和代码会有区别，且版本不统一。</p>
<p>基于此，我搭建项目架构如下图所示，其中“m_moudle_main”是公司主要的、且逻辑和代码相同的业务组件，“b_moudle_north”和“b_moudle_south”是拆分出来的业务组件，管理各自私有的逻辑和代码，且版本有差别。
<img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/76c16fc2f68e4dafab16cab76659ebeb~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
从Android工程看，结构如下图所示：</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd3df0662ad14d698a3d4ddac0726e1b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
注：取moudle名，手动加上“b_” “m_” “x_”这样的前缀，只是为了便于分辨组件层次。</p>
<h2 data-id="heading-10">统一配置文件</h2>
<p>在项目根目录下，自建 config.gradle 文件，对项目进行全局统一配置，并对版本和依赖进行统一管理，源码如下：</p>
<pre><code class="hljs language-gradle copyable" lang="gradle"><span class="hljs-comment">/**
 * 全局统一配置
 */</span>
ext {
    <span class="hljs-comment">/**
     * module开关统一声明在此处
     * true：module作为application，可单独打包为apk
     * false：module作为library，可作为宿主application的组件
     */</span>
    isNorthModule = <span class="hljs-keyword">false</span>
    isSouthModule = <span class="hljs-keyword">false</span>

    <span class="hljs-comment">/**
     * 版本统一管理
     */</span>
    versions = [
            applicationId           : <span class="hljs-string">"com.niujiaojian.amd"</span>,        <span class="hljs-comment">//应用ID</span>
            versionCode             : <span class="hljs-number">100</span>,                    <span class="hljs-comment">//版本号</span>
            versionName             : <span class="hljs-string">"1.0.0"</span>,              <span class="hljs-comment">//版本名称</span>

            compileSdkVersion       : <span class="hljs-number">28</span>,
            minSdkVersion           : <span class="hljs-number">21</span>,
            targetSdkVersion        : <span class="hljs-number">28</span>,

            androidSupportSdkVersion: <span class="hljs-string">"28.0.0"</span>,
            constraintlayoutVersion : <span class="hljs-string">"1.1.3"</span>,
            runnerVersion           : <span class="hljs-string">"1.1.0-alpha4"</span>,
            espressoVersion         : <span class="hljs-string">"3.1.0-alpha4"</span>,
            junitVersion            : <span class="hljs-string">"4.12"</span>,
            annotationsVersion      : <span class="hljs-string">"28.0.0"</span>,
            appcompatVersion        : <span class="hljs-string">"1.0.0-beta01"</span>,
            designVersion           : <span class="hljs-string">"1.0.0-beta01"</span>,

            multidexVersion         : <span class="hljs-string">"1.0.2"</span>,

            butterknifeVersion      : <span class="hljs-string">"10.1.0"</span>,

            arouterApiVersion       : <span class="hljs-string">"1.4.1"</span>,
            arouterCompilerVersion  : <span class="hljs-string">"1.2.2"</span>,
            arouterAnnotationVersion: <span class="hljs-string">"1.0.4"</span>
    ]

    <span class="hljs-keyword">dependencies</span> = [
            <span class="hljs-string">"appcompat"</span>           : <span class="hljs-string">"androidx.appcompat:appcompat:${versions["</span>appcompatVersion<span class="hljs-string">"]}"</span>,
            <span class="hljs-string">"constraintlayout"</span>    : <span class="hljs-string">"androidx.constraintlayout:constraintlayout:${versions["</span>constraintlayoutVersion<span class="hljs-string">"]}"</span>,
            <span class="hljs-string">"runner"</span>              : <span class="hljs-string">"androidx.test:runner:${versions["</span>runnerVersion<span class="hljs-string">"]}"</span>,
            <span class="hljs-string">"espresso_core"</span>       : <span class="hljs-string">"androidx.test.espresso:espresso-core:${versions["</span>espressoVersion<span class="hljs-string">"]}"</span>,
            <span class="hljs-string">"junit"</span>               : <span class="hljs-string">"junit:junit:${versions["</span>junitVersion<span class="hljs-string">"]}"</span>,
            <span class="hljs-comment">//注释处理器</span>
            <span class="hljs-string">"support_annotations"</span> : <span class="hljs-string">"com.android.support:support-annotations:${versions["</span>annotationsVersion<span class="hljs-string">"]}"</span>,
            <span class="hljs-string">"design"</span>              : <span class="hljs-string">"com.google.android.material:material:${versions["</span>designVersion<span class="hljs-string">"]}"</span>,

            <span class="hljs-comment">//方法数超过65535解决方法64K MultiDex分包方法</span>
            <span class="hljs-string">"multidex"</span>            : <span class="hljs-string">"androidx.multidex:multidex:2.0.0"</span>,

            <span class="hljs-comment">//阿里路由</span>
            <span class="hljs-string">"arouter_api"</span>         : <span class="hljs-string">"com.alibaba:arouter-api:${versions["</span>arouterApiVersion<span class="hljs-string">"]}"</span>,
            <span class="hljs-string">"arouter_compiler"</span>    : <span class="hljs-string">"com.alibaba:arouter-compiler:${versions["</span>arouterCompilerVersion<span class="hljs-string">"]}"</span>,
            <span class="hljs-string">"arouter_annotation"</span>  : <span class="hljs-string">"com.alibaba:arouter-annotation:${versions["</span>arouterAnnotationVersion<span class="hljs-string">"]}"</span>,

            <span class="hljs-comment">//黄油刀</span>
            <span class="hljs-string">"butterknife"</span>         : <span class="hljs-string">"com.jakewharton:butterknife:${versions["</span>butterknifeVersion<span class="hljs-string">"]}"</span>,
            <span class="hljs-string">"butterknife_compiler"</span>: <span class="hljs-string">"com.jakewharton:butterknife-compiler:${versions["</span>butterknifeVersion<span class="hljs-string">"]}"</span>
    ]
}
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在project的build.gradle中引入config.gradle文件：</p>
<pre><code class="hljs language-gradle copyable" lang="gradle">apply <span class="hljs-keyword">from</span>: <span class="hljs-string">"config.gradle"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">基础公共组件</h2>
<p>基础公共组件 common 将一直作为 library 存在，所有业务组件都需要依赖 common 组件。</p>
<p>common 组件主要负责封装公共部分，如网络请求、数据存储、自定义控件、各种工具类等，以及对第三方库进行统一依赖等。</p>
<p>下图是我的 common 组件的包结构图：</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1406e96aa77b441fa0fbf1adda8b9bc4~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>前文有言，common 组件还负责对第三方库进行统一依赖，这样上层业务组件就不需要再对第三方库进行重复依赖了，其 build.gradle 源码如下所示：</p>
<pre><code class="hljs language-gradle copyable" lang="gradle">apply plugin: <span class="hljs-string">'com.android.library'</span>
apply plugin: <span class="hljs-string">'com.jakewharton.butterknife'</span>

……

<span class="hljs-keyword">dependencies</span> {
    <span class="hljs-comment">// 在项目中的libs中的所有的.jar结尾的文件，都是依赖</span>
    implementation <span class="hljs-keyword">fileTree</span>(dir: <span class="hljs-string">'libs'</span>, <span class="hljs-keyword">include</span>: [<span class="hljs-string">'*.jar'</span>])

    <span class="hljs-comment">//把implementation 用api代替,它是对外部公开的, 所有其他的module就不需要添加该依赖</span>
    api rootProject.ext.<span class="hljs-keyword">dependencies</span>[<span class="hljs-string">"appcompat"</span>]
    api rootProject.ext.<span class="hljs-keyword">dependencies</span>[<span class="hljs-string">"constraintlayout"</span>]
    api rootProject.ext.<span class="hljs-keyword">dependencies</span>[<span class="hljs-string">"junit"</span>]
    api rootProject.ext.<span class="hljs-keyword">dependencies</span>[<span class="hljs-string">"runner"</span>]
    api rootProject.ext.<span class="hljs-keyword">dependencies</span>[<span class="hljs-string">"espresso_core"</span>]
    <span class="hljs-comment">//注释处理器，butterknife所必需</span>
    api rootProject.ext.<span class="hljs-keyword">dependencies</span>[<span class="hljs-string">"support_annotations"</span>]

    <span class="hljs-comment">//MultiDex分包方法</span>
    api rootProject.ext.<span class="hljs-keyword">dependencies</span>[<span class="hljs-string">"multidex"</span>]

    <span class="hljs-comment">//Material design</span>
    api rootProject.ext.<span class="hljs-keyword">dependencies</span>[<span class="hljs-string">"design"</span>]

    <span class="hljs-comment">//黄油刀</span>
    api rootProject.ext.<span class="hljs-keyword">dependencies</span>[<span class="hljs-string">"butterknife"</span>]
    annotationProcessor rootProject.ext.<span class="hljs-keyword">dependencies</span>[<span class="hljs-string">"butterknife_compiler"</span>]

    <span class="hljs-comment">//Arouter路由</span>
    annotationProcessor rootProject.ext.<span class="hljs-keyword">dependencies</span>[<span class="hljs-string">"arouter_compiler"</span>]
    api rootProject.ext.<span class="hljs-keyword">dependencies</span>[<span class="hljs-string">"arouter_api"</span>]
    api rootProject.ext.<span class="hljs-keyword">dependencies</span>[<span class="hljs-string">"arouter_annotation"</span>]

}
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">业务组件</h2>
<p>业务组件在 library 模式下，向上组合为整体性项目；在 application 模式下，可独立运行。</p>
<p>其 build.gradle 源码如下：</p>
<pre><code class="hljs language-gradle copyable" lang="gradle"><span class="hljs-keyword">if</span> (<span class="hljs-keyword">Boolean</span>.valueOf(rootProject.ext.isModule_North)) {
    apply plugin: <span class="hljs-string">'com.android.application'</span>
} <span class="hljs-keyword">else</span> {
    apply plugin: <span class="hljs-string">'com.android.library'</span>
}
apply plugin: <span class="hljs-string">'com.jakewharton.butterknife'</span>

……

<span class="hljs-keyword">dependencies</span> {
    implementation <span class="hljs-keyword">fileTree</span>(dir: <span class="hljs-string">'libs'</span>, <span class="hljs-keyword">include</span>: [<span class="hljs-string">'*.jar'</span>])

    <span class="hljs-comment">//公用依赖库</span>
    implementation <span class="hljs-keyword">project</span>(<span class="hljs-string">':x_module_common'</span>)
    implementation <span class="hljs-keyword">project</span>(<span class="hljs-string">':m_module_main'</span>)
    <span class="hljs-comment">//黄油刀</span>
    annotationProcessor rootProject.ext.<span class="hljs-keyword">dependencies</span>[<span class="hljs-string">"butterknife_compiler"</span>]
    <span class="hljs-comment">//Arouter路由</span>
    annotationProcessor rootProject.ext.<span class="hljs-keyword">dependencies</span>[<span class="hljs-string">"arouter_compiler"</span>]
}
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，组件化架构的搭建就算完成了。</p>
<p>可还有几个问题，是组件化开发中必须要关注的，也是项目做组件化改造时可能会遭遇的难点，我们一起来看看吧。</p>
<h1 data-id="heading-13">组件化必须要关注的几个问题</h1>
<h2 data-id="heading-14">Application</h2>
<p>在 common 组件中有 BaseAppliaction，提供全局唯一的 context，上层业务组件在组件化模式下，均需继承于 BaseAppliaction。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
 * 基础 Application，所有需要模块化开发的 module 都需要继承自此 BaseApplication。
 */</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BaseApplication</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Application</span> </span>{

    <span class="hljs-comment">//全局唯一的context</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> BaseApplication application;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">attachBaseContext</span><span class="hljs-params">(Context base)</span> </span>{
        <span class="hljs-keyword">super</span>.attachBaseContext(base);
        application = <span class="hljs-keyword">this</span>;
        <span class="hljs-comment">//MultiDexf分包初始化，必须最先初始化</span>
        MultiDex.install(<span class="hljs-keyword">this</span>);
    }

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onCreate</span><span class="hljs-params">()</span> </span>{
        <span class="hljs-keyword">super</span>.onCreate();
        initARouter();
    }

    <span class="hljs-comment">/**
     * 初始化路由
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">initARouter</span><span class="hljs-params">()</span> </span>{
        <span class="hljs-keyword">if</span> (BuildConfig.DEBUG) {
            ARouter.openLog();  <span class="hljs-comment">// 打印日志</span>
            ARouter.openDebug(); <span class="hljs-comment">// 开启调试模式(如果在InstantRun模式下运行，必须开启调试模式！线上版本需要关闭,否则有安全风险)</span>
        }
        ARouter.init(application);<span class="hljs-comment">// 尽可能早，推荐在Application中初始化</span>
    }

    <span class="hljs-comment">/**
     * 获取全局唯一上下文
     *
     * <span class="hljs-doctag">@return</span> BaseApplication
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> BaseApplication <span class="hljs-title">getApplication</span><span class="hljs-params">()</span> </span>{
        <span class="hljs-keyword">return</span> application;
    }
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">applicationId 管理</h2>
<p>可为不同组件设置不同的 applicationId，也可缺省，在Android Studio中，默认的 applicationId 与包名一致。</p>
<p>组件的 applicationId 在其 build.gradle 文件的 defaultConfig 中进行配置：</p>
<pre><code class="hljs language-gradle copyable" lang="gradle"><span class="hljs-keyword">if</span> (<span class="hljs-keyword">Boolean</span>.valueOf(rootProject.ext.isModule_North)) {
    <span class="hljs-comment">//组件模式下设置applicationId</span>
    applicationId <span class="hljs-string">"com.niujiaojian.amd.north"</span>
}
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">manifest.xml 管理</h2>
<p>组件在 library 模式和 application 模式下，需要配置不同的 manifest.xml 文件，因为在 application 模式下，程序入口 Activity 和自定义的 Application 是不可或缺的。</p>
<p>在组件的 build.gradle文件 的 android 中进行 manifest 的管理：</p>
<pre><code class="hljs language-gradle copyable" lang="gradle"><span class="hljs-comment">/*
    * java插件引入了一个概念叫做SourceSets，通过修改SourceSets中的属性，
    * 可以指定哪些源文件（或文件夹下的源文件）要被编译，
    * 哪些源文件要被排除。
    * */</span>
    <span class="hljs-keyword">sourceSets</span> {
        main {
            <span class="hljs-keyword">if</span> (<span class="hljs-keyword">Boolean</span>.valueOf(rootProject.ext.isModule_North)) {<span class="hljs-comment">//apk</span>
                manifest.srcFile <span class="hljs-string">'src/main/manifest/AndroidManifest.xml'</span>
            } <span class="hljs-keyword">else</span> {
                manifest.srcFile <span class="hljs-string">'src/main/AndroidManifest.xml'</span>
                java {
                    <span class="hljs-comment">//library模式下，排除java/debug文件夹下的所有文件</span>
                    <span class="hljs-keyword">exclude</span> <span class="hljs-string">'*module'</span>
                }
            }
        }
    }
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">资源名冲突问题</h2>
<p>资源名冲突问题，相信大家多多少少都遇到过，以前最常见的就是第三方 sdk 导致的资源名冲突了。</p>
<p>这个问题没有特别好的解决办法，只能通过设置资源名前缀 <code>resourcePrefix</code> 以及约束自己开发习惯进行解决。</p>
<p>资源名前缀 <code>resourcePrefix</code> ，是在 Project 的 build.gradle 中进行设置的：</p>
<pre><code class="hljs language-gradle copyable" lang="gradle"><span class="hljs-comment">/**
 * 限定所有子类xml中的资源文件的前缀
 * 注意：图片资源，限定失效，需要手动添加前缀
 * */</span>
<span class="hljs-keyword">subprojects</span> {
    afterEvaluate {
        android {
            resourcePrefix <span class="hljs-string">"${project.name}_"</span>
        }
    }
}
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样设置完之后，string、style、color、dimens 等中资源名，必须以设置的字符串为前缀，而 layout、drawable 文件夹下的 shape 的 xml 文件的命名，必须以设置的字符串为前缀，否则会报错提示。</p>
<p>另外，资源前缀的设置对图片的命名无法限定，建议大家约束自己的开发习惯，自觉加上前缀。</p>
<p><strong>建议：将 color、shape、style 这些放在基础库组件中去，这些资源不会太多，且复用性极高，所有业务组件又都会依赖基础库组件。</strong></p>
<h2 data-id="heading-18">Butterknife R2 问题</h2>
<p>Butterknife 存在的问题是控件 id 找不到，只要将 R 替换为 R2 即可解决问题。</p>
<p>需要注意的是，在如下代码示例外的位置，不要这样做，保持使用 R 即可，如 <code>setContentView(R.layout.b_module_north_activity_splash)</code></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SplashActivity</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">BaseActivity</span> </span>{

    <span class="hljs-meta">@BindView(R2.id.btn_toMain)</span>
    Button btnToMain;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onCreate</span><span class="hljs-params">(<span class="hljs-meta">@Nullable</span> Bundle savedInstanceState)</span> </span>{
        <span class="hljs-keyword">super</span>.onCreate(savedInstanceState);
        setContentView(R.layout.b_module_north_activity_splash);
        ButterKnife.bind(<span class="hljs-keyword">this</span>);
    }

    ……

    <span class="hljs-meta">@OnClick(R2.id.btn_toMain)</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onViewClicked</span><span class="hljs-params">()</span> </span>{
    }
}
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外要注意的是，每一个使用 Butterknife 的组件，在其 build.gradle 的 dependencies 都要配置注解处理器处理其 compiler 库：</p>
<pre><code class="hljs language-gradle copyable" lang="gradle">apply plugin: <span class="hljs-string">'com.jakewharton.butterknife'</span>

……

<span class="hljs-keyword">dependencies</span> {

    ……
    
    annotationProcessor rootProject.ext.<span class="hljs-keyword">dependencies</span>[<span class="hljs-string">"butterknife_compiler"</span>]
}
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">组件间跳转</h2>
<p>由于业务组件间不存在依赖关系，不可以通过 Intent 进行显式跳转。</p>
<p>若需跳转，是要借助于路由的，我使用的是阿里的开源框架 <code>ARouter</code>。</p>
<p>注：我在案例中只使用了 ARouter 的基础的页面跳转功能，更复杂的诸如携带参数跳转、声明拦截器等功能的使用方法，大家可到 Github 上查看其使用文档。</p>
<p>在每一个需要用到 ARouter 的组件的 build.gradle 文件中对其进行配置：</p>
<pre><code class="hljs language-gradle copyable" lang="gradle">android {
   ...
       defaultConfig {
         ...
        <span class="hljs-comment">//Arouter路由配置</span>
        javaCompileOptions {
            annotationProcessorOptions {
                arguments = [AROUTER_MODULE_NAME: <span class="hljs-keyword">project</span>.getName()]
                includeCompileClasspath = <span class="hljs-keyword">true</span>
            }
        }
    }
}
<span class="hljs-keyword">dependencies</span>{
     ...
    <span class="hljs-comment">//Arouter路由</span>
    annotationProcessor rootProject.ext.<span class="hljs-keyword">dependencies</span>[<span class="hljs-string">"arouter_compiler"</span>]
}
<span class="copy-code-btn">复制代码</span></code></pre>
<p>跳转目标页面配置：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@Route(path = "/main/MainActivity")</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MainActivity</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">BaseActivity</span> </span>{
   ……
}
<span class="copy-code-btn">复制代码</span></code></pre>
<p>跳转来源页面的跳转代码：</p>
<pre><code class="hljs language-java copyable" lang="java">...
   ARouter.getInstance()
          .build(<span class="hljs-string">"/main/MainActivity"</span>)
          .navigation();
...
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-20">后记</h1>
<p>组件化优势多多，用起来爽的不要不要的。</p>
<p>其中快感来的最快的，当属大大提升了编译速度了。</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23936d5a840343ddb1cdfe5799da155e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            