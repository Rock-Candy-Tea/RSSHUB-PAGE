
---
title: '超简单学会使用 C++ 单元测试框架，再也不怕面试官刁难了'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79801d77d1804b39b0f87e9bfbdbaff3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 17:04:03 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79801d77d1804b39b0f87e9bfbdbaff3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第31天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h4 data-id="heading-0">导读</h4>
<p>  C++ 开发时我们常有一个非常期望的愿景，那就是引用第三方库和框架时希望尽可能的简单，不然各种平台、各种编译问题可以让人焦头烂额。而<code>Catch2</code>就是一个只有头文件的单元测试框架。放心，这个单元测试框架完全能够支撑你的项目，且它的协议是 Boost Software License，完全可以商用。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79801d77d1804b39b0f87e9bfbdbaff3~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
由于<code>Catch2</code>只有一个头文件，因此你只需要下载这个头文件下来，添加到你的项目中就可以了。</p>
<p>github 下载地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fcatchorg%2FCatch2%2Freleases%2Fdownload%2Fv2.12.2%2Fcatch.hpp" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/catchorg/Catch2/releases/download/v2.12.2/catch.hpp" ref="nofollow noopener noreferrer">catchorg/Catch2</a></p>
<p>不能翻墙的提供csdn下载：
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdownload.csdn.net%2Fdownload%2Fu012534831%2F12548946" target="_blank" rel="nofollow noopener noreferrer" title="https://download.csdn.net/download/u012534831/12548946" ref="nofollow noopener noreferrer">catchorg/Catch2</a></p>
<h4 data-id="heading-1">使用案例</h4>
<pre><code class="copyable">#define CATCH_CONFIG_MAIN

#include <catch2/catch.hpp>

int Factorial( int number ) &#123;
   return number <= 1 ? number : Factorial( number - 1 ) * number;  // fail
// return number <= 1 ? 1      : Factorial( number - 1 ) * number;  // pass
&#125;

TEST_CASE( "Factorial of 0 is 1 (fail)", "[single-file]" ) &#123;
    REQUIRE( Factorial(0) == 1 );
&#125;

TEST_CASE( "Factorials of 1 and higher are computed (pass)", "[single-file]" ) &#123;
    REQUIRE( Factorial(1) == 1 );
    REQUIRE( Factorial(2) == 2 );
    REQUIRE( Factorial(3) == 6 );
    REQUIRE( Factorial(10) == 3628800 );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个例子是官方案例，演示了计算阶乘的算法。</p>
<h5 data-id="heading-2">常规测试</h5>
<p><code>#define CATCH_CONFIG_MAIN</code> 这个宏定义了catch2 的 main 函数。下面的代码是从 catch2 里面摘抄的，可以看到 main 函数定义。</p>
<pre><code class="copyable">#ifdef CATCH_CONFIG_MAIN
// start catch_default_main.hpp

#ifndef __OBJC__

#if defined(CATCH_CONFIG_WCHAR) && defined(WIN32) && defined(_UNICODE) && !defined(DO_NOT_USE_WMAIN)
// Standard C/C++ Win32 Unicode wmain entry point
extern "C" int wmain (int argc, wchar_t * argv[], wchar_t * []) &#123;
#else
// Standard C/C++ main entry point
int main (int argc, char * argv[]) &#123;
#endif

    return Catch::Session().run( argc, argv );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>意味着你不需要自己写 main 函数。</p>
<p>但是如果你需要写自己的 main 函数，catch2 也支持，像下面这样：</p>
<pre><code class="copyable">#define CATCH_CONFIG_RUNNER
#include "catch.hpp"

int main( int argc, char* argv[] ) &#123;
  // global setup...

  int result = Catch::Session().run( argc, argv );

  // global clean-up...
  return result;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大多数情况下我们都是有 main 函数的，当你运行项目时<code>Catch::Session().run( argc, argv );</code>这一句就启动了你的单元测试。如下：</p>
<pre><code class="copyable">#define CATCH_CONFIG_MAIN
#include "catch.hpp"

int main(int argc, char* argv[]) &#123;
    // global setup...
    int result = Catch::Session().run(argc, argv);
    // global clean-up...
    return result;
&#125;

int Factorial(int number) &#123;
    return number <= 1 ? number : Factorial(number - 1) * number;  // fail
&#125;

TEST_CASE("Factorial of 0 is 1 (fail)", "[single-file]") &#123;
    REQUIRE(Factorial(0) == 1);
&#125;

TEST_CASE("Factorials of 1 and higher are computed (pass)", "[single-file]") &#123;
    REQUIRE(Factorial(1) == 1);
    REQUIRE(Factorial(2) == 2);
    REQUIRE(Factorial(3) == 6);
    REQUIRE(Factorial(10) == 3628800);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>回到最上面的测试案例，我们的 test-case 是有命名的，其实 test-case 也是可以没有名字的，因为要测试的函数多了，你最终总是要命名。不命名的test-case 如下：</p>
<pre><code class="copyable">TEST_CASE() &#123;
    REQUIRE(Factorial(1) == 1);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单吧。 剩下的就是去补充你的单元测试文件了，直到你写完了自己需要的 test-case。</p>
<p>看下单元测试运行结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f519125f84d946c486d589ee55b37572~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
16 行测试没有通过，和代码相符。</p>
<h5 data-id="heading-3">BDD 风格测试</h5>
<p>BDD 简介：</p>
<blockquote>
<p>Behavior Driven Development，行为驱动开发是一种敏捷软件开发的技术，它鼓励软件项目中的开发者、QA和非技术人员或商业参与者之间的协作，BDD 提倡的是通过将测试语句转换为类似自然语言的描述，开发人员可以使用更符合大众语言的习惯来书写测试，当别人接手/交付，或者自己修改的时候，都简单易明白，顺利很多。一个典型的 BDD 测试用例包括完整的三段式上下文，测试大多可以翻译为Given...When...Then的格式，读起来轻松惬意。</p>
</blockquote>
<p>catch2 也支持像 BDD（行为驱动开发）风格的单元测试。</p>
<p>因为我们目前的项目是采用敏捷开发的模式，同时基于 BDD 开发，需求人员在写需求是是按照 GIVEN WHEN THEN 的方式，截张图看下（真实图片，理解打码）：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55cac26ac5c34d32ad9da56af2dd003f~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以我们的单元测试需要跟随 BDD 流程来。这样可以保证所有参与者的理解是一致的，包括代码也是跟随需求描述是一致的。</p>
<p>案例：</p>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-meta">#<span class="hljs-meta-keyword">define</span> CATCH_CONFIG_MAIN</span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"catch.hpp"</span></span>

<span class="hljs-built_in">SCENARIO</span>( <span class="hljs-string">"vectors can be sized and resized"</span>, <span class="hljs-string">"[vector]"</span> ) &#123;

    <span class="hljs-built_in">GIVEN</span>( <span class="hljs-string">"A vector with some items"</span> ) &#123;
        <span class="hljs-function">std::vector<<span class="hljs-keyword">int</span>> <span class="hljs-title">v</span><span class="hljs-params">( <span class="hljs-number">5</span> )</span></span>;

        <span class="hljs-built_in">REQUIRE</span>( v.<span class="hljs-built_in">size</span>() == <span class="hljs-number">5</span> );
        <span class="hljs-built_in">REQUIRE</span>( v.<span class="hljs-built_in">capacity</span>() >= <span class="hljs-number">5</span> );

        <span class="hljs-built_in">WHEN</span>( <span class="hljs-string">"the size is increased"</span> ) &#123;
            v.<span class="hljs-built_in">resize</span>( <span class="hljs-number">10</span> );

            <span class="hljs-built_in">THEN</span>( <span class="hljs-string">"the size and capacity change"</span> ) &#123;
                <span class="hljs-built_in">REQUIRE</span>( v.<span class="hljs-built_in">size</span>() == <span class="hljs-number">10</span> );
                <span class="hljs-built_in">REQUIRE</span>( v.<span class="hljs-built_in">capacity</span>() >= <span class="hljs-number">10</span> );
            &#125;
        &#125;
        <span class="hljs-built_in">WHEN</span>( <span class="hljs-string">"the size is reduced"</span> ) &#123;
            v.<span class="hljs-built_in">resize</span>( <span class="hljs-number">0</span> );

            <span class="hljs-built_in">THEN</span>( <span class="hljs-string">"the size changes but not capacity"</span> ) &#123;
                <span class="hljs-built_in">REQUIRE</span>( v.<span class="hljs-built_in">size</span>() == <span class="hljs-number">0</span> );
                <span class="hljs-built_in">REQUIRE</span>( v.<span class="hljs-built_in">capacity</span>() >= <span class="hljs-number">5</span> );
            &#125;
        &#125;
        <span class="hljs-built_in">WHEN</span>( <span class="hljs-string">"more capacity is reserved"</span> ) &#123;
            v.<span class="hljs-built_in">reserve</span>( <span class="hljs-number">10</span> );

            <span class="hljs-built_in">THEN</span>( <span class="hljs-string">"the capacity changes but not the size"</span> ) &#123;
                <span class="hljs-built_in">REQUIRE</span>( v.<span class="hljs-built_in">size</span>() == <span class="hljs-number">5</span> );
                <span class="hljs-built_in">REQUIRE</span>( v.<span class="hljs-built_in">capacity</span>() >= <span class="hljs-number">10</span> );
            &#125;
        &#125;
        <span class="hljs-built_in">WHEN</span>( <span class="hljs-string">"less capacity is reserved"</span> ) &#123;
            v.<span class="hljs-built_in">reserve</span>( <span class="hljs-number">0</span> );

            <span class="hljs-built_in">THEN</span>( <span class="hljs-string">"neither size nor capacity are changed"</span> ) &#123;
                <span class="hljs-built_in">REQUIRE</span>( v.<span class="hljs-built_in">size</span>() == <span class="hljs-number">4</span> );
                <span class="hljs-built_in">REQUIRE</span>( v.<span class="hljs-built_in">capacity</span>() >= <span class="hljs-number">5</span> );
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>真实项目不便演示，上面的代码也是官方给的 BDD 风格的单元测试。我在 42 行故意写错，看下运行结果：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e0004726fb245f484b2bd9322a2d521~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>结果提示 42 行测试不通过。</p>
<h4 data-id="heading-4">结语</h4>
<p>基于上面的小案例，我相信你已经迅速掌握了 catch2 的用法，也可以给自己的代码写单元测试了。只有当你真正的实践过，你才能知道这里面的门道。</p>
<p>如有帮助，请多多点赞支持。</p></div>  
</div>
            