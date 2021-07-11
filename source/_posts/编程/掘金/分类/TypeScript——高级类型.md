
---
title: 'TypeScript——高级类型'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9060'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 05:03:12 GMT
thumbnail: 'https://picsum.photos/400/300?random=9060'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>欢迎关注微信公众号：前端阅读室</p>
</blockquote>
<h1 data-id="heading-0">高级类型</h1>
<h2 data-id="heading-1">交叉类型（Intersection Types）</h2>
<p>交叉类型是将多个类型合并为一个类型。这让我们可以把现有的多种类型叠加到一起成为一种类型，它包含了所需的所有类型的特性。例如， Person & Serializable & Loggable同时是 Person 和 Serializable 和 Loggable。就是说这个类型的对象同时拥有了这三种类型的成员。</p>
<p>我们大多是在混入（mixins）或其它不适合典型面向对象模型的地方看到交叉类型的使用。 （在JavaScript里发生这种情况的场合很多！） 下面是如何创建混入的一个简单例子：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">extend</span><<span class="hljs-title">T</span>, <span class="hljs-title">U</span>>(<span class="hljs-params">first: T, second: U</span>): <span class="hljs-title">T</span> & <span class="hljs-title">U</span> </span>&#123;
    <span class="hljs-keyword">let</span> result = <T & U>&#123;&#125;;
    for (let id in first) &#123;
        (<any>result)[id] = (<any>first)[id];
    &#125;
    for (let id in second) &#123;
        if (!result.hasOwnProperty(id)) &#123;
            (<any>result)[id] = (<any>second)[id];
        &#125;
    &#125;
    return result;
&#125;

class Person &#123;
    constructor(public name: string) &#123; &#125;
&#125;
interface Loggable &#123;
    log(): void;
&#125;
class ConsoleLogger implements Loggable &#123;
    log() &#123;
        // ...
    &#125;
&#125;
var jim = extend(new Person("Jim"), new ConsoleLogger());
var n = jim.name;
jim.log();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">联合类型（Union Types）</h2>
<p>联合类型与交叉类型很有关联，但是使用上却完全不同。偶尔你会遇到这种情况，一个代码库希望传入 number或 string类型的参数。 例如下面的函数：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
 * Takes a string and adds "padding" to the left.
 * If 'padding' is a string, then 'padding' is appended to the left side.
 * If 'padding' is a number, then that number of spaces is added to the left side.
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">padLeft</span>(<span class="hljs-params">value: <span class="hljs-built_in">string</span>, padding: <span class="hljs-built_in">any</span></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> padding === <span class="hljs-string">"number"</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Array</span>(padding + <span class="hljs-number">1</span>).join(<span class="hljs-string">" "</span>) + value;
    &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> padding === <span class="hljs-string">"string"</span>) &#123;
        <span class="hljs-keyword">return</span> padding + value;
    &#125;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`Expected string or number, got '<span class="hljs-subst">$&#123;padding&#125;</span>'.`</span>);
&#125;

padLeft(<span class="hljs-string">"Hello world"</span>, <span class="hljs-number">4</span>); <span class="hljs-comment">// returns "    Hello world"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>padLeft存在一个问题， padding参数的类型指定成了 any。 这就是说我们可以传入一个既不是 number也不是 string类型的参数，但是TypeScript却不报错。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> indentedString = padLeft(<span class="hljs-string">"Hello world"</span>, <span class="hljs-literal">true</span>); <span class="hljs-comment">// 编译阶段通过，运行时报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在传统的面向对象语言里，我们可能会将这两种类型抽象成有层级的类型。 这么做显然是非常清晰的，但同时也存在了过度设计。 padLeft原始版本的好处之一是允许我们传入原始类型。 这样做的话使用起来既简单又方便。 如果我们就是想使用已经存在的函数的话，这种新的方式就不适用了。</p>
<p>代替 any， 我们可以使用 联合类型做为 padding的参数：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
 * Takes a string and adds "padding" to the left.
 * If 'padding' is a string, then 'padding' is appended to the left side.
 * If 'padding' is a number, then that number of spaces is added to the left side.
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">padLeft</span>(<span class="hljs-params">value: <span class="hljs-built_in">string</span>, padding: <span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span></span>) </span>&#123;
    <span class="hljs-comment">// ...</span>
&#125;

<span class="hljs-keyword">let</span> indentedString = padLeft(<span class="hljs-string">"Hello world"</span>, <span class="hljs-literal">true</span>); <span class="hljs-comment">// errors during compilation</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>联合类型表示一个值可以是几种类型之一。 我们用竖线（ |）分隔每个类型，所以 number | string | boolean表示一个值可以是 number， string，或 boolean。</p>
<p>如果一个值是联合类型，我们只能访问此联合类型的所有类型里共有的成员。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Bird &#123;
    fly();
    layEggs();
&#125;

<span class="hljs-keyword">interface</span> Fish &#123;
    swim();
    layEggs();
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getSmallPet</span>(<span class="hljs-params"></span>): <span class="hljs-title">Fish</span> | <span class="hljs-title">Bird</span> </span>&#123;
    <span class="hljs-comment">// ...</span>
&#125;

<span class="hljs-keyword">let</span> pet = getSmallPet();
pet.layEggs(); <span class="hljs-comment">// okay</span>
pet.swim();    <span class="hljs-comment">// errors</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的联合类型可能有点复杂，但是你很容易就习惯了。 如果一个值的类型是 A | B，我们能够 确定的是它包含了 A 和 B中共有的成员。 这个例子里， Bird具有一个 fly成员。 我们不能确定一个 Bird | Fish类型的变量是否有 fly方法。 如果变量在运行时是 Fish类型，那么调用 pet.fly()就出错了。</p>
<h2 data-id="heading-3">类型保护与区分类型（Type Guards and Differentiating Types）</h2>
<p>联合类型适合于那些值可以为不同类型的情况。 但当我们想确切地了解是否为 Fish时怎么办？ JavaScript里常用来区分2个可能值的方法是检查成员是否存在。 如之前提及的，我们只能访问联合类型中共同拥有的成员。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> pet = getSmallPet();

<span class="hljs-comment">// 每一个成员访问都会报错</span>
<span class="hljs-keyword">if</span> (pet.swim) &#123;
    pet.swim();
&#125;
<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (pet.fly) &#123;
    pet.fly();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了让这段代码工作，我们要使用类型断言：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> pet = getSmallPet();

<span class="hljs-keyword">if</span> ((<Fish>pet).swim) &#123;
    (<Fish>pet).swim();
&#125;
<span class="hljs-keyword">else</span> &#123;
    (<Bird>pet).fly();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">用户自定义的类型保护</h3>
<p>这里可以注意到我们不得不多次使用类型断言。 假若我们一旦检查过类型，就能在之后的每个分支里清楚地知道 pet的类型的话就好了。</p>
<p>TypeScript里的 类型保护机制让它成为了现实。 类型保护就是一些表达式，它们会在运行时检查以确保在某个作用域里的类型。 要定义一个类型保护，我们只要简单地定义一个函数，它的返回值是一个 类型谓词：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isFish</span>(<span class="hljs-params">pet: Fish | Bird</span>): <span class="hljs-title">pet</span> <span class="hljs-title">is</span> <span class="hljs-title">Fish</span> </span>&#123;
    <span class="hljs-keyword">return</span> (<Fish>pet).swim !== <span class="hljs-literal">undefined</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个例子里， pet is Fish就是类型谓词。 谓词为 parameterName is Type这种形式， parameterName必须是来自于当前函数签名里的一个参数名。</p>
<p>每当使用一些变量调用 isFish时，TypeScript会将变量缩减为那个具体的类型，只要这个类型与变量的原始类型是兼容的。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 'swim' 和 'fly' 调用都没有问题了</span>

<span class="hljs-keyword">if</span> (isFish(pet)) &#123;
    pet.swim();
&#125;
<span class="hljs-keyword">else</span> &#123;
    pet.fly();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意TypeScript不仅知道在 if分支里 pet是 Fish类型； 它还清楚在 else分支里，一定 不是 Fish类型，一定是 Bird类型。</p>
<h3 data-id="heading-5">typeof类型保护</h3>
<p>现在我们回过头来看看怎么使用联合类型书写 padLeft代码。 我们可以像下面这样利用类型断言来写：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isNumber</span>(<span class="hljs-params">x: <span class="hljs-built_in">any</span></span>): <span class="hljs-title">x</span> <span class="hljs-title">is</span> <span class="hljs-title">number</span> </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> x === <span class="hljs-string">"number"</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isString</span>(<span class="hljs-params">x: <span class="hljs-built_in">any</span></span>): <span class="hljs-title">x</span> <span class="hljs-title">is</span> <span class="hljs-title">string</span> </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> x === <span class="hljs-string">"string"</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">padLeft</span>(<span class="hljs-params">value: <span class="hljs-built_in">string</span>, padding: <span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (isNumber(padding)) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Array</span>(padding + <span class="hljs-number">1</span>).join(<span class="hljs-string">" "</span>) + value;
    &#125;
    <span class="hljs-keyword">if</span> (isString(padding)) &#123;
        <span class="hljs-keyword">return</span> padding + value;
    &#125;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`Expected string or number, got '<span class="hljs-subst">$&#123;padding&#125;</span>'.`</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然而，必须要定义一个函数来判断类型是否是原始类型，这太痛苦了。 幸运的是，现在我们不必将 typeof x === "number"抽象成一个函数，因为TypeScript可以将它识别为一个类型保护。 也就是说我们可以直接在代码里检查类型了。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">padLeft</span>(<span class="hljs-params">value: <span class="hljs-built_in">string</span>, padding: <span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> padding === <span class="hljs-string">"number"</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Array</span>(padding + <span class="hljs-number">1</span>).join(<span class="hljs-string">" "</span>) + value;
    &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> padding === <span class="hljs-string">"string"</span>) &#123;
        <span class="hljs-keyword">return</span> padding + value;
    &#125;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`Expected string or number, got '<span class="hljs-subst">$&#123;padding&#125;</span>'.`</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这些* typeof类型保护*只有两种形式能被识别： typeof v === "typename"和 typeof v !== "typename"， "typename"必须是 "number"， "string"， "boolean"或 "symbol"。 但是TypeScript并不会阻止你与其它字符串比较，语言不会把那些表达式识别为类型保护。</p>
<h3 data-id="heading-6">instanceof类型保护</h3>
<p>如果你已经阅读了 typeof类型保护并且对JavaScript里的 instanceof操作符熟悉的话，你可能已经猜到了这节要讲的内容。</p>
<p>instanceof类型保护是通过构造函数来细化类型的一种方式。 比如，我们借鉴一下之前字符串填充的例子：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Padder &#123;
    getPaddingString(): <span class="hljs-built_in">string</span>
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SpaceRepeatingPadder</span> <span class="hljs-title">implements</span> <span class="hljs-title">Padder</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">private</span> numSpaces: <span class="hljs-built_in">number</span></span>)</span> &#123; &#125;
    <span class="hljs-function"><span class="hljs-title">getPaddingString</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Array</span>(<span class="hljs-built_in">this</span>.numSpaces + <span class="hljs-number">1</span>).join(<span class="hljs-string">" "</span>);
    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">StringPadder</span> <span class="hljs-title">implements</span> <span class="hljs-title">Padder</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">private</span> value: <span class="hljs-built_in">string</span></span>)</span> &#123; &#125;
    <span class="hljs-function"><span class="hljs-title">getPaddingString</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.value;
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getRandomPadder</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.random() < <span class="hljs-number">0.5</span> ?
        <span class="hljs-keyword">new</span> SpaceRepeatingPadder(<span class="hljs-number">4</span>) :
        <span class="hljs-keyword">new</span> StringPadder(<span class="hljs-string">"  "</span>);
&#125;

<span class="hljs-comment">// 类型为SpaceRepeatingPadder | StringPadder</span>
<span class="hljs-keyword">let</span> padder: Padder = getRandomPadder();

<span class="hljs-keyword">if</span> (padder <span class="hljs-keyword">instanceof</span> SpaceRepeatingPadder) &#123;
    padder; <span class="hljs-comment">// 类型细化为'SpaceRepeatingPadder'</span>
&#125;
<span class="hljs-keyword">if</span> (padder <span class="hljs-keyword">instanceof</span> StringPadder) &#123;
    padder; <span class="hljs-comment">// 类型细化为'StringPadder'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>instanceof的右侧要求是一个构造函数，TypeScript将细化为：</p>
<ol>
<li>此构造函数的 prototype属性的类型，如果它的类型不为 any的话</li>
<li>构造签名所返回的类型的联合</li>
</ol>
<p>以此顺序。</p>
<h2 data-id="heading-7">可以为null的类型</h2>
<p>TypeScript具有两种特殊的类型， null和 undefined，它们分别具有值null和undefined. 我们在[基础类型](./Basic Types.md)一节里已经做过简要说明。 默认情况下，类型检查器认为 null与 undefined可以赋值给任何类型。 null与 undefined是所有其它类型的一个有效值。 这也意味着，你阻止不了将它们赋值给其它类型，就算是你想要阻止这种情况也不行。 null的发明者，Tony Hoare，称它为 价值亿万美金的错误。</p>
<p>--strictNullChecks标记可以解决此错误：当你声明一个变量时，它不会自动地包含 null或 undefined。 你可以使用联合类型明确的包含它们：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> s = <span class="hljs-string">"foo"</span>;
s = <span class="hljs-literal">null</span>; <span class="hljs-comment">// 错误, 'null'不能赋值给'string'</span>
<span class="hljs-keyword">let</span> sn: <span class="hljs-built_in">string</span> | <span class="hljs-literal">null</span> = <span class="hljs-string">"bar"</span>;
sn = <span class="hljs-literal">null</span>; <span class="hljs-comment">// 可以</span>

sn = <span class="hljs-literal">undefined</span>; <span class="hljs-comment">// error, 'undefined'不能赋值给'string | null'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，按照JavaScript的语义，TypeScript会把 null和 undefined区别对待。 string | null， string | undefined和 string | undefined | null是不同的类型。</p>
<h3 data-id="heading-8">可选参数和可选属性</h3>
<p>使用了 --strictNullChecks，可选参数会被自动地加上 | undefined:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params">x: <span class="hljs-built_in">number</span>, y?: <span class="hljs-built_in">number</span></span>) </span>&#123;
    <span class="hljs-keyword">return</span> x + (y || <span class="hljs-number">0</span>);
&#125;
f(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>);
f(<span class="hljs-number">1</span>);
f(<span class="hljs-number">1</span>, <span class="hljs-literal">undefined</span>);
f(<span class="hljs-number">1</span>, <span class="hljs-literal">null</span>); <span class="hljs-comment">// error, 'null' is not assignable to 'number | undefined'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可选属性也会有同样的处理：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">C</span> </span>&#123;
    <span class="hljs-attr">a</span>: <span class="hljs-built_in">number</span>;
    b?: <span class="hljs-built_in">number</span>;
&#125;
<span class="hljs-keyword">let</span> c = <span class="hljs-keyword">new</span> C();
c.a = <span class="hljs-number">12</span>;
c.a = <span class="hljs-literal">undefined</span>; <span class="hljs-comment">// error, 'undefined' is not assignable to 'number'</span>
c.b = <span class="hljs-number">13</span>;
c.b = <span class="hljs-literal">undefined</span>; <span class="hljs-comment">// ok</span>
c.b = <span class="hljs-literal">null</span>; <span class="hljs-comment">// error, 'null' is not assignable to 'number | undefined'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">类型保护和类型断言</h3>
<p>由于可以为null的类型是通过联合类型实现，那么你需要使用类型保护来去除 null。 幸运地是这与在JavaScript里写的代码一致：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params">sn: <span class="hljs-built_in">string</span> | <span class="hljs-literal">null</span></span>): <span class="hljs-title">string</span> </span>&#123;
    <span class="hljs-keyword">if</span> (sn == <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">"default"</span>;
    &#125;
    <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> sn;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里很明显地去除了 null，你也可以使用短路运算符：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params">sn: <span class="hljs-built_in">string</span> | <span class="hljs-literal">null</span></span>): <span class="hljs-title">string</span> </span>&#123;
    <span class="hljs-keyword">return</span> sn || <span class="hljs-string">"default"</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果编译器不能够去除 null或 undefined，你可以使用类型断言手动去除。 语法是添加 !后缀： identifier!从 identifier的类型里去除了 null和 undefined：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">broken</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span> | <span class="hljs-literal">null</span></span>): <span class="hljs-title">string</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">postfix</span>(<span class="hljs-params">epithet: <span class="hljs-built_in">string</span></span>) </span>&#123;
    <span class="hljs-keyword">return</span> name.charAt(<span class="hljs-number">0</span>) + <span class="hljs-string">'.  the '</span> + epithet; <span class="hljs-comment">// error, 'name' is possibly null</span>
  &#125;
  name = name || <span class="hljs-string">"Bob"</span>;
  <span class="hljs-keyword">return</span> postfix(<span class="hljs-string">"great"</span>);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fixed</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span> | <span class="hljs-literal">null</span></span>): <span class="hljs-title">string</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">postfix</span>(<span class="hljs-params">epithet: <span class="hljs-built_in">string</span></span>) </span>&#123;
    <span class="hljs-keyword">return</span> name!.charAt(<span class="hljs-number">0</span>) + <span class="hljs-string">'.  the '</span> + epithet; <span class="hljs-comment">// ok</span>
  &#125;
  name = name || <span class="hljs-string">"Bob"</span>;
  <span class="hljs-keyword">return</span> postfix(<span class="hljs-string">"great"</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>本例使用了嵌套函数，因为编译器无法去除嵌套函数的null（除非是立即调用的函数表达式）。 因为它无法跟踪所有对嵌套函数的调用，尤其是你将内层函数做为外层函数的返回值。 如果无法知道函数在哪里被调用，就无法知道调用时 name的类型。</p>
<h2 data-id="heading-10">类型别名</h2>
<p>类型别名会给一个类型起个新名字。 类型别名有时和接口很像，但是可以作用于原始值，联合类型，元组以及其它任何你需要手写的类型。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> Name = <span class="hljs-built_in">string</span>;
<span class="hljs-keyword">type</span> NameResolver = <span class="hljs-function">() =></span> <span class="hljs-built_in">string</span>;
<span class="hljs-keyword">type</span> NameOrResolver = Name | NameResolver;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getName</span>(<span class="hljs-params">n: NameOrResolver</span>): <span class="hljs-title">Name</span> </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> n === <span class="hljs-string">'string'</span>) &#123;
        <span class="hljs-keyword">return</span> n;
    &#125;
    <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> n();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>起别名不会新建一个类型 - 它创建了一个新 名字来引用那个类型。给原始类型起别名通常没什么用，尽管可以做为文档的一种形式使用。</p>
<p>同接口一样，类型别名也可以是泛型 - 我们可以添加类型参数并且在别名声明的右侧传入：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> Container<T> = &#123; <span class="hljs-attr">value</span>: T &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们也可以使用类型别名来在属性里引用自己：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> Tree<T> = &#123;
    <span class="hljs-attr">value</span>: T;
    left: Tree<T>;
    right: Tree<T>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>与交叉类型一起使用，我们可以创建出一些十分稀奇古怪的类型。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> LinkedList<T> = T & &#123; <span class="hljs-attr">next</span>: LinkedList<T> &#125;;

<span class="hljs-keyword">interface</span> Person &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
&#125;

<span class="hljs-keyword">var</span> people: LinkedList<Person>;
<span class="hljs-keyword">var</span> s = people.name;
<span class="hljs-keyword">var</span> s = people.next.name;
<span class="hljs-keyword">var</span> s = people.next.next.name;
<span class="hljs-keyword">var</span> s = people.next.next.next.name;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然而，类型别名不能出现在声明右侧的任何地方。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> Yikes = <span class="hljs-built_in">Array</span><Yikes>; <span class="hljs-comment">// error</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">接口 vs. 类型别名</h3>
<p>像我们提到的，类型别名可以像接口一样；然而，仍有一些细微差别。</p>
<p>其一，接口创建了一个新的名字，可以在其它任何地方使用。 类型别名并不创建新名字—比如，错误信息就不会使用别名。 在下面的示例代码里，在编译器中将鼠标悬停在 interfaced上，显示它返回的是 Interface，但悬停在 aliased上时，显示的却是对象字面量类型。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> Alias = &#123; <span class="hljs-attr">num</span>: <span class="hljs-built_in">number</span> &#125;
<span class="hljs-keyword">interface</span> Interface &#123;
    <span class="hljs-attr">num</span>: <span class="hljs-built_in">number</span>;
&#125;
<span class="hljs-keyword">declare</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">aliased</span>(<span class="hljs-params">arg: Alias</span>): <span class="hljs-title">Alias</span></span>;
<span class="hljs-keyword">declare</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">interfaced</span>(<span class="hljs-params">arg: Interface</span>): <span class="hljs-title">Interface</span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另一个重要区别是类型别名不能被 extends和 implements（自己也不能 extends和 implements其它类型）。 因为 软件中的对象应该对于扩展是开放的，但是对于修改是封闭的，你应该尽量去使用接口代替类型别名。</p>
<p>另一方面，如果你无法通过接口来描述一个类型并且需要使用联合类型或元组类型，这时通常会使用类型别名。</p>
<h2 data-id="heading-12">字符串字面量类型</h2>
<p>字符串字面量类型允许你指定字符串必须的固定值。 在实际应用中，字符串字面量类型可以与联合类型，类型保护和类型别名很好的配合。 通过结合使用这些特性，你可以实现类似枚举类型的字符串。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> Easing = <span class="hljs-string">"ease-in"</span> | <span class="hljs-string">"ease-out"</span> | <span class="hljs-string">"ease-in-out"</span>;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UIElement</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">animate</span>(<span class="hljs-params">dx: <span class="hljs-built_in">number</span>, dy: <span class="hljs-built_in">number</span>, easing: Easing</span>)</span> &#123;
        <span class="hljs-keyword">if</span> (easing === <span class="hljs-string">"ease-in"</span>) &#123;
            <span class="hljs-comment">// ...</span>
        &#125;
        <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (easing === <span class="hljs-string">"ease-out"</span>) &#123;
        &#125;
        <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (easing === <span class="hljs-string">"ease-in-out"</span>) &#123;
        &#125;
        <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// error! should not pass null or undefined.</span>
        &#125;
    &#125;
&#125;

<span class="hljs-keyword">let</span> button = <span class="hljs-keyword">new</span> UIElement();
button.animate(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-string">"ease-in"</span>);
button.animate(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-string">"uneasy"</span>); <span class="hljs-comment">// error: "uneasy" is not allowed here</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>字符串字面量类型还可以用于区分函数重载：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElement</span>(<span class="hljs-params">tagName: <span class="hljs-string">"img"</span></span>): <span class="hljs-title">HTMLImageElement</span></span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElement</span>(<span class="hljs-params">tagName: <span class="hljs-string">"input"</span></span>): <span class="hljs-title">HTMLInputElement</span></span>;
<span class="hljs-comment">// ... more overloads ...</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElement</span>(<span class="hljs-params">tagName: <span class="hljs-built_in">string</span></span>): <span class="hljs-title">Element</span> </span>&#123;
    <span class="hljs-comment">// ... code goes here ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">数字字面量类型</h2>
<p>TypeScript还具有数字字面量类型。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">rollDie</span>(<span class="hljs-params"></span>): 1 | 2 | 3 | 4 | 5 | 6 </span>&#123;
    <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们很少直接这样使用。</p>
<h2 data-id="heading-14">枚举成员类型</h2>
<p>如我们在 枚举一节里提到的，当每个枚举成员都是用字面量初始化的时候枚举成员是具有类型的。</p>
<p>在我们谈及“单例类型”的时候，多数是指枚举成员类型和数字/字符串字面量类型，尽管大多数用户会互换使用“单例类型”和“字面量类型”。</p>
<h2 data-id="heading-15">可辨识联合（Discriminated Unions）</h2>
<p>你可以合并单例类型，联合类型，类型保护和类型别名来创建一个叫做 可辨识联合的高级模式，它也称做 标签联合或 代数数据类型。 可辨识联合在函数式编程很有用处。 一些语言会自动地为你辨识联合；而TypeScript则基于已有的JavaScript模式。 它具有3个要素：</p>
<ol>
<li>具有普通的单例类型属性 — 可辨识的特征。</li>
<li>一个类型别名包含了那些类型的联合 — 联合。</li>
<li>此属性上的类型保护。</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Square &#123;
    <span class="hljs-attr">kind</span>: <span class="hljs-string">"square"</span>;
    size: <span class="hljs-built_in">number</span>;
&#125;
<span class="hljs-keyword">interface</span> Rectangle &#123;
    <span class="hljs-attr">kind</span>: <span class="hljs-string">"rectangle"</span>;
    width: <span class="hljs-built_in">number</span>;
    height: <span class="hljs-built_in">number</span>;
&#125;
<span class="hljs-keyword">interface</span> Circle &#123;
    <span class="hljs-attr">kind</span>: <span class="hljs-string">"circle"</span>;
    radius: <span class="hljs-built_in">number</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先我们声明了将要联合的接口。 每个接口都有 kind属性但有不同的字符串字面量类型。 kind属性称做 可辨识的特征或 标签。 其它的属性则特定于各个接口。 注意，目前各个接口间是没有联系的。 下面我们把它们联合到一起：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> Shape = Square | Rectangle | Circle;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们使用可辨识联合:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">area</span>(<span class="hljs-params">s: Shape</span>) </span>&#123;
    <span class="hljs-keyword">switch</span> (s.kind) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"square"</span>: <span class="hljs-keyword">return</span> s.size * s.size;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"rectangle"</span>: <span class="hljs-keyword">return</span> s.height * s.width;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"circle"</span>: <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.PI * s.radius ** <span class="hljs-number">2</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">完整性检查</h3>
<p>当没有涵盖所有可辨识联合的变化时，我们想让编译器可以通知我们。 比如，如果我们添加了 Triangle到 Shape，我们同时还需要更新 area:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> Shape = Square | Rectangle | Circle | Triangle;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">area</span>(<span class="hljs-params">s: Shape</span>) </span>&#123;
    <span class="hljs-keyword">switch</span> (s.kind) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"square"</span>: <span class="hljs-keyword">return</span> s.size * s.size;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"rectangle"</span>: <span class="hljs-keyword">return</span> s.height * s.width;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"circle"</span>: <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.PI * s.radius ** <span class="hljs-number">2</span>;
    &#125;
    <span class="hljs-comment">// should error here - we didn't handle case "triangle"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有两种方式可以实现。 首先是启用 --strictNullChecks并且指定一个返回值类型：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">area</span>(<span class="hljs-params">s: Shape</span>): <span class="hljs-title">number</span> </span>&#123; <span class="hljs-comment">// error: returns number | undefined</span>
    <span class="hljs-keyword">switch</span> (s.kind) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"square"</span>: <span class="hljs-keyword">return</span> s.size * s.size;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"rectangle"</span>: <span class="hljs-keyword">return</span> s.height * s.width;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"circle"</span>: <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.PI * s.radius ** <span class="hljs-number">2</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为 switch没有包涵所有情况，所以TypeScript认为这个函数有时候会返回 undefined。 如果你明确地指定了返回值类型为 number，那么你会看到一个错误，因为实际上返回值的类型为 number | undefined。 然而，这种方法存在些微妙之处且 --strictNullChecks对旧代码支持不好。</p>
<p>第二种方法使用 never类型，编译器用它来进行完整性检查：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">assertNever</span>(<span class="hljs-params">x: <span class="hljs-built_in">never</span></span>): <span class="hljs-title">never</span> </span>&#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"Unexpected object: "</span> + x);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">area</span>(<span class="hljs-params">s: Shape</span>) </span>&#123;
    <span class="hljs-keyword">switch</span> (s.kind) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"square"</span>: <span class="hljs-keyword">return</span> s.size * s.size;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"rectangle"</span>: <span class="hljs-keyword">return</span> s.height * s.width;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"circle"</span>: <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.PI * s.radius ** <span class="hljs-number">2</span>;
        <span class="hljs-keyword">default</span>: <span class="hljs-keyword">return</span> assertNever(s); <span class="hljs-comment">// error here if there are missing cases</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里， assertNever检查 s是否为 never类型—即为除去所有可能情况后剩下的类型。如果你忘记了某个case，那么 s将具有一个真实的类型并且你会得到一个错误。 这种方式需要你定义一个额外的函数，但是在你忘记某个case的时候也更加明显。</p>
<h2 data-id="heading-17">多态的 this类型</h2>
<p>多态的 this类型表示的是某个包含类或接口的 子类型。 这被称做 F-bounded多态性。 它能很容易的表现连贯接口间的继承，比如。 在计算器的例子里，在每个操作之后都返回 this类型：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BasicCalculator</span> </span>&#123;
    <span class="hljs-keyword">public</span> <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">protected</span> value: <span class="hljs-built_in">number</span> = <span class="hljs-number">0</span></span>)</span> &#123; &#125;
    <span class="hljs-keyword">public</span> currentValue(): <span class="hljs-built_in">number</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.value;
    &#125;
    <span class="hljs-keyword">public</span> add(operand: <span class="hljs-built_in">number</span>): <span class="hljs-built_in">this</span> &#123;
        <span class="hljs-built_in">this</span>.value += operand;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
    &#125;
    <span class="hljs-keyword">public</span> multiply(operand: <span class="hljs-built_in">number</span>): <span class="hljs-built_in">this</span> &#123;
        <span class="hljs-built_in">this</span>.value *= operand;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
    &#125;
    <span class="hljs-comment">// ... other operations go here ...</span>
&#125;

<span class="hljs-keyword">let</span> v = <span class="hljs-keyword">new</span> BasicCalculator(<span class="hljs-number">2</span>)
            .multiply(<span class="hljs-number">5</span>)
            .add(<span class="hljs-number">1</span>)
            .currentValue();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于这个类使用了 this类型，你可以继承它，新的类可以直接使用之前的方法，不需要做任何的改变。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ScientificCalculator</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">BasicCalculator</span> </span>&#123;
    <span class="hljs-keyword">public</span> <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">value = <span class="hljs-number">0</span></span>)</span> &#123;
        <span class="hljs-built_in">super</span>(value);
    &#125;
    <span class="hljs-keyword">public</span> <span class="hljs-function"><span class="hljs-title">sin</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.value = <span class="hljs-built_in">Math</span>.sin(<span class="hljs-built_in">this</span>.value);
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
    &#125;
    <span class="hljs-comment">// ... other operations go here ...</span>
&#125;

<span class="hljs-keyword">let</span> v = <span class="hljs-keyword">new</span> ScientificCalculator(<span class="hljs-number">2</span>)
        .multiply(<span class="hljs-number">5</span>)
        .sin()
        .add(<span class="hljs-number">1</span>)
        .currentValue();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果没有 this类型， ScientificCalculator就不能够在继承 BasicCalculator的同时还保持接口的连贯性。 multiply将会返回 BasicCalculator，它并没有 sin方法。 然而，使用 this类型， multiply会返回 this，在这里就是 ScientificCalculator。</p>
<h2 data-id="heading-18">索引类型（Index types）</h2>
<p>使用索引类型，编译器就能够检查使用了动态属性名的代码。 例如，一个常见的JavaScript模式是从对象中选取属性的子集。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pluck</span>(<span class="hljs-params">o, names</span>) </span>&#123;
    <span class="hljs-keyword">return</span> names.map(<span class="hljs-function"><span class="hljs-params">n</span> =></span> o[n]);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面是如何在TypeScript里使用此函数，通过 索引类型查询和 索引访问操作符：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pluck</span><<span class="hljs-title">T</span>, <span class="hljs-title">K</span> <span class="hljs-title">extends</span> <span class="hljs-title">keyof</span> <span class="hljs-title">T</span>>(<span class="hljs-params">o: T, names: K[]</span>): <span class="hljs-title">T</span>[<span class="hljs-title">K</span>][] </span>&#123;
  <span class="hljs-keyword">return</span> names.map(<span class="hljs-function"><span class="hljs-params">n</span> =></span> o[n]);
&#125;

<span class="hljs-keyword">interface</span> Person &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
    age: <span class="hljs-built_in">number</span>;
&#125;
<span class="hljs-keyword">let</span> person: Person = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'Jarid'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">35</span>
&#125;;
<span class="hljs-keyword">let</span> strings: <span class="hljs-built_in">string</span>[] = pluck(person, [<span class="hljs-string">'name'</span>]); <span class="hljs-comment">// ok, string[]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译器会检查 name是否真的是 Person的一个属性。 本例还引入了几个新的类型操作符。 首先是 keyof T， 索引类型查询操作符。 对于任何类型 T， keyof T的结果为 T上已知的公共属性名的联合。 例如：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> personProps: keyof Person; <span class="hljs-comment">// 'name' | 'age'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>keyof Person是完全可以与 'name' | 'age'互相替换的。 不同的是如果你添加了其它的属性到 Person，例如 address: string，那么 keyof Person会自动变为 'name' | 'age' | 'address'。 你可以在像 pluck函数这类上下文里使用 keyof，因为在使用之前你并不清楚可能出现的属性名。 但编译器会检查你是否传入了正确的属性名给 pluck：</p>
<pre><code class="hljs language-ts copyable" lang="ts">pluck(person, [<span class="hljs-string">'age'</span>, <span class="hljs-string">'unknown'</span>]); <span class="hljs-comment">// error, 'unknown' is not in 'name' | 'age'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二个操作符是 T[K]， 索引访问操作符。 在这里，类型语法反映了表达式语法。 这意味着 person['name']具有类型 Person['name'] — 在我们的例子里则为 string类型。 然而，就像索引类型查询一样，你可以在普通的上下文里使用 T[K]，这正是它的强大所在。 你只要确保类型变量 K extends keyof T就可以了。 例如下面 getProperty函数的例子：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getProperty</span><<span class="hljs-title">T</span>, <span class="hljs-title">K</span> <span class="hljs-title">extends</span> <span class="hljs-title">keyof</span> <span class="hljs-title">T</span>>(<span class="hljs-params">o: T, name: K</span>): <span class="hljs-title">T</span>[<span class="hljs-title">K</span>] </span>&#123;
    <span class="hljs-keyword">return</span> o[name]; <span class="hljs-comment">// o[name] is of type T[K]</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>getProperty里的 o: T和 name: K，意味着 o[name]: T[K]。 当你返回 T[K]的结果，编译器会实例化键的真实类型，因此 getProperty的返回值类型会随着你需要的属性改变。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> name: <span class="hljs-built_in">string</span> = getProperty(person, <span class="hljs-string">'name'</span>);
<span class="hljs-keyword">let</span> age: <span class="hljs-built_in">number</span> = getProperty(person, <span class="hljs-string">'age'</span>);
<span class="hljs-keyword">let</span> unknown = getProperty(person, <span class="hljs-string">'unknown'</span>); <span class="hljs-comment">// error, 'unknown' is not in 'name' | 'age'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">索引类型和字符串索引签名</h3>
<p>keyof和 T[K]与字符串索引签名进行交互。 如果你有一个带有字符串索引签名的类型，那么 keyof T会是 string。 并且 T[string]为索引签名的类型：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Map<T> &#123;
    [key: <span class="hljs-built_in">string</span>]: T;
&#125;
<span class="hljs-keyword">let</span> keys: keyof <span class="hljs-built_in">Map</span><<span class="hljs-built_in">number</span>>; <span class="hljs-comment">// string</span>
<span class="hljs-keyword">let</span> value: <span class="hljs-built_in">Map</span><<span class="hljs-built_in">number</span>>[<span class="hljs-string">'foo'</span>]; <span class="hljs-comment">// number</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">映射类型</h2>
<p>一个常见的任务是将一个已知的类型每个属性都变为可选的：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> PersonPartial &#123;
    name?: <span class="hljs-built_in">string</span>;
    age?: <span class="hljs-built_in">number</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者我们想要一个只读版本：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> PersonReadonly &#123;
    <span class="hljs-keyword">readonly</span> name: <span class="hljs-built_in">string</span>;
    <span class="hljs-keyword">readonly</span> age: <span class="hljs-built_in">number</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这在JavaScript里经常出现，TypeScript提供了从旧类型中创建新类型的一种方式 — 映射类型。 在映射类型里，新类型以相同的形式去转换旧类型里每个属性。 例如，你可以令每个属性成为 readonly类型或可选的。 下面是一些例子：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> Readonly<T> = &#123;
  <span class="hljs-keyword">readonly</span> [P <span class="hljs-keyword">in</span> keyof T]: T[P];
&#125;;
<span class="hljs-keyword">type</span> Partial<T> = &#123;
  [P <span class="hljs-keyword">in</span> keyof T]?: T[P];
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面来看看最简单的映射类型和它的组成部分：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> Keys = <span class="hljs-string">'option1'</span> | <span class="hljs-string">'option2'</span>;
<span class="hljs-keyword">type</span> Flags = &#123; [K <span class="hljs-keyword">in</span> Keys]: <span class="hljs-built_in">boolean</span> &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它的语法与索引签名的语法类型，内部使用了 for .. in。 具有三个部分：</p>
<ol>
<li>类型变量 K，它会依次绑定到每个属性。</li>
<li>字符串字面量联合的 Keys，它包含了要迭代的属性名的集合。</li>
<li>属性的结果类型。</li>
</ol>
<p>在个简单的例子里， Keys是硬编码的的属性名列表并且属性类型永远是 boolean，因此这个映射类型等同于：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> Flags = &#123;
    <span class="hljs-attr">option1</span>: <span class="hljs-built_in">boolean</span>;
    option2: <span class="hljs-built_in">boolean</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在真正的应用里，可能不同于上面的 Readonly或 Partial。 它们会基于一些已存在的类型，且按照一定的方式转换字段。 这就是 keyof和索引访问类型要做的事情：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> NullablePerson = &#123; [P <span class="hljs-keyword">in</span> keyof Person]: Person[P] | <span class="hljs-literal">null</span> &#125;
<span class="hljs-keyword">type</span> PartialPerson = &#123; [P <span class="hljs-keyword">in</span> keyof Person]?: Person[P] &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但它更有用的地方是可以有一些通用版本。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> Nullable<T> = &#123; [P <span class="hljs-keyword">in</span> keyof T]: T[P] | <span class="hljs-literal">null</span> &#125;
<span class="hljs-keyword">type</span> Partial<T> = &#123; [P <span class="hljs-keyword">in</span> keyof T]?: T[P] &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这些例子里，属性列表是 keyof T且结果类型是 <code>T[P]</code>的变体。 这是使用通用映射类型的一个好模版。 因为这类转换是 同态的，映射只作用于 T的属性而没有其它的。 编译器知道在添加任何新属性之前可以拷贝所有存在的属性修饰符。 例如，假设 Person.name是只读的，那么 <code>Partial<Person>.name</code>也将是只读的且为可选的。</p>
<p>下面是另一个例子， <code>T[P]</code>被包装在 <code>Proxy<T></code>类里：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> <span class="hljs-built_in">Proxy</span><T> = &#123;
    get(): T;
    set(value: T): <span class="hljs-built_in">void</span>;
&#125;
<span class="hljs-keyword">type</span> Proxify<T> = &#123;
    [P <span class="hljs-keyword">in</span> keyof T]: <span class="hljs-built_in">Proxy</span><T[P]>;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">proxify</span><<span class="hljs-title">T</span>>(<span class="hljs-params">o: T</span>): <span class="hljs-title">Proxify</span><<span class="hljs-title">T</span>> </span>&#123;
   <span class="hljs-comment">// ... wrap proxies ...</span>
&#125;
<span class="hljs-keyword">let</span> proxyProps = proxify(props);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意 <code>Readonly<T></code>和 <code>Partial<T></code>用处不小，因此它们与 Pick和 Record一同被包含进了TypeScript的标准库里：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> Pick<T, K <span class="hljs-keyword">extends</span> keyof T> = &#123;
    [P <span class="hljs-keyword">in</span> K]: T[P];
&#125;
<span class="hljs-keyword">type</span> Record<K <span class="hljs-keyword">extends</span> <span class="hljs-built_in">string</span>, T> = &#123;
    [P <span class="hljs-keyword">in</span> K]: T;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Readonly， Partial和 Pick是同态的，但 Record不是。 因为 Record并不需要输入类型来拷贝属性，所以它不属于同态：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> ThreeStringProps = Record<<span class="hljs-string">'prop1'</span> | <span class="hljs-string">'prop2'</span> | <span class="hljs-string">'prop3'</span>, <span class="hljs-built_in">string</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>非同态类型本质上会创建新的属性，因此它们不会从它处拷贝属性修饰符。</p>
<h3 data-id="heading-21">由映射类型进行推断</h3>
<p>现在你了解了如何包装一个类型的属性，那么接下来就是如何拆包。其实这也非常容易：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unproxify</span><<span class="hljs-title">T</span>>(<span class="hljs-params">t: Proxify<T></span>): <span class="hljs-title">T</span> </span>&#123;
    <span class="hljs-keyword">let</span> result = &#123;&#125; <span class="hljs-keyword">as</span> T;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> k <span class="hljs-keyword">in</span> t) &#123;
        result[k] = t[k].get();
    &#125;
    <span class="hljs-keyword">return</span> result;
&#125;

<span class="hljs-keyword">let</span> originalProps = unproxify(proxyProps);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意这个拆包推断只适用于同态的映射类型。 如果映射类型不是同态的，那么需要给拆包函数一个明确的类型参数。</p>
<h3 data-id="heading-22">预定义的有条件类型</h3>
<p>TypeScript 2.8在lib.d.ts里增加了一些预定义的有条件类型：</p>
<ul>
<li><code>Exclude<T, U></code> -- 从T中剔除可以赋值给U的类型。</li>
<li><code>Extract<T, U></code> -- 提取T中可以赋值给U的类型。</li>
<li><code>NonNullable<T></code> -- 从T中剔除null和undefined。</li>
<li><code>ReturnType<T></code> -- 获取函数返回值类型。</li>
<li><code>InstanceType<T></code> -- 获取构造函数类型的实例类型。</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> T00 = Exclude<<span class="hljs-string">"a"</span> | <span class="hljs-string">"b"</span> | <span class="hljs-string">"c"</span> | <span class="hljs-string">"d"</span>, <span class="hljs-string">"a"</span> | <span class="hljs-string">"c"</span> | <span class="hljs-string">"f"</span>>;  <span class="hljs-comment">// "b" | "d"</span>
<span class="hljs-keyword">type</span> T01 = Extract<<span class="hljs-string">"a"</span> | <span class="hljs-string">"b"</span> | <span class="hljs-string">"c"</span> | <span class="hljs-string">"d"</span>, <span class="hljs-string">"a"</span> | <span class="hljs-string">"c"</span> | <span class="hljs-string">"f"</span>>;  <span class="hljs-comment">// "a" | "c"</span>

<span class="hljs-keyword">type</span> T02 = Exclude<<span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span> | (<span class="hljs-function">() =></span> <span class="hljs-built_in">void</span>), <span class="hljs-built_in">Function</span>>;  <span class="hljs-comment">// string | number</span>
<span class="hljs-keyword">type</span> T03 = Extract<<span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span> | (<span class="hljs-function">() =></span> <span class="hljs-built_in">void</span>), <span class="hljs-built_in">Function</span>>;  <span class="hljs-comment">// () => void</span>

<span class="hljs-keyword">type</span> T04 = NonNullable<<span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span> | <span class="hljs-literal">undefined</span>>;  <span class="hljs-comment">// string | number</span>
<span class="hljs-keyword">type</span> T05 = NonNullable<(<span class="hljs-function">() =></span> <span class="hljs-built_in">string</span>) | <span class="hljs-built_in">string</span>[] | <span class="hljs-literal">null</span> | <span class="hljs-literal">undefined</span>>;  <span class="hljs-comment">// (() => string) | string[]</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f1</span>(<span class="hljs-params">s: <span class="hljs-built_in">string</span></span>) </span>&#123;
    <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">b</span>: s &#125;;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">C</span> </span>&#123;
    x = <span class="hljs-number">0</span>;
    y = <span class="hljs-number">0</span>;
&#125;

<span class="hljs-keyword">type</span> T10 = ReturnType<<span class="hljs-function">() =></span> <span class="hljs-built_in">string</span>>;  <span class="hljs-comment">// string</span>
<span class="hljs-keyword">type</span> T11 = ReturnType<<span class="hljs-function">(<span class="hljs-params">s: <span class="hljs-built_in">string</span></span>) =></span> <span class="hljs-built_in">void</span>>;  <span class="hljs-comment">// void</span>
<span class="hljs-keyword">type</span> T12 = ReturnType<(<T><span class="hljs-function">() =></span> T)>;  <span class="hljs-comment">// &#123;&#125;</span>
<span class="hljs-keyword">type</span> T13 = ReturnType<(<T extends U, U extends number[]>() => T)>;  // number[]
type T14 = ReturnType<typeof f1>;  // &#123; a: number, b: string &#125;
type T15 = ReturnType<any>;  // any
type T16 = ReturnType<never>;  // any
type T17 = ReturnType<string>;  // Error
type T18 = ReturnType<Function>;  // Error

type T20 = InstanceType<typeof C>;  // C
type T21 = InstanceType<any>;  // any
type T22 = InstanceType<never>;  // any
type T23 = InstanceType<string>;  // Error
type T24 = InstanceType<Function>;  // Error
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：Exclude类型是建议的Diff类型的一种实现。我们使用Exclude这个名字是为了避免破坏已经定义了Diff的代码，并且我们感觉这个名字能更好地表达类型的语义。我们没有增加<code>Omit<T, K></code>类型，因为它可以很容易的用<code>Pick<T, Exclude<keyof T, K>></code>来表示。</p>
<blockquote>
<p>欢迎关注微信公众号：前端阅读室</p>
</blockquote></div>  
</div>
            