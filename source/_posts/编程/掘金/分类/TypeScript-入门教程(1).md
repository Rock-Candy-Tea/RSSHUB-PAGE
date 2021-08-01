
---
title: 'TypeScript-入门教程(1)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75c1b2cac1bd412cbda48c70e4cfa071~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 23:45:29 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75c1b2cac1bd412cbda48c70e4cfa071~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1.什么是typescript？</h3>
<p>typescript它是JavaScript的一个超集，扩展了 JavaScript 的语法，可以编译成javascript语法。</p>
<h3 data-id="heading-1">2.typescript的特点与优势</h3>
<p>JavaScript 代码可与 TypeScript 一起工作无需任何修改，TypeScript 通过类型注解提供编译时的静态类型检查。TypeScript 可处理已有的 JavaScript 代码，并只对其中的 TypeScript 代码进行编译。TypeScript 增加了代码的可读性和可维护性，可以在编译阶段就能发现错误，提高我们编程的效率。</p>
<h3 data-id="heading-2">3.typescript的安装</h3>
<p>Windows系统可以通过npm install typescript -g来安装typescript 包,mac系统的电脑使用 sudo npm install typescript -g安装，通过tsc index.ts来编译成javascript的文件</p>
<h3 data-id="heading-3">4.基本数据类型</h3>
<p>typescript 和 javascript的对于变量的申明是有差别的：</p>
<pre><code class="copyable">let isDone: boolean = false; //typescript申明方式
let isDone=true;             // js申明方式
我们会发现在变量的后面加了：boolean，这样做的目的就是限定这个变量只能为boolean类型的数据，
不可以是其他的，但是我们javascript就不会限定，你现在为 true，我也可以改变成Number 类型，string类型等等
下图我们可以看出js文件中申明变量a=true,a然后又等于“abcd”,最后打印出来的就是“abcd”,
但是同样的我们在ts文件中也是如此操作，但是却报错了“Type 'string' is not assignable to type 'boolean'”,意思就是类型“string”不可分配给类型“boolean”，也就是说boolean的变量改变，只能改变成为boolean类型的
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75c1b2cac1bd412cbda48c70e4cfa071~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d26e674c0f94b4e9f9a7b1cab3bc29c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>同样的我们申明字符串，数字<em>let name: string = "bob";let decLiteral: number = 6</em>;只能指定为字符串和数字类型，修改时也只能修改为对应类型的数据；但是这里要特别说明的是：数字类型的也可以设置为二进制和八进制字面量，例如：<em>let hexLiteral: number = 0xf00d; let binaryLiteral: number = 0b1010;</em></p>
</blockquote>
<blockquote>
<p><code>undefined</code>和<code>null</code>两者各自有自己的类型分别叫做<code>undefined</code>和<code>null</code>。他们本身类型用处不大，申明方式和和字符串，数字一样<em>let u: undefined = undefined; let n: null = null;</em></p>
<blockquote>
<p>注意：默认情况下<code>null</code>和<code>undefined</code>是所有类型的子类型。也就是说字符串，数字等类型的变量的值是可以为null/undefined 例如：let num:number=null/undefined;</p>
</blockquote>
</blockquote>
<h3 data-id="heading-4">5.数组类型</h3>
<p>TypeScript像JavaScript一样可以操作数组元素。 有两种方式可以定义数组：</p>
<p>let list: number[] = [1, 2, 3];---元素类型+<code>[]</code></p>
<p>let list: Array = [1, 2, 3];---使用数组泛型，<code>Array<元素类型></code></p>
<p>元素类型限制我们数组内部的元素只能是Number类型的</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/076b9570ea3e4a0ca9aab45743f03938~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
当Number类型的数组中出现字符串时会报错，同时我们运行时也会报错</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2172f7ee9ad4a008b7fb0f3e433750b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
意思就是类型“string”不可分配给类型“Number”</p>
<p><strong>那么我们如何我们如何让数组，或者变量能够为任何值，或者改变为任何值呢，亦或还不清楚类型的变量指定一个类型？</strong></p>
<h3 data-id="heading-5">any类型数据</h3>
<p>当我们不知道变量的数据类型是我们可以指定为any类型，同时any类型的数据可以赋值改变为任意其他类型的数据。
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c74dc0328aa64e1aaacba13fd47c7484~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
申明变量p1位any类型的，我们分别赋值，打印出来的结果分别为12，abc，true也就是说any类型的变量可以赋值为其他类型的变量</p>
<p>同样当我们把数组的元素类型设置为any的时候，那么数组里的元素可以为不同类型的元素</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb2f4c158e7448b38611f8e4697512fa~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">void类型数据</h3>
<p><code>void</code>类型像是与<code>any</code>类型相反，它表示没有任何类型。 当一个函数没有返回值时，你通常会见到其返回值类型是 <code>void</code>：</p>
<blockquote>
<p>function warnUser(): void &#123; console.log("This is my warning message"); &#125;</p>
</blockquote>
<p>而且声明一个<code>void</code>类型的变量没有什么大用，因为你只能为它赋予<code>undefined</code>和<code>null</code>；</p>
<h3 data-id="heading-7">类型推论</h3>
<p>如果没有明确的指定类型，那么 TypeScript 会依照类型推论（Type Inference）的规则推断出一个类型。</p>
<pre><code class="copyable">let myFavoriteNumber = 'seven';
myFavoriteNumber = 7;
这段代码中yFavoriteNumber这个变量虽然没有指定类型，但是在编译时依然会报错
Type 'number' is not assignable to type 'string'
事实上这段代码等价于
let myFavoriteNumber: string = 'seven';
myFavoriteNumber = 7;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>TypeScript 会在没有明确的指定类型的时候推测出一个类型，这就是类型推论。</em></p></div>  
</div>
            