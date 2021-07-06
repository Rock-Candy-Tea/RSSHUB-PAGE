
---
title: '🔥一篇够用的TypeScript总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6879c5f8e72c4235bdfbd5a9840c6e31~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 06 Jul 2021 00:31:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6879c5f8e72c4235bdfbd5a9840c6e31~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、前言</h2>
<p>没写ts之前看<a href="https://www.tslang.cn/docs/home.html" target="_blank" rel="nofollow noopener noreferrer">官方文档</a>，被<code>那么多</code>特性吓尿了，实际上写业务用的特性不多。五月底ts正式升级了4.3版本，4.4也已经在beta版本了。差不多先生，够用就行，这里更多的是，以自己的理解去总结一下常用的ts特性。有理解错误的，<code>欢迎大哥指正</code>👏🏻</p>
<p>知识这种东西，学了还是要总结下，梳理清楚自己对当前知识的掌握程度。偷懒了一段时间，接下来要好好发力了。</p>
<blockquote>
<p>首发博客：<a href="https://alexwjj.github.io/" target="_blank" rel="nofollow noopener noreferrer">俊劫的学习基地</a> 欢迎star，一起学习！博客主页有吹水群，扫码加入！</p>
</blockquote>
<h2 data-id="heading-1">二、ts的优缺点</h2>
<h3 data-id="heading-2">1、优点</h3>
<ul>
<li><code>代码的可读性和可维护性</code>：举个🌰看后端某个<code>接口返回值</code>，一般需要去network看or去看接口文档，才知道返回数据结构，而正确用了ts后，编辑器会<code>提醒</code>接口返回值的类型，这点相当实用。</li>
<li>在<code>编译阶段</code>就发现大部分错误，避免了很多<code>线上bug</code></li>
<li>增强了编辑器和 IDE 的功能，包括<code>代码补全</code>、<code>接口提示</code>、<code>跳转到定义</code>、<code>重构</code>等</li>
</ul>
<h3 data-id="heading-3">2、缺点</h3>
<ul>
<li>有一定的<code>学习成本</code>，需要理解接口（Interfaces）、泛型（Generics）、类（Classes）、枚举类型（Enums）等前端工程师可能不是很熟悉的概念</li>
<li>会增加一些<code>开发成本</code>，当然这是前期的，后期维护更简单了</li>
<li>一些JavaScript库需要<code>兼容</code>，提供声明文件，像vue2，底层对ts的兼容就不是很好。</li>
<li>ts编译是需要<code>时间</code>的，这就意味着项目大了以后，开发环境启动和生产环境打包的速度就成了考验</li>
<li>可以看看<a href="https://www.infoq.cn/article/u72qtztgazttfazzihbz" target="_blank" rel="nofollow noopener noreferrer">Deno 内部代码将停用 TypeScript，并公布五项具体理由</a></li>
</ul>
<p>或多或少，听到过的开发体验最好的架构：<code>React Hooks + TypeScript</code>。目前也在用，还在学习中，至于到底好不好，我还是对<code>vue</code>
情有独钟。前端还在快速发展中，后面再出来个<code>xxxScript</code>，谁也说不好。所以一个字：<code>学！</code></p>
<h2 data-id="heading-4">三、anyScript</h2>
<p>可能因为业务场景或者业务紧张，or某个跑路的大哥省了点功夫，用了typeScript的项目也可能会变成<code>anyScript</code>。以下是几种救急的方式（<code>大哥们还没有其他办法</code>）：</p>
<ul>
<li>// @ts-nocheck 禁用整个文件的ts校验</li>
<li>// @ts-ignore 禁用单行ts校验</li>
<li>any和unknown</li>
</ul>
<p>不建议多用，但也不是不能用，有些场景确实不好写ts定义。这个时候就不要硬憋自己了，写个备注any下。</p>
<blockquote>
<p>抛个面试题：<code>你知道any和unknown的区别吗？</code></p>
</blockquote>
<p>回归正题，开始学习，总结一些项目中使用较多的，一些TS高级特性这里就不说了。</p>
<h2 data-id="heading-5">四、ts类型</h2>
<p>本篇所有demo都可在<a href="https://www.typescriptlang.org/zh/play" target="_blank" rel="nofollow noopener noreferrer">TypeScript Playground</a> 运行，不理解的建议都来跑跑看。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6879c5f8e72c4235bdfbd5a9840c6e31~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">1、基础类型</h3>
<ul>
<li>常用：boolean、number、string、array、enum、any、void</li>
<li>不常用：tuple、null、undefine、never</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> count: number = <span class="hljs-number">20210701</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">2、对象类型</h3>
<p>简单理解interface 和 type 的区别：type 更强大，interface 可以进行<code>声明合并</code>，type 不行；</p>
<p>看个人习惯，一般声明都用interface，需要用到其他变量类型，type多一些。有没有interface或type<code>一把梭的</code>🤣？</p>
<pre><code class="hljs language-js copyable" lang="js">interface Hero &#123;
  <span class="hljs-attr">name</span>: string;
  age: number;
  skill: string;
  skinNum?: number;
  say(): string; <span class="hljs-comment">// say函数返回值为string</span>
  [propname: string]: any; <span class="hljs-comment">// 当前Hero可定义任意字符串类型的key</span>
&#125;
<span class="hljs-comment">// 继承</span>
interface littleSoldier <span class="hljs-keyword">extends</span> Hero &#123;
  rush(): string;
&#125;
<span class="hljs-comment">// 任意类型</span>
interface IAnyObject &#123;
  [key: string]: any;
&#125;

type Hero = &#123;
  <span class="hljs-attr">name</span>: string,
  <span class="hljs-attr">age</span>: number,
  <span class="hljs-attr">skill</span>: string,
  skinNum?: number,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">3、数组类型</h3>
<p>项目中常见的写法，需要声明<code>列表数据</code>类型：</p>
<pre><code class="hljs language-js copyable" lang="js">interface IItem &#123;
  <span class="hljs-attr">id</span>: number;
  name: string;
  isDad: boolean;
&#125;
<span class="hljs-keyword">const</span> objectArr: IItem[] = [&#123; <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'俊劫'</span>, <span class="hljs-attr">isGod</span>: <span class="hljs-literal">true</span> &#125;];
<span class="hljs-comment">// or</span>
<span class="hljs-keyword">const</span> objectArr: <span class="hljs-built_in">Array</span><IItem> = [&#123; <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'俊劫'</span>, <span class="hljs-attr">isGod</span>: <span class="hljs-literal">true</span> &#125;];

<span class="hljs-keyword">const</span> numberArr: number[] = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];

<span class="hljs-keyword">const</span> arr: (number | string)[] = [<span class="hljs-number">1</span>, <span class="hljs-string">"string"</span>, <span class="hljs-number">2</span>];
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">4、元组 tuple</h3>
<p>元组和数组类似，但是类型注解时会不一样</p>
<p>赋值的类型、位置、个数需要和定义（生明）的类型、位置、个数一致。</p>
<p>暂时没用过，感觉用处不大~~~</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 数组 某个位置的值可以是注解中的任何一个</span>
<span class="hljs-keyword">const</span> LOL: (string | number)[] = [<span class="hljs-string">"zed"</span>, <span class="hljs-number">25</span>, <span class="hljs-string">"darts"</span>];

<span class="hljs-comment">// 元祖 每一项数据类型必须一致</span>
<span class="hljs-keyword">const</span> LOL: [string, string, number] = [<span class="hljs-string">"zed"</span>, <span class="hljs-string">"darts"</span>, <span class="hljs-number">25</span>];
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">5、联合| or 交叉&类型</h3>
<ul>
<li>联合类型：某个变量可能是多个 interface 中的其中一个，用 <code>|</code> 分割</li>
<li>交叉类型：由多个类型组成，用 <code>&</code> 连接</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// anjiao 某胖博主爱好</span>
interface Waiter &#123;
  <span class="hljs-attr">anjiao</span>: boolean;
  say: <span class="hljs-function">() =></span> &#123;&#125;;
&#125;

interface Teacher &#123;
  <span class="hljs-attr">anjiao</span>: boolean;
  skill: <span class="hljs-function">() =></span> &#123;&#125;;
&#125;

<span class="hljs-comment">// 联合类型</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">judgeWho</span>(<span class="hljs-params">animal: Waiter | Teacher</span>) </span>&#123;&#125;
<span class="hljs-comment">// 交叉类型 </span>
<span class="hljs-comment">// 同名类型会进行合并，同名基础类型属性的合并返回：never</span>
<span class="hljs-comment">// 同名非基础类型属性可以正常合并</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">judgeWho</span>(<span class="hljs-params">jishi: Waiter & Teacher</span>) </span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">6、enum枚举</h3>
<p>提高代码可维护性，统一维护某些枚举值，避免 <code>JiShi === 1</code>这种魔法数字。<code>JiShi === JiShiEnum.BLUEJ</code>这样写，老板一眼就知道我想找谁。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 初始值默认为 0</span>
enum JiShiEnum &#123;
     REDJ,
     BLUEJ,
     GREENJ,
&#125;
<span class="hljs-comment">// 设置初始值</span>
enum JiShiEnum &#123;
     REDJ = <span class="hljs-number">8</span>,
     BLUEJ,
     GREENJ,
&#125;
<span class="hljs-keyword">const</span> jishi: JiShiEnum = JiShiENUM.BLUE
<span class="hljs-built_in">console</span>.log(jishi) <span class="hljs-comment">// 9</span>
<span class="hljs-comment">// 字符串枚举，每个都需要声明</span>
enum JiShiEnum &#123;
     REDJ = <span class="hljs-string">"8号"</span>,
     BLUEJ = <span class="hljs-string">"9号"</span>,
     GREENJ = <span class="hljs-string">"10号"</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">7、泛型 T（Type）</h3>
<p>简单说就是：泛指的类型，不确定的类型，可以理解为一个<code>占位符</code>（使用T只是习惯，使用任何字母都行）</p>
<ul>
<li>K（Key）：表示对象中的键类型；</li>
<li>V（Value）：表示对象中的值类型；</li>
<li>E（Element）：表示元素类型。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// T 自定义名称</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myFun</span><<span class="hljs-title">T</span>>(<span class="hljs-params">params: T[]</span>) </span>&#123;
  <span class="hljs-keyword">return</span> params;
&#125;
myFun <string> [<span class="hljs-string">"123"</span>, <span class="hljs-string">"456"</span>];

<span class="hljs-comment">// 定义多个泛型</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">join</span><<span class="hljs-title">T</span>, <span class="hljs-title">P</span>>(<span class="hljs-params">first: T, second: P</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;first&#125;</span><span class="hljs-subst">$&#123;second&#125;</span>`</span>;
&#125;
join <number, string> (<span class="hljs-number">1</span>, <span class="hljs-string">"2"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">8、断言</h3>
<p>主要通过 <code>as</code> 语法，<code>告诉ts</code>这个变量属于哪个类型，一般用在你比 TypeScript 更了解某个值的详细信息。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">judgeWho</span>(<span class="hljs-params">animal: Waiter | Teacher</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (animal.anjiao) &#123;
    (animal <span class="hljs-keyword">as</span> Teacher).skill();
  &#125;<span class="hljs-keyword">else</span>&#123;
    (animal <span class="hljs-keyword">as</span> Waiter).say();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">9、in</h3>
<p>类似于数组和字符串的 <code>includes</code> 方法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">judgeWhoTwo</span>(<span class="hljs-params">animal: Waiter | Teacher</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-string">"skill"</span> <span class="hljs-keyword">in</span> animal) &#123;
    animal.skill();
  &#125; <span class="hljs-keyword">else</span> &#123;
    animal.say();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">10、类型注解</h3>
<p>显式的告诉代码，我们的 count 变量就是一个数字类型，这就叫做类型注解</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> count: number; <span class="hljs-comment">// 类型注解</span>
count = <span class="hljs-number">123</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">11、类型推断</h3>
<ul>
<li>如果 TS 能够自动分析变量类型， 我们就什么也不需要做了</li>
<li>如果 TS 无法分析变量类型的话， 我们就需要使用类型注解</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ts可以推断出count 为number类型</span>
<span class="hljs-keyword">let</span> count = <span class="hljs-number">123</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">12、void和never</h3>
<p>返回值类型，也算是基础类型。没有返回值的函数: void</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sayHello</span>(<span class="hljs-params"></span>): <span class="hljs-title">void</span> </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"hello world"</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果一个函数是永远也执行不完的，就可以定义返回值为 never</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">errorFuntion</span>(<span class="hljs-params"></span>): <span class="hljs-title">never</span> </span>&#123;
  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>();
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Hello World"</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一个函数有入参，也有出参，项目中的常规写法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 定义一个小姐姐</span>
interface IGirl &#123;
  <span class="hljs-attr">name</span>: string,
  <span class="hljs-attr">age</span>: number,
  <span class="hljs-attr">skill</span>: string,
  <span class="hljs-attr">isAnMo</span>: boolean;
  number: JiShiEnum;
&#125;;
<span class="hljs-comment">// 定义搜索小姐姐的入参</span>
interface ISearchParams <span class="hljs-keyword">extends</span> IGirl&#123;
  <span class="hljs-attr">serviceTime</span>: string;
&#125;
interface IGetGirls &#123;
  <span class="hljs-attr">data</span>: IGirl[];
&#125;
<span class="hljs-comment">// 函数主体</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getGirls</span>(<span class="hljs-params">data: ISearchParams</span>): <span class="hljs-title">Promise</span><<span class="hljs-title">IGetGirls</span>> </span>&#123;
  <span class="hljs-keyword">return</span> axios(&#123;
    <span class="hljs-attr">url</span>: <span class="hljs-string">`/dabaojian/getGirls`</span>,
    <span class="hljs-attr">method</span>: <span class="hljs-string">'GET'</span>,
    data,
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">13、类型检测</h3>
<h4 data-id="heading-19">1、typeof</h4>
<p>typeof 操作符可以用来获取一个变量或对象的类型</p>
<pre><code class="hljs language-js copyable" lang="js">interface Hero &#123;
  <span class="hljs-attr">name</span>: string;
  skill: string;
&#125;

<span class="hljs-keyword">const</span> zed: Hero = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"影流之主"</span>, <span class="hljs-attr">skill</span>: <span class="hljs-string">"影子"</span> &#125;;
type LOL = <span class="hljs-keyword">typeof</span> zed; <span class="hljs-comment">// type LOL = Hero</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面代码中，我们通过 typeof 操作符获取 zed 变量的类型并赋值给 LOL 类型变量，之后我们就可以使用 LOL 类型</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> ahri: LOL = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"阿狸"</span>, <span class="hljs-attr">skill</span>: <span class="hljs-string">"魅惑"</span> &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">2、instanceof</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">NumberObj</span> </span>&#123;
  <span class="hljs-attr">count</span>: number;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addObj</span>(<span class="hljs-params">first: object | NumberObj, second: object | NumberObj</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (first <span class="hljs-keyword">instanceof</span> NumberObj && second <span class="hljs-keyword">instanceof</span> NumberObj) &#123;
    <span class="hljs-keyword">return</span> first.count + second.count;
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-21">3、keyof</h4>
<p>keyof 与 Object.keys 略有相似，只不过 keyof 取 interface 的键</p>
<pre><code class="hljs language-js copyable" lang="js">interface Point &#123;
    <span class="hljs-attr">x</span>: number;
    y: number;
&#125;

<span class="hljs-comment">// type keys = "x" | "y"</span>
type keys = keyof Point;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>用 keyof 可以更好的定义数据类型</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">get</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">object</span>, <span class="hljs-title">K</span> <span class="hljs-title">extends</span> <span class="hljs-title">keyof</span> <span class="hljs-title">T</span>>(<span class="hljs-params">o: T, name: K</span>): <span class="hljs-title">T</span>[<span class="hljs-title">K</span>] </span>&#123;
  <span class="hljs-keyword">return</span> o[name]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">14、ts类里的关键字</h3>
<p>了解ts关键字的作用，在写base类的时候可能会用到，个人用的不多。</p>
<ul>
<li>public</li>
<li>private 类的外部不可用，继承也不行</li>
<li>protected 类的外部不可用，继承可以</li>
<li>public readOnly xxx 只读属性</li>
<li>static funcXXX 静态方法，不需要 new 就可以调用</li>
<li>abstract funcXXX 抽象类，所有子类都必须要实现 funcXXX</li>
</ul>
<h2 data-id="heading-23">五、tsconfig</h2>
<p>需要去了解 tsconfig.json 中一些参数的说明，具体参考官方文档<a href="https://www.tslang.cn/docs/handbook/tsconfig-json.html" target="_blank" rel="nofollow noopener noreferrer">tsconfig.json
</a></p>
<h3 data-id="heading-24">1、作用：</h3>
<ul>
<li>用于标识 TypeScript 项目的根路径；</li>
<li>用于配置 TypeScript 编译器；</li>
<li>用于指定编译的文件。</li>
</ul>
<h3 data-id="heading-25">2、注意事项：</h3>
<ul>
<li>tsc -init 生成 tsconfig.json，项目目录下直接 tsc,编译的时候就会走配置文件</li>
<li>compilerOptions 内部字段含义 <a href="https://juejin.cn/post/6872111128135073806#heading-110" target="_blank">阿宝哥 这篇文章有详细说明</a></li>
<li>项目别名配置：遇到过的一个坑，仅在项目config中配置别名不生效，需要在tsconfig.json中再配置一遍</li>
</ul>
<h2 data-id="heading-26">六、Utility Types</h2>
<p>Utility Types： 可以理解为基于ts封装的工具类型;</p>
<p>具体源码解析可以参考：</p>
<ul>
<li><a href="https://juejin.cn/post/6865910915011706887" target="_blank">源码解读utility-types</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/120802610" target="_blank" rel="nofollow noopener noreferrer">TypeScript Utility Types 学习笔记及源码解析</a></li>
</ul>
<h3 data-id="heading-27">1、<code>Partial<T></code></h3>
<p>将T中所有属性转换为可选属性。返回的类型可以是T的任意子集</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> interface UserModel &#123;
  <span class="hljs-attr">name</span>: string;
  age?: number;
  sex: number;
&#125;

type JUserModel = Partial<UserModel>
<span class="hljs-comment">// =</span>
type JUserModel = &#123;
    name?: string | <span class="hljs-literal">undefined</span>;
    age?: number | <span class="hljs-literal">undefined</span>;
    sex?: number | <span class="hljs-literal">undefined</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 源码解析</span>
type Partial<T> = &#123; [P <span class="hljs-keyword">in</span> keyof T]?: T[P]; &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-28">2、<code>Required<T></code></h3>
<p>通过将T的所有属性设置为必选属性来构造一个新的类型。与Partial相反</p>
<pre><code class="hljs language-js copyable" lang="js">type JUserModel2 = Required<UserModel>
<span class="hljs-comment">// =</span>
type JUserModel2 = &#123;
    <span class="hljs-attr">name</span>: string;
    age: number;
    sex: number;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-29">3、<code>Readonly<T></code></h3>
<p>将T中所有属性设置为只读</p>
<pre><code class="hljs language-js copyable" lang="js">type JUserModel3 = Readonly<UserModel>

<span class="hljs-comment">// =</span>
type JUserModel3 = &#123;
    readonly name: string;
    readonly age?: number | <span class="hljs-literal">undefined</span>;
    readonly sex: number;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-30">4、<code>Record<K,T></code></h3>
<p>构造一个类型，该类型具有一组属性K，每个属性的类型为T。可用于将一个类型的属性映射为另一个类型。Record 后面的泛型就是对象键和值的类型。</p>
<p>简单理解：K对应对应的key，T对应对象的value，返回的就是一个声明好的对象</p>
<pre><code class="hljs language-js copyable" lang="js">type TodoProperty = <span class="hljs-string">'title'</span> | <span class="hljs-string">'description'</span>;

type Todo = Record<TodoProperty, string>;
<span class="hljs-comment">// =</span>
type Todo = &#123;
    <span class="hljs-attr">title</span>: string;
    description: string;
&#125;

interface IGirl &#123;
  <span class="hljs-attr">name</span>: string;
  age: number;
&#125;

type allGirls = Record<string, IGirl>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-31">5、<code>Pick<T,K></code></h3>
<p>在一个声明好的对象中，挑选一部分出来组成一个新的声明对象</p>
<pre><code class="hljs language-js copyable" lang="js">interface Todo &#123;
  <span class="hljs-attr">title</span>: string;
  description: string;
  done: boolean;
&#125;

type TodoBase = Pick<Todo, <span class="hljs-string">"title"</span> | <span class="hljs-string">"done"</span>>;

<span class="hljs-comment">// =</span>
type TodoBase = &#123;
    <span class="hljs-attr">title</span>: string;
    done: boolean;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-32">6、<code>Omit<T,K></code></h3>
<p>从T中取出除去K的其他所有属性。与Pick相对。</p>
<h3 data-id="heading-33">7、<code>Exclude<T,U></code></h3>
<p>从T中排除可分配给U的属性，剩余的属性构成新的类型</p>
<pre><code class="hljs language-js copyable" lang="js">type T0 = Exclude<<span class="hljs-string">'a'</span> | <span class="hljs-string">'b'</span> | <span class="hljs-string">'c'</span>, <span class="hljs-string">'a'</span>>; 

<span class="hljs-comment">// = </span>

type T0 = <span class="hljs-string">"b"</span> | <span class="hljs-string">"c"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-34">8、<code>Extract<T,U></code></h3>
<p>从T中抽出可分配给U的属性构成新的类型。与Exclude相反</p>
<pre><code class="hljs language-js copyable" lang="js">type T0 = Exclude<<span class="hljs-string">'a'</span> | <span class="hljs-string">'b'</span> | <span class="hljs-string">'c'</span>, <span class="hljs-string">'a'</span>>; 

<span class="hljs-comment">// = </span>

type T0 = <span class="hljs-string">'a'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-35">9、<code>NonNullable<T></code></h3>
<p>去除T中的 null 和 undefined 类型</p>
<h3 data-id="heading-36">10、<code>Parameters<T></code></h3>
<p>返回类型为T的函数的参数类型所组成的数组</p>
<pre><code class="hljs language-js copyable" lang="js">
type T0 = Parameters<<span class="hljs-function">() =></span> string>;  <span class="hljs-comment">// []</span>

type T1 = Parameters<<span class="hljs-function">(<span class="hljs-params">s: string</span>) =></span> <span class="hljs-keyword">void</span>>;  <span class="hljs-comment">// [string]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-37">11、<code>ReturnType<T></code></h3>
<p>function T的返回类型</p>
<pre><code class="hljs language-js copyable" lang="js">type T0 = ReturnType<<span class="hljs-function">() =></span> string>;  <span class="hljs-comment">// string</span>

type T1 = ReturnType<<span class="hljs-function">(<span class="hljs-params">s: string</span>) =></span> <span class="hljs-keyword">void</span>>;  <span class="hljs-comment">// void</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-38">12、<code>InstanceType<T></code></h3>
<p>返回构造函数类型T的实例类型; 相当于js中的，不过返回的是对应的实例</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">C</span> </span>&#123;
  x = <span class="hljs-number">0</span>;
  y = <span class="hljs-number">0</span>;
&#125;

type T0 = InstanceType<<span class="hljs-keyword">typeof</span> C>;  <span class="hljs-comment">// C</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-39">七、ts学习资源</h2>
<ul>
<li><a href="https://www.bilibili.com/video/BV1qV41167VD" target="_blank" rel="nofollow noopener noreferrer">B站 技术胖ts入门视频</a> 胖哥新版ts教程</li>
<li><a href="https://www.bilibili.com/video/BV1Xy4y1v7S2" target="_blank" rel="nofollow noopener noreferrer">尚硅谷2021版TypeScript教程（李立超老师TS新课）</a> 还算比较新，喜欢视频学习的同学了解下</li>
<li><a href="https://typescript.bootcss.com/" target="_blank" rel="nofollow noopener noreferrer">TypeScript 中文手册</a> 比官网那个易读一些</li>
<li><a href="https://typescript.bootcss.com/tutorials/react.html" target="_blank" rel="nofollow noopener noreferrer">TypeScript与React结合</a> 快速上手指南</li>
<li><a href="https://juejin.cn/post/6872111128135073806" target="_blank">一份不可多得的 TS 学习指南（1.8W字）</a> 阿宝哥，ts大佬 <a href="https://github.com/semlinker" target="_blank" rel="nofollow noopener noreferrer">主页有很多ts教程</a></li>
<li><a href="https://jkchao.github.io/typescript-book-chinese/" target="_blank" rel="nofollow noopener noreferrer">深入理解 TypeScript</a> 讲的就比较深入了</li>
<li><a href="https://github.com/pipiliang/clean-code-typescript" target="_blank" rel="nofollow noopener noreferrer">TypeScript 代码整洁之道</a> 翻译国外大佬写的，国内大佬翻译的</li>
<li><a href="https://www.typescriptlang.org/play/" target="_blank" rel="nofollow noopener noreferrer">TypeScript Playground</a> TypeScript 官方提供的在线 TypeScript 运行环境</li>
<li><a href="http://json2ts.com/" target="_blank" rel="nofollow noopener noreferrer">json2ts</a> 将JSON转换成ts声明，应该好用，不过我们后端的接口文档自带了这个功能，我是用不上了。了解到有些类库可以直接根据数据表结构生成ts定义</li>
</ul>
<h2 data-id="heading-40">八、往期回顾</h2>
<ul>
<li><a href="https://juejin.cn/post/6960556335092269063" target="_blank">一名 vueCoder 总结的 React 基础</a> 180+ 👍🏿</li>
<li><a href="https://juejin.cn/post/6953482028188860424" target="_blank">Vue 转 React不完全指北</a> 600+ 👍🏿</li>
<li><a href="https://juejin.cn/post/6942988170208215076" target="_blank">跳槽人速来，面经&资源分享</a> 1100+ 👍🏿</li>
<li><a href="https://juejin.cn/post/6940058373534515237" target="_blank">一年半前端人的求职路</a> 300+ 👍🏿</li>
<li><a href="https://juejin.cn/post/6921911974611664903" target="_blank">vue2.x高阶问题，你能答多少</a> 400+ 👍🏿</li>
<li><a href="https://juejin.cn/post/6921911974611664903" target="_blank">聊一聊前端性能优化</a> 1300+ 👍🏿</li>
<li><a href="https://juejin.cn/post/6907500437134376974" target="_blank">Egg + Puppeteer 实现Html转PDF(已开源)</a> 50+ 👍🏿</li>
<li><a href="https://juejin.cn/post/6865957891988258823" target="_blank">web打印，一篇搞定</a> 15+ 👍🏿</li>
</ul>
<h2 data-id="heading-41">九、最后</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f54ccd795016409cb57c1a72aa28a75e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            