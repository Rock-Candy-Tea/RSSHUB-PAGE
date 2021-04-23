
---
title: '前端抢饭碗系列之Vue项目中如何做单元测试'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2331ac2c34b247ae92f795373b887b31~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 22 Apr 2021 04:43:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2331ac2c34b247ae92f795373b887b31~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>　　关于单元测试，最常见的问题应该就是“前端单元测试有必要吗？”，通过这篇文章，你将会了解单元测试的必要性，以及在Vue项目中如何能够全面可靠的测试我们写的组件。</p>
<blockquote>
<p>本文首发于公众号<code>【前端壹读】</code>，更多精彩内容敬请关注公众号最新消息。</p>
</blockquote>
<h1 data-id="heading-0">单元测试的必要性</h1>
<p>　　一般在我们的印象里，单元测试都是测试工程师的工作，前端负责代码就行了；百度搜索Vue单元测试，联想词出来的都是<code>“单元测试有必要吗？”</code> <code>“单元测试是做什么的？”</code>虽然我们平时项目中一般都会有测试工程师来对我们的页面进行测试“兜底”，但是根据我的观察，一般测试工程师并不会覆盖所有的业务逻辑，而且有一些深层次的代码逻辑测试工程师在不了解代码的情况下也根本无法进行触发。因此在这种情况下，我们并不能够完全的依赖测试工程师对我们项目测试，前端项目的单元测试就显得非常的有必要。</p>
<p>　　而且单元测试也能够帮助我们节省很大一部分自我测试的成本，假如我们有一个订单展示的组件，根据订单状态的不同以及其他的一些业务逻辑来进行对应文案的展示；我们想在页面上查看文案展示是否正确，这时就需要繁琐的填写下单信息后才能查看；如果第二天又又加入了一些新的逻辑判断（你前一天下的单早就过期啦），这时你有三个选择，第一种选择就是再次繁琐地填写订单并支付完（又给老板提供资金支持了），第二种选择就是死皮赖脸的求着后端同事给你更改订单状态（后端同事给你一个白眼自己体会），第三种选择就是代理接口或者使用mock数据（你需要编译整个项目运行进行测试）。</p>
<p>　　这时，单元测试就提供了第四种成本更低的测试方式，写一个测试用例，来对我们的组件进行测试，判断文案是否按照我们预想的方式进行展示；这种方式既不需要依赖后端的协助，也不需要对项目进行任何改动，可谓是省时又省力。</p>
<h1 data-id="heading-1">测试框架和断言库</h1>
<p>　　说到单元测试，我们首先来介绍一下流行的测试框架，主要是mocha和jest。先简单介绍下mocha，翻译成中文就是<code>摩卡</code>（人家是一种咖啡！不是抹茶啊），名字的由来估猜是因为开发人员喜欢喝摩卡咖啡，就像Java名字也是从咖啡由来一样，mocha的logo也是一杯摩卡咖啡：</p>
<p><img alt="mocha logo" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2331ac2c34b247ae92f795373b887b31~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>　　和jest相比，两者主要的不同就是jest内置了集成度比较高的断言库<code>expect.js</code>，而mocha需要搭配额外的断言库，一般会选择比较流行的<code>chai</code>作为断言库，这里一直提到断言库，那么什么是断言库呢？我们首先来看下mocha是怎么来测试代码的，首先我们写了一个<code>addNum函数</code>，但是不确定是否返回我们想要的结果，因此需要对这个函数进行测试：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//src/index.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addNum</span>(<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> a + b;
&#125;
<span class="hljs-built_in">module</span>.exports = addNum;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　然后就可以写我们的测试文件了，所有的测试文件都放在test目录下，一般会将测试文件和所要测试的源码文件同名，方便进行对应，运行mocha时会自动对test目录下所有js文件进行测试：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//test/index.test.js</span>
<span class="hljs-keyword">var</span> addNum = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../src/index"</span>);
describe(<span class="hljs-string">"测试addNum函数"</span>, <span class="hljs-function">() =></span> &#123;
  it(<span class="hljs-string">"两数相加结果为两个数字的和"</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (addNum(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>) !== <span class="hljs-number">3</span>) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"两数相加结果不为两个数字的和"</span>);
    &#125;
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　上面这段代码就是测试脚本的语法，一个测试脚本会包括一个或多个<code>describe</code>块，每个<code>describe</code>又包括一个或多个<code>it</code>块；这里<code>describe</code>称为<code>测试套件</code>（test suite），表示一组相关的测试，它包含了两个参数，第一个参数是这个<code>测试套件</code>的名称，第二个参数是实际执行的函数。</p>
<p>　　而<code>it</code>称为<code>测试用例</code>，表示一个单独的测试，是测试的最小单位，它也包含两个参数，第一个参数是<code>测试用例</code>的名称，第二个参数是实际执行的函数。</p>
<p>　　<code>it</code>块中就是我们需要测试的代码，如果运行结果不是我们所预期的就抛出异常；上面的测试用例写好后，我们就可以运行测试了，</p>
<p><img alt="运行mocha" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24806dd5abe347a8b0f119e8e2ab3afb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>　　运行结果通过了，是我们想要的结果，说明我们的函数是正确的；但是每次都通过抛出异常来判断，多少有点繁琐了，断言库就出现了；断言的目的就是将测试代码运行后和我们的预期做比较，如果和预期一致，就表明代码没有问题；如果和预期不一致，就是代码有问题了；每一个测试用例最后都会有一个断言进行判断，如果没有断言，测试就没有意义了。</p>
<p>　　上面也说了mocha一般搭配chai断言库，而chai有好几种断言风格，比较常见的有should和expect两种风格，我们分别看下这两种断言：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> chai = <span class="hljs-built_in">require</span>(<span class="hljs-string">"chai"</span>),
  expect = chai.expect,
  should = chai.should();

describe(<span class="hljs-string">"测试addNum函数"</span>, <span class="hljs-function">() =></span> &#123;
  it(<span class="hljs-string">"1+2"</span>, <span class="hljs-function">() =></span> &#123;
    addNum(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>).should.equal(<span class="hljs-number">3</span>);
  &#125;);
  it(<span class="hljs-string">"2+3"</span>, <span class="hljs-function">() =></span> &#123;
    expect(addNum(<span class="hljs-number">2</span>, <span class="hljs-number">3</span>)).to.be.equal(<span class="hljs-number">5</span>);
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　这里should是后置的，在断言变量之后，而expect是前置的，作为断言的开始，两种风格纯粹看个人喜好；我们发现这里expect是从chai中获取的一个函数，而should则是直接调用，这是因为should实际上是给所有的对象都扩充了一个 <code>getter</code> 属性<code>should</code>，因此我们才能够在变量上使用<code>.should</code>方式来进行断言。</p>
<p>　　和chai的多种断言风格不同，jest内置了断言库expect，它的语法又有些不同：</p>
<pre><code class="hljs language-js copyable" lang="js">describe(<span class="hljs-string">"测试addNum函数"</span>, <span class="hljs-function">() =></span> &#123;
  it(<span class="hljs-string">"1+2"</span>, <span class="hljs-function">() =></span> &#123;
    expect(addNum(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>)).toBe(<span class="hljs-number">3</span>);
  &#125;);
  it(<span class="hljs-string">"2+3"</span>, <span class="hljs-function">() =></span> &#123;
    expect(addNum(<span class="hljs-number">2</span>, <span class="hljs-number">3</span>)).toBe(<span class="hljs-number">5</span>);
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　jest中的expect直接通过<code>toBe</code>的语法，在形式上相较于mocha更为简洁；这两个框架在使用上极其相似，比如在异步代码上都支持<code>done</code>回调和<code>async/await</code>关键字，在断言语法和其他用法有些差别；两者也有相同的钩子机制，连名字都相同beforeEach和afterEach；在vue cli脚手架创建项目时，也可以在两个框架中进行选择其一，我们这里主要以jest进行测试。</p>
<h1 data-id="heading-2">Jest</h1>
<p>　　Jest是Facebook出品的一个测试框架，相较于其他测试框架，最大的特点就是内置了常用的测试工具，比如自带断言、测试覆盖率工具，实现了开箱即用，这也和它官方的slogan相符。</p>
<p><img alt="jest logo" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e95eafbf2c04eb2bf11e19630ef9784~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>Jest 是一个令人愉快的 JavaScript 测试框架，专注于<code>简洁明快</code>。</p>
</blockquote>
<p>　　Jest几乎是零配置的，它会自动识别一些常用的测试文件，比如<code>*.spec.js</code>和 <code>*.test.js</code>后缀的测试脚本，所有的测试脚本都放在<code>tests</code>或<code>__tests__</code>目录下；我们可以在全局安装jest或者局部安装，然后在packages.json中指定测试脚本：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"test"</span>: <span class="hljs-string">"jest"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　当我们运行<code>npm run test</code>时会自动运行测试目录下所有测试文件，完成测试；我们在jest官网可能还会看到通过test函数写的测试用例：</p>
<pre><code class="hljs language-js copyable" lang="js">test(<span class="hljs-string">"1+2"</span>, <span class="hljs-function">() =></span> &#123;
  expect(addNum(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>)).toBe(<span class="hljs-number">3</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　和it函数相同，test函数也代表一个测试用例，mocha只支持<code>it</code>，而jest支持<code>it</code>和<code>test</code>，这里为了和jest官网保持统一，下面代码统一使用<code>test</code>函数。</p>
<h2 data-id="heading-3">匹配器</h2>
<p>　　我们经常需要对测试代码返回的值进行匹配测试，上面代码中的<code>toBe</code>是最简单的一个匹配器，用来测试两个数值是否相同。</p>
<pre><code class="hljs language-js copyable" lang="js">test(<span class="hljs-string">"test tobe"</span>, <span class="hljs-function">() =></span> &#123;
  expect(<span class="hljs-number">2</span> + <span class="hljs-number">2</span>).toBe(<span class="hljs-number">4</span>);
  expect(<span class="hljs-literal">true</span>).toBe(<span class="hljs-literal">true</span>);
  <span class="hljs-keyword">const</span> val = <span class="hljs-string">"team"</span>;
  expect(val).toBe(<span class="hljs-string">"team"</span>);
  expect(<span class="hljs-literal">undefined</span>).toBe(<span class="hljs-literal">undefined</span>);
  expect(<span class="hljs-literal">null</span>).toBe(<span class="hljs-literal">null</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　toBe函数内部使用了<code>Object.is</code>来进行精确匹配，它的特性类似于<code>===</code>；对于普通类型的数值可以进行比较，但是对于对象数组等复杂类型，就需要用到<code>toEqual</code>来比较了：</p>
<pre><code class="hljs language-js copyable" lang="js">    test(<span class="hljs-string">"expect a object"</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">var</span> obj = &#123;
        <span class="hljs-attr">a</span>: <span class="hljs-string">"1"</span>,
    &#125;;
    obj.b = <span class="hljs-string">"2"</span>;
    expect(obj).toEqual(&#123; <span class="hljs-attr">a</span>: <span class="hljs-string">"1"</span>, <span class="hljs-attr">b</span>: <span class="hljs-string">"2"</span> &#125;);
&#125;);

test(<span class="hljs-string">"expect array"</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">var</span> list = [];
    list.push(<span class="hljs-number">1</span>);
    list.push(<span class="hljs-number">2</span>);
    expect(list).toEqual([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>]);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　我们有时候还需要对undefined、null等类型或者对条件语句中的表达式的真假进行精确匹配，Jest也有五个函数帮助我们：</p>
<ul>
<li>toBeNull：只匹配null</li>
<li>toBeUndefined：只匹配undefined</li>
<li>toBeDefined：与toBeUndefined相反，等价于.not.toBeUndefined</li>
<li>toBeTruthy：匹配任何 if 语句为真</li>
<li>toBeFalsy：匹配任何 if 语句为假</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">test(<span class="hljs-string">"null"</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> n = <span class="hljs-literal">null</span>;
    expect(n).toBeNull();
    expect(n).not.toBeUndefined();
    expect(n).toBeDefined();
    expect(n).not.toBeTruthy();
    expect(n).toBeFalsy();
&#125;);
test(<span class="hljs-string">"0"</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> z = <span class="hljs-number">0</span>;
    expect(z).not.toBeNull();
    expect(z).not.toBeUndefined();
    expect(z).toBeDefined();
    expect(z).not.toBeTruthy();
    expect(z).toBeFalsy();
&#125;);
test(<span class="hljs-string">"undefined"</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> a = <span class="hljs-literal">undefined</span>;
    expect(a).not.toBeNull();
    expect(a).toBeUndefined();
    expect(a).not.toBeDefined();
    expect(a).not.toBeTruthy();
    expect(a).toBeFalsy();
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　toBeTruthy和toBeFalsy用来判断在if语句中的表达式是否成立，等价于`if(n)<code>和</code>if(!n)``的判断。</p>
<p>　　对于数值类型的数据，我们有时候也可以通过大于或小于来进行判断：</p>
<pre><code class="hljs language-js copyable" lang="js">test(<span class="hljs-string">"number"</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> val = <span class="hljs-number">2</span> + <span class="hljs-number">2</span>;
    <span class="hljs-comment">// 大于</span>
    expect(val).toBeGreaterThan(<span class="hljs-number">3</span>);
    <span class="hljs-comment">// 大于等于</span>
    expect(val).toBeGreaterThanOrEqual(<span class="hljs-number">3.5</span>);
    <span class="hljs-comment">// 小于</span>
    expect(val).toBeLessThan(<span class="hljs-number">5</span>);
    <span class="hljs-comment">// 小于等于</span>
    expect(val).toBeLessThanOrEqual(<span class="hljs-number">4.5</span>);
    <span class="hljs-comment">// 完全判断</span>
    expect(val).toBe(<span class="hljs-number">4</span>);
    expect(val).toEqual(<span class="hljs-number">4</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　浮点类型的数据虽然我们也可以用toBe和toEqual来进行比较，但是如果遇到有些特殊的浮点数据计算，比如0.1+0.2就会出现问题，我们可以通过<code>toBeCloseTo</code>来判断：</p>
<pre><code class="hljs language-js copyable" lang="js">test(<span class="hljs-string">"float"</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// expect(0.1 + 0.2).toBe(0.3); 报错</span>
    expect(<span class="hljs-number">0.1</span> + <span class="hljs-number">0.2</span>).toBeCloseTo(<span class="hljs-number">0.3</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　对于数组、set或者字符串等可迭代类型的数据，可以通过<code>toContain</code>来判断内部是否有某一项：</p>
<pre><code class="hljs language-js copyable" lang="js">test(<span class="hljs-string">"expect iterable"</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> shoppingList = [
      <span class="hljs-string">"diapers"</span>,
      <span class="hljs-string">"kleenex"</span>,
      <span class="hljs-string">"trash bags"</span>,
      <span class="hljs-string">"paper towels"</span>,
      <span class="hljs-string">"milk"</span>,
    ];
    expect(shoppingList).toContain(<span class="hljs-string">"milk"</span>);
    expect(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(shoppingList)).toContain(<span class="hljs-string">"diapers"</span>);
    expect(<span class="hljs-string">"abcdef"</span>).toContain(<span class="hljs-string">"cde"</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">异步代码</h2>
<p>　　我们项目中经常也会涉及到异步代码，比如setTimeout、接口请求等都会涉及到异步，那么这些异步代码怎么来进行测试呢？假设我们有一个异步获取数据的函数<code>fetchData</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fetchData</span>(<span class="hljs-params">cb</span>) </span>&#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    cb(<span class="hljs-string">"res data"</span>);
  &#125;, <span class="hljs-number">2000</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　在2秒后通过回调函数返回了一个字符串，我们可以在测试用例的函数中使用一个<code>done</code>的参数，Jest会等done回调后再完成测试：</p>
<pre><code class="hljs language-js copyable" lang="js">test(<span class="hljs-string">"callback"</span>, <span class="hljs-function">(<span class="hljs-params">done</span>) =></span> &#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cb</span>(<span class="hljs-params">data</span>) </span>&#123;
    <span class="hljs-keyword">try</span> &#123;
      expect(data).toBe(<span class="hljs-string">"res data"</span>);
      done();
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
      done();
    &#125;
  &#125;
  fetchData(cb);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　我们将一个回调函数传入fetchData，在回调函数中对返回的数据进行断言，在断言结束后需要调用done；如果最后没有调用done，那么Jest不知道什么时候结束，就会报错；在我们日常代码中，都会通过promise来获取数据，将我们的<code>fetchData</code>进行一下改写：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fetchData</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      resolve(<span class="hljs-string">"promise data"</span>);
    &#125;, <span class="hljs-number">2000</span>);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　Jest支持在测试用例中直接返回一个promise，我们可以在then中进行断言：</p>
<pre><code class="hljs language-js copyable" lang="js">test(<span class="hljs-string">"promise callback"</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> fetchData().then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
    expect(res).toBe(<span class="hljs-string">"promise data"</span>);
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　除了直接将fetchData返回，我们也可以在断言中使用<code>.resolves/.rejects </code>匹配符，Jest也会等待promise结束：</p>
<pre><code class="hljs language-js copyable" lang="js">test(<span class="hljs-string">"promise callback"</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> expect(fetchData()).resolves.toBe(<span class="hljs-string">"promise data"</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　除此之外，Jest还支持<code>async/await</code>，不过我们需要在test的匿名函数加上<code>async修饰符</code>表示：</p>
<pre><code class="hljs language-js copyable" lang="js">test(<span class="hljs-string">"async/await callback"</span>, <span class="hljs-keyword">async</span> () => &#123;
  <span class="hljs-keyword">const</span> data = <span class="hljs-keyword">await</span> fetchData();
  expect(data).toBe(<span class="hljs-string">"promise data"</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">全局挂载与卸载</h2>
<p>　　全局挂载和卸载有点类似Vue-Router的全局守卫，在每个导航触发前和触发后做一些操作；在Jest中也有，比如我们需要在每个测试用例前初始化一些数据，或者在每个测试用例之后清除数据，就可以使用<code>beforeEach</code>和<code>afterEach</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> cityList = []
beforeEach(<span class="hljs-function">() =></span> &#123;
  initializeCityDatabase();
&#125;);

afterEach(<span class="hljs-function">() =></span> &#123;
  clearCityDatabase();
&#125;);

test(<span class="hljs-string">"city data has suzhou"</span>, <span class="hljs-function">() =></span>  &#123;
  expect(cityList).toContain(<span class="hljs-string">"suzhou"</span>)
&#125;)

test(<span class="hljs-string">"city data has shanghai"</span>, <span class="hljs-function">() =></span>  &#123;
  expect(cityList).toContain(<span class="hljs-string">"suzhou"</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　这样，每个测试用例进行测试前都会调用init，每次结束后都会调用clear；我们有可能会在某些<code>test</code>中更改cityList的数据，但是在<code>beforeEach</code>进行初始化的操作后，每个测试用例获取的cityList数据就保证都是相同的；和上面一节异步代码一样，在<code>beforeEach</code>和<code>afterEach</code>我们也可以使用异步代码来进行初始化：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> cityList = []
beforeEach(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> initializeCityDatabase().then(<span class="hljs-function">(<span class="hljs-params">res</span>)=></span>&#123;
    cityList = res.data
  &#125;);
&#125;);
<span class="hljs-comment">//或者使用async/await</span>
beforeEach(<span class="hljs-keyword">async</span> () => &#123;
  cityList = <span class="hljs-keyword">await</span> initializeCityDatabase();
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　和<code>beforeEach</code>和<code>afterEach</code>相对应的就是<code>beforeAll</code>和<code>afterAll</code>，区别就是<code>beforeAll</code>和<code>afterAll</code>只会执行一次；<code>beforeEach</code>和<code>afterEach</code>默认会应用到每个test，但是我们可能希望只针对某些test，我们可以通过<code>describe</code>将这些test放到一起，这样就只应用到<code>describe</code>块中的test：</p>
<pre><code class="hljs language-js copyable" lang="js">beforeEach(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 应用到所有的test</span>
&#125;);
describe(<span class="hljs-string">"put test together"</span>, <span class="hljs-function">() =></span> &#123;
  beforeEach(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 只应用当前describe块中的test</span>
  &#125;);
  test(<span class="hljs-string">"test1"</span>, <span class="hljs-function">()=></span> &#123;&#125;)
  test(<span class="hljs-string">"test2"</span>, <span class="hljs-function">()=></span> &#123;&#125;)
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">模拟函数</h2>
<p>　　在项目中，一个模块的函数内常常会去调用另外一个模块的函数。在单元测试中，我们可能并不需要关心内部调用的函数的执行过程和结果，只想知道被调用模块的函数是否被正确调用，甚至会指定该函数的返回值，因此模拟函数十分有必要。</p>
<p>　　如果我们正在测试一个函数forEach，它的参数包括了一个回调函数，作用在数组上的每个元素：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">forEach</span>(<span class="hljs-params">items, callback</span>) </span>&#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>; index < items.length; index++) &#123;
    callback(items[index]);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　为了测试这个forEach，我们需要构建一个模拟函数，来检查模拟函数是否按照预期被调用了：</p>
<pre><code class="hljs language-js copyable" lang="js">test(<span class="hljs-string">"mock callback"</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> mockCallback = jest.fn(<span class="hljs-function">(<span class="hljs-params">x</span>) =></span> <span class="hljs-number">42</span> + x);
  forEach([<span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>], mockCallback);
  expect(mockCallback.mock.calls.length).toBe(<span class="hljs-number">3</span>);
  expect(mockCallback.mock.calls[<span class="hljs-number">0</span>][<span class="hljs-number">0</span>]).toBe(<span class="hljs-number">0</span>);
  expect(mockCallback.mock.calls[<span class="hljs-number">1</span>][<span class="hljs-number">0</span>]).toBe(<span class="hljs-number">1</span>);
  expect(mockCallback.mock.calls[<span class="hljs-number">2</span>][<span class="hljs-number">0</span>]).toBe(<span class="hljs-number">1</span>);
  expect(mockCallback.mock.results[<span class="hljs-number">0</span>].value).toBe(<span class="hljs-number">42</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　我们发现在mockCallback有一个特殊的<code>.mock</code>属性，它保存了模拟函数被调用的信息；我们打印出来看下：</p>
<p><img alt="mock属性" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe07be3209e6497ab9c562eb14de1ba2~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>　　它有四个属性：</p>
<ul>
<li>calls：调用参数</li>
<li>instances：this指向</li>
<li>invocationCallOrder：函数调用顺序</li>
<li>results：调用结果</li>
</ul>
<p>　　在上面属性中有一个<code>instances</code>属性，表示了函数的this指向，我们还可以通过<code>bind</code>函数来更改我们模拟函数的this：</p>
<pre><code class="hljs language-js copyable" lang="js">test(<span class="hljs-string">"mock callback"</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> mockCallback = jest.fn(<span class="hljs-function">(<span class="hljs-params">x</span>) =></span> <span class="hljs-number">42</span> + x);
    <span class="hljs-keyword">const</span> obj = &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span> &#125;;
    <span class="hljs-keyword">const</span> bindMockCallback = mockCallback.bind(obj);
    forEach([<span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>], bindMockCallback);
    expect(mockCallback.mock.instances[<span class="hljs-number">0</span>]).toEqual(obj);
    expect(mockCallback.mock.instances[<span class="hljs-number">1</span>]).toEqual(obj);
    expect(mockCallback.mock.instances[<span class="hljs-number">2</span>]).toEqual(obj);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　通过bind更改函数的this之后，我们可以用<code>instances</code>来进行检测；模拟函数可以在运行时将返回值进行注入：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> myMock = jest.fn();
<span class="hljs-comment">// undefined</span>
<span class="hljs-built_in">console</span>.log(myMock());

myMock
    .mockReturnValueOnce(<span class="hljs-number">10</span>)
    .mockReturnValueOnce(<span class="hljs-string">"x"</span>)
    .mockReturnValue(<span class="hljs-literal">true</span>);

<span class="hljs-comment">//10 x true true</span>
<span class="hljs-built_in">console</span>.log(myMock(), myMock(), myMock(), myMock());

myMock.mockReturnValueOnce(<span class="hljs-literal">null</span>);

<span class="hljs-comment">// null true true</span>
<span class="hljs-built_in">console</span>.log(myMock(), myMock(), myMock());
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　我们第一次执行myMock，由于没有注入任何返回值，然后通过<code>mockReturnValueOnce</code>和<code>mockReturnValue</code>进行返回值注入，Once只会注入一次；模拟函数在连续性函数传递返回值时使用注入非常的有用：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> filterFn = jest.fn();
filterFn.mockReturnValueOnce(<span class="hljs-literal">true</span>).mockReturnValueOnce(<span class="hljs-literal">false</span>);
<span class="hljs-keyword">const</span> result = [<span class="hljs-number">2</span>, <span class="hljs-number">3</span>].filter(<span class="hljs-function">(<span class="hljs-params">num</span>) =></span> filterFn(num));
expect(result).toEqual([<span class="hljs-number">2</span>]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　我们还可以对模拟函数的调用情况进行断言：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> mockFunc = jest.fn();

<span class="hljs-comment">// 断言函数还没有被调用</span>
expect(mockFunc).not.toHaveBeenCalled();
mockFunc(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>);
mockFunc(<span class="hljs-number">2</span>, <span class="hljs-number">3</span>);
<span class="hljs-comment">// 断言函数至少调用一次</span>
expect(mockFunc).toHaveBeenCalled();
<span class="hljs-comment">// 断言函数调用参数</span>
expect(mockFunc).toHaveBeenCalledWith(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>);
expect(mockFunc).toHaveBeenCalledWith(<span class="hljs-number">2</span>, <span class="hljs-number">3</span>);
<span class="hljs-comment">// 断言函数最后一次的调用参数</span>
expect(mockFunc).toHaveBeenLastCalledWith(<span class="hljs-number">2</span>, <span class="hljs-number">3</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　除了能对函数进行模拟，Jest还支持拦截axios返回数据，假如我们有一个获取用户的接口：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// /src/api/users</span>
<span class="hljs-keyword">const</span> axios = <span class="hljs-built_in">require</span>(<span class="hljs-string">"axios"</span>);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fetchUserData</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> axios
    .get(<span class="hljs-string">"/user.json"</span>)
    .then(<span class="hljs-function">(<span class="hljs-params">resp</span>) =></span> resp.data);
&#125;

<span class="hljs-built_in">module</span>.exports = &#123;
  fetchUserData,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　现在我们想要测试<code>fetchUserData</code>函数获取数据但是并不实际请求接口，我们可以使用<code>jest.mock</code>来模拟axios模块：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> users = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../api/users"</span>);
<span class="hljs-keyword">const</span> axios = <span class="hljs-built_in">require</span>(<span class="hljs-string">"axios"</span>);
jest.mock(<span class="hljs-string">"axios"</span>);

test(<span class="hljs-string">"should fetch users"</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> userData = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"aaa"</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">10</span>,
  &#125;;
  <span class="hljs-keyword">const</span> resp = &#123; <span class="hljs-attr">data</span>: userData &#125;;

  axios.get.mockResolvedValue(resp);

  <span class="hljs-keyword">return</span> users.fetchUserData().then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
    expect(res).toEqual(userData);
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　一旦我们对模块进行了模拟，我们可以用get函数提供一个mockResolvedValue方法，以返回我们需要测试的数据；通过模拟后，实际上axios并没有去真正发送请求去获取<code>/user.json</code>的数据。</p>
<h1 data-id="heading-7">Vue Test Utils</h1>
<p>　　Vue Test Utils是Vue.js官方的单元测试实用工具库，能够对我们编写的Vue组件进行测试。</p>
<h2 data-id="heading-8">挂载组件</h2>
<p>　　在Vue中我们通过<code>import</code>引入组件，然后在<code>components</code>进行注册后就能使用；在单元测试中，我们使用<code>mount</code>来进行挂载组件；假如我们写了一个计数器组件<code>counter.js</code>，用来展示count，并且有一个按钮操作count：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- Counter.vue --></span>
<span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"counter"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"count"</span>></span>&#123;&#123; count &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"add"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"add"</span>></span>加<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>,
    &#125;;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.count++;
    &#125;,
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　组件进行挂载后得到一个wrapper（包裹器），wrapper会暴露很多封装、遍历和查询其内部的Vue组件实例的便捷的方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; mount &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@vue/test-utils"</span>;
<span class="hljs-keyword">import</span> Counter <span class="hljs-keyword">from</span> <span class="hljs-string">"@/components/Counter"</span>;
<span class="hljs-keyword">const</span> wrapper = mount(Counter);
<span class="hljs-keyword">const</span> vm = wrapper.vm;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　我们可以通过<code>wrapper.vm</code>来访问组件的Vue实例，进而获取实例上的methods和data等；通过wrapper，我们可以对组件的渲染情况做断言：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// test/unit/counter.spec.js</span>
describe(<span class="hljs-string">"Counter"</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> wrapper = mount(Counter);
  test(<span class="hljs-string">"counter class"</span>, <span class="hljs-function">() =></span> &#123;
    expect(wrapper.classes()).toContain(<span class="hljs-string">"counter"</span>);
    expect(wrapper.classes(<span class="hljs-string">"counter"</span>)).toBe(<span class="hljs-literal">true</span>);
  &#125;);
  test(<span class="hljs-string">"counter has span"</span>, <span class="hljs-function">() =></span> &#123;
    expect(wrapper.html()).toContain(<span class="hljs-string">"<span class="</span>count<span class="hljs-string">">0</span>"</span>);
  &#125;);
  test(<span class="hljs-string">"counter has btn"</span>, <span class="hljs-function">() =></span> &#123;
    expect(wrapper.find(<span class="hljs-string">"button#add"</span>).exists()).toBe(<span class="hljs-literal">true</span>);
    expect(wrapper.find(<span class="hljs-string">"button#add"</span>).exists()).not.toBe(<span class="hljs-literal">false</span>);
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　上面几个函数我们根据名字也能猜出它们的作用：</p>
<ul>
<li>classes：获取wrapper的class，并返回一个数组</li>
<li>html：获取组件渲染html结构字符串</li>
<li>find：返回匹配子元素的wrapper</li>
<li>exists：断言wrapper是否存在</li>
</ul>
<p>　　find返回的是查找的第一个DOM节点，但有些情况我们希望能操作一组DOM，我们可以用<code>findAll</code>函数：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> wrapper = mount(Counter);
<span class="hljs-comment">// 返回一组wrapper</span>
<span class="hljs-keyword">const</span> divList = wrapper.findAll(<span class="hljs-string">'div'</span>);
divList.length
<span class="hljs-comment">// 找到第一个div，返回它的wrapper</span>
<span class="hljs-keyword">const</span> firstDiv = divList.at(<span class="hljs-number">0</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　有些组件需要通过外部传入的props、插槽slots、provide/inject等其他的插件或者属性，我们在mount挂载时可以传入一个对象，设置这些额外属性：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> wrapper = mount(Component, &#123;
  <span class="hljs-comment">// 向组件传入data，合并到现有的data中</span>
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">foo</span>: <span class="hljs-string">"bar"</span>
    &#125;
  &#125;,
  <span class="hljs-comment">// 设置组件的props</span>
  <span class="hljs-attr">propsData</span>: &#123;
    <span class="hljs-attr">msg</span>: <span class="hljs-string">"hello"</span>
  &#125;,
  <span class="hljs-comment">// vue本地拷贝</span>
  localVue,
  <span class="hljs-comment">// 伪造全局对象</span>
  <span class="hljs-attr">mocks</span>: &#123;
    $route
  &#125;,
  <span class="hljs-comment">// 插槽</span>
  <span class="hljs-comment">// 键名就是相应的 slot 名</span>
  <span class="hljs-comment">// 键值可以是一个组件、一个组件数组、一个字符串模板或文本。</span>
  <span class="hljs-attr">slots</span>: &#123;
    <span class="hljs-attr">default</span>: SlotComponent,
    <span class="hljs-attr">foo</span>: <span class="hljs-string">"<div />"</span>,
    <span class="hljs-attr">bar</span>: <span class="hljs-string">"<my-component />"</span>,
    <span class="hljs-attr">baz</span>: <span class="hljs-string">""</span>
  &#125;,
  <span class="hljs-comment">// 用来注册自定义组件</span>
  <span class="hljs-attr">stubs</span>: &#123;
    <span class="hljs-string">"my-component"</span>: MyComponent,
    <span class="hljs-string">"el-button"</span>: <span class="hljs-literal">true</span>,
  &#125;,
  <span class="hljs-comment">// 设置组件实例的$attrs 对象。</span>
  <span class="hljs-attr">attrs</span>: &#123;&#125;,
  <span class="hljs-comment">// 设置组件实例的$listeners对象。</span>
  <span class="hljs-attr">listeners</span>: &#123;
    <span class="hljs-attr">click</span>: jest.fn()
  &#125;,
  <span class="hljs-comment">// 为组件传递用于注入的属性</span>
  <span class="hljs-attr">provide</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">foo</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-string">"fooValue"</span>
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　<code>stubs</code>主要用来处理在全局注册的自定义组件，比如我们常用的组件库Element等，直接使用<code>el-button</code>、<code>el-input</code>组件，或者vue-router注册在全局的<code>router-view</code>组件等；当我们在单元测试中引入时就会提示我们对应的组件找不到，这时我们就可以通过这个<code>stubs</code>来避免报错。</p>
<p>　　我们在对某个组件进行单元测试时，希望只针对单一组件进行测试，避免子组件带来的副作用；比如我们在<code>父组件ParentComponent</code>中判断是否有某个div时，恰好子组件<code>ChildComponent</code>也渲染了该div，那么就会对我们的测试带来一定的干扰；我们可以使用<code>shallowMount</code>挂载函数，相遇比mount，shallowMount不会渲染子组件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; shallowMount &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@vue/test-utils'</span>
<span class="hljs-keyword">const</span> wrapper = shallowMount(Component)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　这样就保证了我们需要测试的组件在渲染时不会渲染其子组件，避免子组件的干扰。</p>
<h2 data-id="heading-9">操作组件</h2>
<p>　　我们经常需要对子组件中的元素或者子组件的数据进行一些操作和修改，比如页面的点击、修改data数据，进行操作后再来断言数据是否正确；我们以一个简单的Form组件为例：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"form"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"title"</span>></span>&#123;&#123; title &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span>></span>请填写姓名：<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"name-input"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"name"</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"name"</span>></span>&#123;&#123; name &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span>></span>请选择性别：<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"radio"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"sex"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"sex"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"f"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">""</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"radio"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"sex"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"sex"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"m"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">""</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span>></span>请选择爱好：<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
      footbal
      <span class="hljs-tag"><<span class="hljs-name">input</span>
        <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span>
        <span class="hljs-attr">name</span>=<span class="hljs-string">"hobby"</span>
        <span class="hljs-attr">v-model</span>=<span class="hljs-string">"hobby"</span>
        <span class="hljs-attr">value</span>=<span class="hljs-string">"footbal"</span>
      /></span>
      basketball
      <span class="hljs-tag"><<span class="hljs-name">input</span>
        <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span>
        <span class="hljs-attr">name</span>=<span class="hljs-string">"hobby"</span>
        <span class="hljs-attr">v-model</span>=<span class="hljs-string">"hobby"</span>
        <span class="hljs-attr">value</span>=<span class="hljs-string">"basketball"</span>
      /></span>
      ski
      <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"hobby"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"hobby"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"ski"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">input</span>
        <span class="hljs-attr">:class</span>=<span class="hljs-string">"submit ? 'submit' : ''"</span>
        <span class="hljs-attr">type</span>=<span class="hljs-string">"submit"</span>
        <span class="hljs-attr">value</span>=<span class="hljs-string">"提交"</span>
        @<span class="hljs-attr">click</span>=<span class="hljs-string">"clickSubmit"</span>
      /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"Form"</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">title</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-string">"表单名称"</span>,
    &#125;,
  &#125;,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">""</span>,
      <span class="hljs-attr">sex</span>: <span class="hljs-string">"f"</span>,
      <span class="hljs-attr">hobby</span>: [],
      <span class="hljs-attr">submit</span>: <span class="hljs-literal">false</span>,
    &#125;;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">clickSubmit</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.submit = !<span class="hljs-built_in">this</span>.submit;
    &#125;,
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　我们可以向Form表单组件传入一个title，作为表单的名称，其内部也有input、radio和checkbox等一系列元素，我们就来看下怎么对这些元素进行修改；首先我们来修改props的值，在组件初始化的时候我们传入了<code>propsData</code>，在后续的代码中我们可以通过<code>setProps</code>对props值进行修改：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> wrapper = mount(Form, &#123;
  <span class="hljs-attr">propsData</span>: &#123;
    <span class="hljs-attr">title</span>: <span class="hljs-string">"form title"</span>,
  &#125;,
&#125;);
<span class="hljs-keyword">const</span> vm = wrapper.vm;
test(<span class="hljs-string">"change prop"</span>, <span class="hljs-function">() =></span> &#123;
  expect(wrapper.find(<span class="hljs-string">".title"</span>).text()).toBe(<span class="hljs-string">"form title"</span>);
  wrapper.setProps(&#123;
    <span class="hljs-attr">title</span>: <span class="hljs-string">"new form title"</span>,
  &#125;);
  <span class="hljs-comment">// 报错了</span>
  expect(wrapper.find(<span class="hljs-string">".title"</span>).text()).toBe(<span class="hljs-string">"new form title"</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　我们满怀期待进行测试，但是发现最后一条断言报错了；这是因为Vue异步更新数据，我们改变prop和data后，获取dom发现数据并不会立即更新；在页面上我们一般都会通过<code>$nextTick</code>进行解决，在单元测试时，我们也可以使用nextTick配合获取DOM：</p>
<pre><code class="hljs language-js copyable" lang="js">test(<span class="hljs-string">"change prop1"</span>, <span class="hljs-keyword">async</span> () => &#123;
  expect(wrapper.find(<span class="hljs-string">".title"</span>).text()).toBe(<span class="hljs-string">"new form title"</span>);
  wrapper.setProps(&#123;
    <span class="hljs-attr">title</span>: <span class="hljs-string">"new form title1"</span>,
  &#125;);
  <span class="hljs-keyword">await</span> Vue.nextTick();
  <span class="hljs-comment">// 或者使用vm的nextTick</span>
  <span class="hljs-comment">// await wrapper.vm.nextTick();</span>
  expect(wrapper.find(<span class="hljs-string">".title"</span>).text()).toBe(<span class="hljs-string">"new form title1"</span>);
&#125;);

test(<span class="hljs-string">"change prop2"</span>, <span class="hljs-function">(<span class="hljs-params">done</span>) =></span> &#123;
  expect(wrapper.find(<span class="hljs-string">".title"</span>).text()).toBe(<span class="hljs-string">"new form title1"</span>);
  wrapper.setProps(&#123;
    <span class="hljs-attr">title</span>: <span class="hljs-string">"new form title2"</span>,
  &#125;);
  Vue.nextTick(<span class="hljs-function">() =></span> &#123;
    expect(wrapper.find(<span class="hljs-string">".title"</span>).text()).toBe(<span class="hljs-string">"new form title2"</span>);
    done();
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　和Jest中测试异步代码一样，我们也可以使用<code>done回调</code>或者<code>async/await</code>来进行异步测试；除了设置props，<code>setData</code>可以用来改变wrapper中的data：</p>
<pre><code class="hljs language-js copyable" lang="js">test(<span class="hljs-string">"test set data"</span>, <span class="hljs-keyword">async</span> () => &#123;
  wrapper.setData(&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"new name"</span>,
  &#125;);
  expect(vm.name).toBe(<span class="hljs-string">"new name"</span>);
  <span class="hljs-keyword">await</span> Vue.nextTick();
  expect(wrapper.find(<span class="hljs-string">".name"</span>).text()).toBe(<span class="hljs-string">"new name"</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　对于input、textarea或者select这种输入性的组件元素，我们有两种方式来改变他们的值：</p>
<pre><code class="hljs language-js copyable" lang="js">test(<span class="hljs-string">"test input set value"</span>, <span class="hljs-keyword">async</span> () => &#123;
  <span class="hljs-keyword">const</span> input = wrapper.find(<span class="hljs-string">"#name-input"</span>);
  <span class="hljs-keyword">await</span> input.setValue(<span class="hljs-string">"change input by setValue"</span>);
  expect(vm.name).toBe(<span class="hljs-string">"change input by setValue"</span>);
  expect(input.element.value).toBe(<span class="hljs-string">"change input by setValue"</span>);
&#125;);
<span class="hljs-comment">// 等价于</span>
test(<span class="hljs-string">"test input trigger"</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> input = wrapper.find(<span class="hljs-string">"#name-input"</span>);
  input.element.value = <span class="hljs-string">"change input by trigger"</span>;
  <span class="hljs-comment">// 通过input.element.value改变值后必须触发trigger才能真正修改</span>
  input.trigger(<span class="hljs-string">"input"</span>);
  expect(vm.name).toBe(<span class="hljs-string">"change input by trigger"</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　可以看出，通过<code>input.element.value</code>或者<code>setValue</code>的两种方式改变值后，由于v-model绑定关系，因此vm中的data数据也进行了改变；我们还可以通过<code>input.element.value</code>来获取input元素的值。</p>
<p>　　对于radio、checkbox选择性的组件元素，我们可以通过<code>setChecked(Boolean)</code>函数来触发值的更改，更改同时也会更新元素上v-model绑定的值：</p>
<pre><code class="hljs language-js copyable" lang="js">test(<span class="hljs-string">"test radio"</span>, <span class="hljs-function">() =></span> &#123;
  expect(vm.sex).toBe(<span class="hljs-string">"f"</span>);
  <span class="hljs-keyword">const</span> radioList = wrapper.findAll(<span class="hljs-string">'input[name="sex"]'</span>);
  radioList.at(<span class="hljs-number">1</span>).setChecked();
  expect(vm.sex).toBe(<span class="hljs-string">"m"</span>);
&#125;);
test(<span class="hljs-string">"test checkbox"</span>, <span class="hljs-function">() =></span> &#123;
  expect(vm.hobby).toEqual([]);
  <span class="hljs-keyword">const</span> checkboxList = wrapper.findAll(<span class="hljs-string">'input[name="hobby"]'</span>);
  checkboxList.at(<span class="hljs-number">0</span>).setChecked();
  expect(vm.hobby).toEqual([<span class="hljs-string">"footbal"</span>]);
  checkboxList.at(<span class="hljs-number">1</span>).setChecked();
  expect(vm.hobby).toEqual([<span class="hljs-string">"footbal"</span>, <span class="hljs-string">"basketball"</span>]);
  checkboxList.at(<span class="hljs-number">0</span>).setChecked(<span class="hljs-literal">false</span>);
  expect(vm.hobby).toEqual([<span class="hljs-string">"basketball"</span>]);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　对于按钮等元素，我们希望在上面触发点击操作，可以使用<code>trigger</code>进行触发：</p>
<pre><code class="hljs language-js copyable" lang="js">test(<span class="hljs-string">"test click"</span>, <span class="hljs-keyword">async</span> () => &#123;
  <span class="hljs-keyword">const</span> submitBtn = wrapper.find(<span class="hljs-string">'input[type="submit"]'</span>);
  <span class="hljs-keyword">await</span> submitBtn.trigger(<span class="hljs-string">"click"</span>);
  expect(vm.submit).toBe(<span class="hljs-literal">true</span>);
  <span class="hljs-keyword">await</span> submitBtn.trigger(<span class="hljs-string">"click"</span>);
  expect(vm.submit).toBe(<span class="hljs-literal">false</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">自定义事件</h2>
<p>　　对于一些组件，可能会通过<code>$emit</code>触发一些返回数据，比如我们改写上面Form表单中的submit按钮，点击后返回一些数据：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">clickSubmit</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">"foo"</span>, <span class="hljs-string">"foo1"</span>, <span class="hljs-string">"foo2"</span>);
      <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">"bar"</span>, <span class="hljs-string">"bar1"</span>);
    &#125;,
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　除了触发组件中元素的点击事件进行$emi，我们还可以通过<code>wrapper.vm</code>触发，因为vm本身相当于组件的<code>this</code>：</p>
<pre><code class="hljs language-js copyable" lang="js">wrapper.vm.$emit(<span class="hljs-string">"foo"</span>, <span class="hljs-string">"foo3"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　最后，所有$emit触发返回的数据都存储在<code>wrapper.emitted()</code>，它返回了一个对象；结构如下：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">foo</span>: [ [ <span class="hljs-string">'foo1'</span>, <span class="hljs-string">'foo2'</span> ], [ <span class="hljs-string">'foo3'</span> ] ],
    <span class="hljs-attr">bar</span>: [ [ <span class="hljs-string">'bar1'</span> ] ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　<code>emitted()</code>返回对象中的属性是一个数组，数组的length代表了这个方法被触发了多少次；我们可以对对象上的属性进行断言，来判断组件的emit是否被触发：</p>
<pre><code class="hljs language-js copyable" lang="js">test(<span class="hljs-string">"test emit"</span>, <span class="hljs-keyword">async</span> () => &#123;
  <span class="hljs-comment">// 组件元素触发emit</span>
  <span class="hljs-keyword">await</span> wrapper.find(<span class="hljs-string">'input[type="submit"]'</span>).trigger(<span class="hljs-string">"click"</span>);
  wrapper.vm.$emit(<span class="hljs-string">"foo"</span>, <span class="hljs-string">"foo3"</span>);
  <span class="hljs-keyword">await</span> vm.$nextTick();
  <span class="hljs-comment">// foo被触发过</span>
  expect(wrapper.emitted().foo).toBeTruthy();
  <span class="hljs-comment">// foo触发过两次</span>
  expect(wrapper.emitted().foo.length).toBe(<span class="hljs-number">2</span>);
  <span class="hljs-comment">// 断言foo第一次触发的数据</span>
  expect(wrapper.emitted().foo[<span class="hljs-number">0</span>]).toEqual([<span class="hljs-string">"foo1"</span>, <span class="hljs-string">"foo2"</span>]);
  <span class="hljs-comment">// baz没有触发</span>
  expect(wrapper.emitted().baz).toBeFalsy();
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　我们也可以把<code>emitted()</code>函数进行改写，并不是一次性获取整个<code>emitted对象</code>：</p>
<pre><code class="hljs language-js copyable" lang="js">expect(wrapper.emitted(<span class="hljs-string">'foo'</span>)).toBeTruthy();
expect(wrapper.emitted(<span class="hljs-string">'foo'</span>).length).toBe(<span class="hljs-number">2</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　有一些组件触发emit事件可能是由其子组件触发的，我们可以通过子组件的vm进行emit：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; mount &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@vue/test-utils'</span>
<span class="hljs-keyword">import</span> ParentComponent <span class="hljs-keyword">from</span> <span class="hljs-string">'@/components/ParentComponent'</span>
<span class="hljs-keyword">import</span> ChildComponent <span class="hljs-keyword">from</span> <span class="hljs-string">'@/components/ChildComponent'</span>

describe(<span class="hljs-string">'ParentComponent'</span>, <span class="hljs-function">() =></span> &#123;
  it(<span class="hljs-string">"emit"</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> wrapper = mount(ParentComponent)
    wrapper.find(ChildComponent).vm.$emit(<span class="hljs-string">'custom'</span>)
  &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">配合Vue-Router</h2>
<p>　　在有些组件中，我们有可能会用到<code>Vue-Router</code>的相关组件或者Api方法，比如我们有一个Header组件：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"jump"</span>></span>&#123;&#123; $route.params.id &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">:to</span>=<span class="hljs-string">"&#123; path: '/detail' &#125;"</span>></span><span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;&#125;;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">jump</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.$router.push(&#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">"/list"</span>,
      &#125;);
    &#125;,
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　直接在测试脚本中引入会报错，提示找不到<code>router-link</code>和<code>router-view</code>两个组件和<code>$route</code>属性；这里不推荐使用<code>Vue.use(VueRouter)</code>，因为会污染全局的Vue；我们有两种方法解决，第一种使用<code>createLocalVue </code>创建一个Vue的类，我们可以在这个类中进行添加组件、混入和安装插件而不会污染全局的Vue类：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; shallowMount, createLocalVue &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@vue/test-utils'</span>
<span class="hljs-keyword">import</span> VueRouter <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>
<span class="hljs-keyword">import</span> Header <span class="hljs-keyword">from</span> <span class="hljs-string">"@/components/Header"</span>;

<span class="hljs-comment">// 一个Vue类</span>
<span class="hljs-keyword">const</span> localVue = createLocalVue()
localVue.use(VueRouter)
<span class="hljs-comment">// 路由数组</span>
<span class="hljs-keyword">const</span> routes = []
<span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  routes
&#125;)

shallowMount(Header, &#123;
  localVue,
  router
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　我们来看下这里做了哪些操作，通过<code>createLocalVue</code>创建了一个localVue，相当于<code>import Vue</code>；然后<code>localVue.use</code>告诉Vue来使用VueRouter，和<code>Vue.use</code>有着相同的作用；最后实例化创建<code>router</code>对象传入shallowMount进行挂载。</p>
<p>　　第二种方式是注入伪造数据，这里主要用的就是<code>mocks</code>和<code>stubs</code>，<code>mocks</code>用来伪造<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>r</mi><mi>o</mi><mi>u</mi><mi>t</mi><mi>e</mi><mtext>和</mtext></mrow><annotation encoding="application/x-tex">route和</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">o</span><span class="mord mathnormal">u</span><span class="mord mathnormal">t</span><span class="mord mathnormal">e</span><span class="mord cjk_fallback">和</span></span></span></span></span>router等全局对象，是一种将属性添加到<code>Vue.prototype</code>上的方式；而<code>stubs</code>用来覆写全局或局部注册的组件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; mount &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@vue/test-utils"</span>;
<span class="hljs-keyword">import</span> Header <span class="hljs-keyword">from</span> <span class="hljs-string">"@/components/Header"</span>;

describe(<span class="hljs-string">"header"</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> $route = &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">"/home"</span>,
    <span class="hljs-attr">params</span>: &#123;
      <span class="hljs-attr">id</span>: <span class="hljs-string">"111"</span>,
    &#125;,
  &#125;;
  <span class="hljs-keyword">const</span> $router = &#123;
    <span class="hljs-attr">push</span>: jest.fn(),
  &#125;;
  <span class="hljs-keyword">const</span> wrapper = mount(Header, &#123;
    <span class="hljs-attr">stubs</span>: [<span class="hljs-string">"router-view"</span>, <span class="hljs-string">"router-link"</span>],
    <span class="hljs-attr">mocks</span>: &#123;
      $route,
      $router,
    &#125;,
  &#125;);
  <span class="hljs-keyword">const</span> vm = wrapper.vm;
  test(<span class="hljs-string">"render home div"</span>, <span class="hljs-function">() =></span> &#123;
    expect(wrapper.find(<span class="hljs-string">"div"</span>).text()).toBe(<span class="hljs-string">"111"</span>);
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　相比于第一种方式，第二种方式可操作性更强，可以直接伪造$route路由的数据；一般第一种方式不会单独使用，经常会搭配第二种伪造数据的方式。</p>
<h2 data-id="heading-12">配合Vuex</h2>
<p>　　我们通常会在组件中会用到vuex，我们可以通过伪造<code>store</code>数据来模拟测试，假如我们有一个的count组件，它的数据存放在vuex中：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"number"</span>></span>&#123;&#123; number &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"add"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"clickAdd"</span>></span>add<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"sub"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"clickSub"</span>></span>sub<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; mapState, mapGetters &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vuex"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"Count"</span>,
  <span class="hljs-attr">computed</span>: &#123;
    ...mapState(&#123;
      <span class="hljs-attr">number</span>: <span class="hljs-function">(<span class="hljs-params">state</span>) =></span> state.number,
    &#125;),
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">clickAdd</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.$store.commit(<span class="hljs-string">"ADD_COUNT"</span>);
    &#125;,
    <span class="hljs-function"><span class="hljs-title">clickSub</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.$store.commit(<span class="hljs-string">"SUB_COUNT"</span>);
    &#125;,
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　在vuex中我们通过<code>mutations</code>对number进行修改：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">state</span>: &#123;
    <span class="hljs-attr">number</span>: <span class="hljs-number">0</span>,
  &#125;,
  <span class="hljs-attr">mutations</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">ADD_COUNT</span>(<span class="hljs-params">state</span>)</span> &#123;
      state.number = state.number + <span class="hljs-number">1</span>;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">SUB_COUNT</span>(<span class="hljs-params">state</span>)</span> &#123;
      state.number = state.number - <span class="hljs-number">1</span>;
    &#125;,
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　那我们现在如何来伪造<code>store</code>数据呢？这里和<code>Vue-Router</code>的原理是一样的，通过<code>createLocalVue</code>创建一个隔离的Vue类：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; mount, createLocalVue &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@vue/test-utils"</span>;
<span class="hljs-keyword">import</span> Count <span class="hljs-keyword">from</span> <span class="hljs-string">"@/components/Count"</span>;
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">"vuex"</span>;

<span class="hljs-keyword">const</span> localVue = createLocalVue();
localVue.use(Vuex);

describe(<span class="hljs-string">"count"</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> state = &#123;
    <span class="hljs-attr">number</span>: <span class="hljs-number">0</span>,
  &#125;;
  <span class="hljs-keyword">const</span> mutations = &#123;
    <span class="hljs-attr">ADD_COUNT</span>: jest.fn(),
    <span class="hljs-attr">SUB_COUNT</span>: jest.fn(),
  &#125;;
  <span class="hljs-keyword">const</span> store = <span class="hljs-keyword">new</span> Vuex.Store(&#123;
    state,
    mutations
  &#125;);
  test(<span class="hljs-string">"render"</span>, <span class="hljs-keyword">async</span> () => &#123;
    <span class="hljs-keyword">const</span> wrapper = mount(Count, &#123;
      store,
      localVue,
    &#125;);
    expect(wrapper.find(<span class="hljs-string">".number"</span>).text()).toBe(<span class="hljs-string">"0"</span>);
    wrapper.find(<span class="hljs-string">".add"</span>).trigger(<span class="hljs-string">"click"</span>);
    expect(mutations.ADD_COUNT).toHaveBeenCalled();
    expect(mutations.SUB_COUNT).not.toHaveBeenCalled();
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　我们看一下这里做了什么操作，前面和VueRouter一样创建一个隔离类<code>localVue</code>；然后通过<code>new Vuex.Store</code>创建了一个store并填入假数据state和mutations；这里我们并不关心mutations中函数做了哪些操作，我们只要知道元素点击触发了哪个mutations函数，通过伪造的函数我们去断言mutations是否被调用。</p>
<p>　　另一种测试<code>store</code>数据的方式是创建一个运行中的store，不再通过页面触发Vuex中的函数，这样的好处就是不需要伪造Vuex函数；假设我们有一个<code>store/list.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">state</span>: &#123;
    <span class="hljs-attr">list</span>: [],
  &#125;,
  <span class="hljs-attr">getters</span>: &#123;
    <span class="hljs-attr">joinList</span>: <span class="hljs-function">(<span class="hljs-params">state</span>) =></span> &#123;
      <span class="hljs-keyword">return</span> state.list.join(<span class="hljs-string">","</span>);
    &#125;,
  &#125;,
  <span class="hljs-attr">mutations</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">PUSH</span>(<span class="hljs-params">state, payload</span>)</span> &#123;
      state.list.push(payload);
    &#125;,
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createLocalVue &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@vue/test-utils"</span>;
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">"vuex"</span>;
<span class="hljs-keyword">import</span> &#123; cloneDeep &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"lodash"</span>;
<span class="hljs-keyword">import</span> listStore <span class="hljs-keyword">from</span> <span class="hljs-string">"@/store/list"</span>;

describe(<span class="hljs-string">"list"</span>, <span class="hljs-function">() =></span> &#123;
  test(<span class="hljs-string">"expect list"</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> localVue = createLocalVue();
    localVue.use(Vuex);
    <span class="hljs-keyword">const</span> store = <span class="hljs-keyword">new</span> Vuex.Store(cloneDeep(listStore));
    expect(store.state.list).toEqual([]);
    store.commit(<span class="hljs-string">"PUSH"</span>, <span class="hljs-string">"1"</span>);
    expect(store.state.list).toEqual([<span class="hljs-string">"1"</span>]);
  &#125;);
  test(<span class="hljs-string">"list getter"</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> localVue = createLocalVue();
    localVue.use(Vuex);
    <span class="hljs-keyword">const</span> store = <span class="hljs-keyword">new</span> Vuex.Store(cloneDeep(listStore));

    expect(store.getters.joinList).toBe(<span class="hljs-string">""</span>);
    store.commit(<span class="hljs-string">"PUSH"</span>, <span class="hljs-string">"1"</span>);
    store.commit(<span class="hljs-string">"PUSH"</span>, <span class="hljs-string">"3"</span>);
    expect(store.getters.joinList).toBe(<span class="hljs-string">"1,3"</span>);
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　我们直接创建了一个store，通过store来进行commit和getters的操作。</p>
<h1 data-id="heading-13">总结</h1>
<p>　　前端框架迭代不断，但是前端单元测试确显有人关注；一个健壮的前端项目应该有单元测试的模块，保证了我们的项目代码质量和功能的稳定；但是也并不是所有的项目都需要有单元测试的，毕竟编写测试用例也需要成本；因此如果你的项目符合下面的几个条件，就可以考虑引入单元测试：</p>
<ul>
<li>长期稳定的项目迭代，需要保证代码的可维护性和功能稳定；</li>
<li>页面功能相对来说说比较复杂，逻辑较多；</li>
<li>对于一些复用性很高的组件，可以考虑单元测试；</li>
</ul>
<p>　　</p>
<p>更多前端资料请关注公众号<code>【前端壹读】</code>。</p>
<p>如果觉得写得还不错，请关注我的<a href="https://juejin.im/user/580038cebf22ec0064bd0b2d">掘金主页</a>。更多文章请访问<a href="http://xieyufei.com/" target="_blank" rel="nofollow noopener noreferrer">谢小飞的博客</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            