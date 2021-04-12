
---
title: 'TypeScript趁早学习提高职场竞争力'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00ff65c5b18347718b845d657d204652~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 11 Apr 2021 16:00:34 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00ff65c5b18347718b845d657d204652~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://github.com/webVueBlog/WebFamily" target="_blank" rel="nofollow noopener noreferrer">Github来源：</a> | 求星星 ✨ | 给个❤️关注，❤️点赞，❤️鼓励一下作者</p>
<h2 data-id="heading-0">前言</h2>
<p>希望可以通过这篇文章，能够给你得到帮助。(感谢一键三连)</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00ff65c5b18347718b845d657d204652~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">还不抓紧学TypeScript</h3>
<p>TS：以JavaScript为基础构建的语言；可以在如何支持JavaScript的平台中执行；一个JavaScript的超集，TypeScript扩展了JavaScript，并添加了类型；TS不能被JS解析器直接执行。</p>
<p>TypeScript增加了一些类型，支持ES的新特性，添加ES不具备的新特性，丰富的配置选项，强大的开发工具。</p>
<p>学习TS，记得下载Node.js哦~</p>
<p>使用npm全局安装typescript，进入命令行，输入：<code>npm i -g typescript</code>，创建一个ts文件，使用tsc对ts文件进行编译：进入命令行，进入ts文件所在目录，执行命令：<code>tsc xxx.ts</code>。</p>
<p>基本类型：</p>
<p>类型声明：</p>
<ul>
<li>类型声明是TS非常重要的一个特点</li>
<li>通过类型声明可以指定TS中变量的类型</li>
<li>指定类型后，当位变量赋值时，TS编译器会自动检查是否符合类型声明，符合则赋值，否则报错</li>
<li>简而言之，类型声明给变量设置了类型，使得变量只能存储某种类型的值</li>
</ul>
<p>语法：</p>
<pre><code class="copyable">let 变量: 类型;
let 变量: 类型 = 值；
function fn(参数: 类型， 参数: 类型）:类型 &#123;
...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>自动类型判断：</p>
<ul>
<li>TS拥有自动的类型判断机制</li>
<li>当对变量的声明和赋值是同时进行的，TS编译器会自动判断变量的类型</li>
<li>所以如果你的变量的声明和赋值时同时进行的，可以省略掉类型声明</li>
</ul>

























































<table><thead><tr><th>类型</th><th>描述</th></tr></thead><tbody><tr><td>number</td><td>任意数字</td></tr><tr><td>string</td><td>任意字符串</td></tr><tr><td>boolean</td><td>布尔值true或false</td></tr><tr><td>字面量</td><td>限制变量的值就是该字面量的值</td></tr><tr><td>any</td><td>任意类型</td></tr><tr><td>unknown</td><td>类型安全的any</td></tr><tr><td>void</td><td>没有值或undefined</td></tr><tr><td>never</td><td>没有值  不能是任何值</td></tr><tr><td>object</td><td>任意的JS对象</td></tr><tr><td>array</td><td>任意JS数组</td></tr><tr><td>tuple</td><td>元素，TS新增类型，固定长度数组</td></tr><tr><td>enum</td><td>枚举，TS中新增类型</td></tr></tbody></table>
<ul>
<li>number</li>
</ul>
<pre><code class="copyable">let decimal: number = 6;
let hex: number = 0xf00d;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>boolean</li>
</ul>
<pre><code class="copyable">let isDone: boolean = false;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>string</li>
</ul>
<pre><code class="copyable">let color: striing = "blue"'
color = "red";
let fullName: string = "jeskson";
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>字面量</li>
</ul>
<pre><code class="copyable">let color: 'red' | 'blue' | 'black';
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>any</li>
</ul>
<pre><code class="copyable">let d: any = 3;
d = 'jeskson';
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>unknown</li>
</ul>
<pre><code class="copyable">let notSure: unknown = 4;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>void</li>
</ul>
<pre><code class="copyable">let unusable: void = undefined;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>never</li>
</ul>
<pre><code class="copyable">function error(message: string): never &#123;
 throw new Error(message);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>object</li>
</ul>
<pre><code class="copyable">let obj: object = &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>array</li>
</ul>
<pre><code class="copyable">let list: number[] = [1,2,3];
let list: Array<number> = [1,2,3];
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>tuple</li>
</ul>
<pre><code class="copyable">let x: [string, number];
x = ["hello", 10];
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>类型断言</li>
</ul>
<p>有些情况下，变量的类型对于我们来说是很明确的，但是TS编译器却并不清楚，此时，可以通过类型断言来告诉编译器变量的类型，断言有两种形式：</p>
<ul>
<li>第一种：</li>
</ul>
<pre><code class="copyable">let someValue: unknown = "jeskson 1024bibi.com";
let strlength: number = (someValue as string).length;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>第二种：</li>
</ul>
<pre><code class="copyable">let someValue: unknown = "1024bibi.com";
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">编译选项</h3>
<ul>
<li>自动编译文件</li>
</ul>
<p>编译文件时，使用<code>-w</code>指令后，TS编译器会自动监视文件的变化，并在文件发生变化时对文件进行重新编译。</p>
<pre><code class="copyable">tsc xxx.ts -w
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>自动编译整个项目：</li>
</ul>
<p>如果直接使用tsc指令，则可以自动将当前项目下的所有ts文件编译为js文件。</p>
<p>但是能直接使用tsc命令的前提时，要先在项目根目录下创建一个ts的配置文件<code>tsconfig.json</code>。</p>
<p><code>tsconfig.json</code>是一个<code>JSON</code>文件，添加配置文件后，只需<code>tsc</code>命令即可完成对整个项目的编译。</p>
<p>配置选项：</p>
<p><code>include</code>: 定义希望被编译文件所在的目录</p>
<pre><code class="copyable">// tsconfig.json
&#123;
 "include": [
  "./src/**/*"
 ]
&#125;
// ** 任意目录
// * 任意文件
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所有src目录和tests目录下的文件都会被编译</p>
<pre><code class="copyable">"include": ["src/**/*", "tests/**/*"]
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>exclude</li>
</ul>
<p>定义需要排除在外的目录；默认值<code>["node_modules","bower_components","jspm_package"]</code></p>
<pre><code class="copyable">"exclude": ["./src/hello/**/*"]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>src下hello目录下的文件都不会被编译</p>
<ul>
<li>extends：定义被继承的配置文件</li>
</ul>
<pre><code class="copyable">"extends": "./configs/base"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当前配置文件中会自动包含config目录下base.json中的所有配置信息</p>
<ul>
<li>files</li>
</ul>
<p>指定被编译的列表，只有需要编译的文件少时才会用到</p>
<p>示例：</p>
<pre><code class="copyable">"files": [
 "type.ts",
 "dada.ts"
]
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>compilerOptions</li>
</ul>
<p>编译选项是配置文件中非常重要也比较复杂的配置选项</p>
<p>在compilerOptions中包含多个子选项，用来完成对编译的配置</p>
<p>项目选项：target</p>
<p>设置ts代码编译的目标版本</p>
<p>示例：</p>
<pre><code class="copyable">"compilerOptions": &#123;
 "target": "ES6"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上设置，我们所编写的ts代码将会被编译为ES6版本的js代码</p>
<ul>
<li>lib</li>
</ul>
<p>指定代码运行时所包含的库</p>
<pre><code class="copyable">"compilerOptions": &#123;
 "target": "ES6",
 "lib": ["ES6", "DOM"],
 "outDir": "dist",
 "outFile": "dist/aa.js"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">module</h3>
<p>设置编译后代码使用的模块化系统</p>
<pre><code class="copyable">// 配置
// 当有错误时不生成编译后的文件
"noEmitOnError": true,
// 用来设置编译后的文件是否使用严格模式
"alwayStrict": true,
// 不允许隐式的any类型
"noImplicitAny": true,
// 不允许不明确类型的this
"noImplicitThis": true,
// 严格的检查空值
"strictNullChecks": true
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">使用webpack打包代码</h3>
<p>使用命令：<code>npm init -y</code></p>
<p>使用：<code>cnpm i -D webpack webpack-cli typescript ts-loader</code></p>
<pre><code class="copyable">// webpack.config.js
// 引入一个包
const path = require('path');

// webpack中的所有的配置信息都应该写在module.exports中
module.exports = &#123;
 // 指定入口文件
 entry: "./src/index.ts",
 // 指定打包文件所在目录
 output: &#123;
  // 指定打包文件的目录
  path: path.resolve(__dirname, 'dist'),
  // 打包后文件
  filename: "bundle.js"
 &#125;,
 
 // 指定webpack打包时要使用模块
 module: &#123;
  // 指定要加载的规则
  rules: [
   &#123;
    // test指定的是规则生效的文件
    test: /\.ts$/,
    // 要使用的Loader
    use: 'ts-loader',
    // 要排除的文件
    exclude: /node-modules/
   &#125;
  ]
 &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// tsconfig.json
&#123;
 "compilerOptions": &#123;
  "module": "ES2015",
  "target": "ES2015",
  "strict" true
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// package.json

"scripts": &#123;
 ...
 "bulid": "webpack"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用命令行：<code>npm run build</code></p>
<h3 data-id="heading-5">webpack</h3>
<p>通常情况下，实际开发中我们都需要使用构建工具对代码进行打包，TS同样也可以结合构建工具一起使用，下边以webpack为例介绍以下如何结合构建工具使用TS。</p>
<p>步骤：</p>
<ul>
<li>初始化项目</li>
</ul>
<p>进入项目根目录，执行命令：<code>npm init -y</code>，主要作用：创建<code>package.json</code>文件。</p>
<ul>
<li>下载构建工具</li>
</ul>
<p><code>npm i -D webpack webpack-cli webpack-dev-server typescript ts-loader clean-webpack-plugin</code></p>
<pre><code class="copyable">npm i -D webpack webpack-cli typescript ts-loader
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>webpack：构建工具webpack</li>
<li>webpack-cli: webpack的命令行工具</li>
<li>webpack-dev-server: webpack 的开发服务器</li>
<li>typescript: ts编译器</li>
</ul>
<pre><code class="copyable">// webpack.config.js

// 引入html插件
const HTMLWebpackPlugiin = require('html-webpack-plugin');
const &#123;CleanWebpackPlugin&#125; = require('clean-webpack-plugin');

// 配置webpack插件
plugins: [
 new CleanWebpackPlugin(),
 new HTMLWebpackPlugin(&#123;
  title: "这是一个自定义title"
 &#125;), // 自动的生成html文件
]

// 用来设置引用模块
resolve: &#123;
 extensions: ['.ts', '.js']
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// package.json
"script": &#123;
 ...
 "start": "webpack serve --open chrome.exe"
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用命令：<code>cnpm i -D @babel/core @babel/preset-env babel-loader core-js</code></p>
<pre><code class="copyable"> // 指定webpack打包时要使用模块
 module: &#123;
  // 指定要加载的规则
  rules: [
   &#123;
    // test指定的是规则生效的文件
    test: /\.ts$/,
    // 要使用的Loader
    use: [
     &#123;
     loader: "babel-loader",
     // 设置babel
     options: &#123;
      presets: [
       [
        // 指定环境的插件
        "@babel/preset-env",
        // 配置信息
        &#123;
         targets: &#123;
          "chrome":"88"
         &#125;
         "corejs": "3",
         // 使用corejs的方式 usage表示按需加载
         "useBuiltIns":"usage"
        &#125;
       ]
      ]
     &#125;
     &#125;
     
     'ts-loader'
    ]
    // 要排除的文件
    exclude: /node-modules/
   &#125;
  ]
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">面向对象</h3>
<p>面向对象是程序中一个非常重要的思想，它被很多同学理解成了一个比较难，比较深奥的问题。其实，面向对象很简单，程序之中所有的操作都需要通过对象来完成。</p>
<p>如：</p>
<ul>
<li>操作浏览器要使用window对象</li>
<li>操作网页要使用document对象</li>
<li>操作控制台要使用console对象</li>
</ul>
<p>一切操作都要通过对象，也就是所谓的面向对象，那么对象到底是什么呢？这就要先说到程序是什么，计算机程序的本质就是对现实事物的抽象，抽象的反义词是具体，比如：照片是对一个具体的人的抽象，汽车模型是对具体汽车的抽象等等。程序也是对事物的抽象，在抽象中我们可以表示一个人，一条狗等。一个事物到了程序就变成了一个对象。</p>
<h3 data-id="heading-7">类</h3>
<p>定义类：</p>
<pre><code class="copyable">class 类名 &#123;
 属性名: 类型;
 constructor(参数: 类型)&#123;
  this.属性名 = 参数;
 &#125;
 方法名()&#123;
  ...
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例：</p>
<pre><code class="copyable">class Person &#123;
 // 直接定义的属性是实例属性，需要通过对象的实例去访问：
 // const per = new Person();
 // per.name
 
 // 使用static开头的属性是静态属性（类属性），可以直接通过类去访问
 // Person.age
 
 // readonly开头的属性表示一个只读的属性
 
 // 定义实例属性
 name: string = 'jeskson';
 // 在属性前使用static 关键字可以定义类属性（静态属性）
 static age: number = 18;
&#125;
const per = new Person();
// console.log(per);
// console.log(per.name, per.age);
sayHello()&#123;
 console.log('hello');
&#125;

// 不加static，实例对象调用
// 定义static，类方法或属性
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">构造函数</h3>
<pre><code class="copyable">class Dog&#123;
 name = 'j';
 age = 1;
 bark()&#123;
  alert('j');
 &#125;
&#125;

const dog = new Dog();
const dog2 = new Dog();

console.log(dog);
console.log(dog2);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>改造：</p>
<pre><code class="copyable">class Dog &#123;
 name: string;
 age: number;
 
 // constructor 被称为构造函数
 // 构造函数会在对象创建时调用
 constructor(name: string, age: number) &#123;
  // 在实例方法中，this就表示当前的实例
  // 在构造函数中当前对象就是当前新建的那个对象
  // 可以通过this向新建的对象中添加属性
  this.name = name;
  this.age = age;
 &#125;
 bark() &#123;
  alert('1024bibi.com');
  // 在方法中可以通过this来表示当前调用方法的对象
  console.log(this.name);
 &#125;
&#125;
const dog = new Dog('dadaqianduan.cn', age: 1);
const dog2 = new Dog('1024bibi.com', age: 2);
console.log(dog);
console.log(dog2);

dog2.bark();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">继承</h3>
<pre><code class="copyable">(function()&#123;
 // 定义一个表示狗的类
 class Dog&#123;
  name: string;
  age: number;
  
  constructor(name: string, age: number) &#123;
   this.name = name;
   this.age = age;
  &#125;
  
  sayHello() &#123;
   console.log('dadaqianduan.cn')'
  &#125;
 &#125;
 
 const dog = new Dog('dada', 1);
 console.log(dog);
 dog.sayHello();
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用继承后，子类将会拥有父类所有的方法和属性</p>
<p>使用继承可以将多个类中公有的代码写在一个父类中，这样只需要写一次即可让所有的子类都同时拥有父类中的属性和方法。</p>
<p>子类覆盖掉父类方法的形式，称为方法重写。</p>
<pre><code class="copyable">class Dog extends Animal&#123;
 run() &#123;
  console.log();
 &#125;
 sayHello() &#123;
  console.log();
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">super-父类还有一个名字叫做超类</h3>
<pre><code class="copyable">(function()&#123;
 class Animal&#123;
  name: string;
  
  constructor(name: string) &#123;
   this.name = name;
  &#125;
  
  sayHello() &#123;
   console.log('动物叫');
  &#125;
 &#125;
 
 class Dog extends Animal&#123;
  sayHello() &#123;
   // 在类的方法中 super 就表示当前类的父类
   super.sayHello();
  &#125;
 &#125;
 
 const dog = new Dog('1024bibi.com');
 dog.sayHello();
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">class Dog extends Animal&#123;
 age: number,
 constructor(name: string, age: number)&#123;
  // 如果在子类中写了构造函数，在子类构造函数中必须对父类引用
  super(name); // 调用父类的构造函数
  this.age = age;
 &#125;
 sayHello() &#123;
  // 在类的方法中 super 就表示当前类的父类
  // super.sayHello();
 &#125;
&#125;
const dog = new Dog('dadaqianduan.cn');
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">抽象类</h3>
<p>以abstract开头的类是抽象类，不希望这个类创建对象的时候</p>
<p>抽象类中可以添加抽象方法，抽象方法只能定义在抽象类中，子类必须对抽象方法进行重写</p>
<pre><code class="copyable">abstract class Animal&#123;
 name: string;
 
 constructor(name: string) &#123;
  this.name = name;
 &#125;
 
 // 定义一个抽象方法
 // 抽象方法使用abstract开头，没有方法体
 // 抽象方法只能定义在抽象类中，子类必须对抽象方法进行重写
 abstract sayHello():void;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">接口</h3>
<pre><code class="copyable">(function()&#123;
 // 描述一个对象的类型
 type myType = &#123;
  name: string,
  age: number
 &#125;;
 
 // 接口用来定义一个类结构
 // 用来定义一个类中应该包含哪些属性和方法
 // 同时接口也可以当成类型声明去使用
 
 interface myInterface&#123;
  name: string;
  age: number;
 &#125;
 
 interface myInterface&#123;
  gender: string;
 &#125;
 
 const obj: myType = &#123;
  name: 'dada',
  age: 1
 &#125;;
 
 const obj1: myInterface = &#123;
  name: 'dada',
  age: 1,
  gender: '男'
 &#125;;
 
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接口可以在定义类的时候去限制类的结构</p>
<p>接口中的所有的属性都不能有实际的值</p>
<p>接口只定义对象的结构，而不考虑实际值</p>
<p>在接口中所有的方法都是抽象方法</p>
<pre><code class="copyable">interface myInter&#123;
 name: string;
 
 sayHello(): void;
&#125;

// 定义类时，可以使类去实现一个接口
// 实现接口就是使类满足接口的要求

class MyClass implements myInter &#123;
 name: string;
 constructor(name: stirng) &#123;
  this.name = name;
 &#125;
 sayHello()&#123;
  // 接口就是就类的限制，定义规范
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">封装</h3>
<pre><code class="copyable">(function()&#123;
 // 定义一个表示人的类
 class Person&#123;
  private _name: string;
  private _age: number;
  // public 修饰的属性可以在任意位置访问（修改）默认值
  // private 私有属性，私有属性只能在类内部进行访问修改
  
  // 通过在类中添加方法使得私有属性可以被外部访问
  
  constructor(name: string, age: number) &#123;
   this._name = name;
   this._age = age;
  &#125;
  // 定义方法，用来获取name属性
  getName() &#123;
   return this._name;
  &#125;
  // 定义方法，用来设置name属性
  setName(value: string) &#123;
    if(value>=0) &#123;
      this._name = value;
    &#125;
  &#125;
  
  // TS中设置getter方法的法方式
  get name() &#123;
  console.log('get name()执行了');
   return this._name;
  &#125;
  set age(value) &#123;
   if(value>=0)&#123;
    this._age = value;
   &#125;
  &#125;
  &#125;
 &#125;
 
 const per = new Person('jeskson', 18);
 console.log(per);
 
 // per.name = 'dadaqianduan.cn';
 // per.age = 12;
 
 // console.log(per.getName());
 // per.setName('jeskson');
 // per.age = 2
 
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">get name() &#123;
 return this._name;
&#125;

set name(value) &#123;
 this._name = value;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">public</h3>
<pre><code class="copyable">class A &#123;
 public num: number;
 // private num: number;
 // protected 受保护的属性，只能在当前类和子类中使用
 constructor(num: number)&#123;
  this.num = num;
 &#125;
&#125;

class B extends A &#123;
 test() &#123;
  console.log(this.num);
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">语法糖</h3>
<pre><code class="copyable">class C&#123;
 // 可以直接将属性定义在构造函数中
 constructor(public name: string, public age: number)&#123;
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">泛型</h3>
<p>在定义函数或是类时，如果遇到类型不明确就可以使用泛型</p>
<pre><code class="copyable">function fn(a: number): number&#123;
 return a;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时泛型便能够发挥作用；</p>
<p>举个例子：</p>
<pre><code class="copyable">function test(arg: any): any&#123;
    return arg;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>any会关闭掉类型的检查，任意类型</li>
</ul>
<p>使用any会关闭TS的类型检查，其次这样设置也不能体现出参数和返回值是相同的类型。</p>
<p>创建泛型函数</p>
<pre><code class="copyable">// 类型不明确时，使用泛型
function fn<T>(a: T): T&#123;
 return a;
&#125;
// T只有在函数的执行的时候，才能定义
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的<code><T></code>就是泛型，不一定非叫T</p>
<p>可以直接调用具有泛型的函数</p>
<pre><code class="copyable">fn(10); // 不指定泛型，ts可以自动对类型进行推断

fn<string>('jeskson'); // 指定泛型

function fn2<T,k>(a: T, b: K): T &#123;
 console.log(b);
 return a;
&#125;

fn2<number, string>(123, 'dadaqianduan.cn');

// 限制泛型的类型

interface Inter &#123;
 length: number;
&#125;

function fn3<T extends Inter>(a: T): number&#123;
 return a.length;
&#125;

fn3('123');
fn3(&#123;length: 12);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>泛型可以同时指定多个，<code>T extends Inter</code>表示泛型必须时Inter实现类（子类）</p>
<p>泛型类</p>
<pre><code class="copyable">class MyClass<T> &#123;
 name: T;
 constructor(name: T) &#123;
  this.name = name;
 &#125;
&#125;

const mc = new MyClass<string>('jeskson');
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">typescript打包</h3>
<p>webpack整合，通常情况下，实际开发中我们都需要使用构建工具对代码进行打包；TS同样也可以结合构建工具一起使用，下边以webpack为例介绍一下如何构建工具使用TS：</p>
<p>初始化项目，进入项目根目录执行命令：<code>npm init -y</code>，创建<code>package.json</code>文件。</p>
<p><strong>下载构建工具</strong>，命令如下：</p>
<pre><code class="copyable">npm i -D webpack webpack-cli webpack-dev-server typescript ts-loader clean-webpack-plugin
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>webpack</code>：构建工具<code>webpack</code></li>
<li><code>webpack-cli</code>：<code>webpack</code>的命令行工具</li>
<li><code>webpack-dev-server</code>：<code>webpack</code>的开发服务器</li>
<li><code>typescript</code>：<code>ts</code>编译器</li>
<li><code>ts-loader</code>：<code>ts</code>加载器，用于在webpack中编译ts文件</li>
<li><code>html-webpack-plugin</code>：<code>webpack</code>中html插件，用来自动创建html文件</li>
<li><code>clean-webpack-plugin</code>：<code>webpack</code>中的清除插件，每次构建都会先清除目录</li>
</ul>
<p>配置<code>webpack</code></p>
<p>根目录下创建webpack的配置文件<code>webpack.config.js：</code></p>
<pre><code class="copyable">const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const &#123; CleanWebpackPlugin &#125; = require("clean-webpack-plugin");

module.exports = &#123;
   optimization:&#123;
       minimize: false // 关闭代码压缩，可选
   &#125;,

   entry: "./src/index.ts",

   devtool: "inline-source-map",

   devServer: &#123;
       contentBase: './dist'
   &#125;,

   output: &#123;
       path: path.resolve(__dirname, "dist"),
       filename: "bundle.js",
       environment: &#123;
           arrowFunction: false // 关闭webpack的箭头函数，可选
       &#125;
   &#125;,

   resolve: &#123;
       extensions: [".ts", ".js"]
   &#125;,

   module: &#123;
       rules: [
           &#123;
               test: /\.ts$/,
               use: &#123;
                   loader: "ts-loader"     
               &#125;,
               exclude: /node_modules/
           &#125;
       ]
   &#125;,

   plugins: [
       new CleanWebpackPlugin(),
       new HtmlWebpackPlugin(&#123;
           title:'TS测试'
       &#125;),
   ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>配置TS编译选项</strong></p>
<p>根目录下创建<code>tsconfig.json</code>，配置可以根据自己需要</p>
<pre><code class="copyable">&#123;
   "compilerOptions": &#123;
       "target": "ES2015",
       "module": "ES2015",
       "strict": true
   &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改<code>package.json</code>配置</p>
<pre><code class="copyable">"scripts": &#123;
   "test": "echo \"Error: no test specified\" && exit 1",
   "build": "webpack",
   "start": "webpack serve --open chrome.exe"
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>项目使用</strong></p>
<p>在src下创建ts文件，并在并命令行执行<code>npm run build</code>对代码进行编译；</p>
<p>或者执行<code>npm start</code>来启动开发服务器；</p>
<p><strong>Babel</strong></p>
<p>除了webpack，开发中还经常需要结合babel来对代码进行转换；以使其可以兼容到更多的浏览器，在上述步骤的基础上，通过以下步骤再将babel引入到项目中。</p>
<p>Promise等ES6特性，TS无法直接转换，这时还要用到babel来做转换。</p>
<p>安装依赖包：</p>
<pre><code class="copyable">npm i -D @babel/core @babel/preset-env babel-loader core-js
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>共安装了4个包</strong>，分别是：</p>
<p><code>@babel/core</code>：babel的核心工具</p>
<p><code>@babel/preset-env</code>：babel的预定义环境</p>
<p><code>@babel-loader</code>：<code>babel</code>在<code>webpack</code>中的加载器</p>
<p><code>core-js</code>：<code>core-js</code>用来使老版本的浏览器支持新版ES语法</p>
<p>修改<code>webpack.config.js</code>配置文件</p>
<pre><code class="copyable">module: &#123;
    rules: [
        &#123;
            test: /\.ts$/,
            use: [
                &#123;
                    loader: "babel-loader",
                    options:&#123;
                        presets: [
                            [
                                "@babel/preset-env",
                                &#123;
                                    "targets":&#123;
                                        "chrome": "58",
                                        "ie": "11"
                                    &#125;,
                                    "corejs":"3",
                                    "useBuiltIns": "usage"
                                &#125;
                            ]
                        ]
                    &#125;
                &#125;,
                &#123;
                    loader: "ts-loader",

                &#125;
            ],
            exclude: /node_modules/
        &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用ts编译后的文件将会再次被babel处理;使得代码可以在大部分浏览器中直接使用;同时可以在配置选项的targets中指定要兼容的浏览器版本</p>
<h3 data-id="heading-18">编译选项</h3>
<p>自动编译文件</p>
<pre><code class="copyable">tsc xxx.ts -w
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>自动编译整个项目</strong></p>
<p>如果直接使用tsc指令，则可以自动将当前项目下的所有ts文件编译为js文件。</p>
<p>但是能直接使用tsc命令的前提时，要先在项目根目录下创建一个ts的配置文件 <code>tsconfig.json</code></p>
<p><code>tsconfig.json</code>是一个JSON文件，添加配置文件后，只需只需 tsc 命令即可完成对整个项目的编译</p>
<p><code>include</code></p>
<p>定义希望被编译文件所在的目录</p>
<pre><code class="copyable">默认值：["**/*"]
示例：

"include":["src/**/*", "tests/**/*"]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>exclude</code></p>
<p>定义需要排除在外的目录</p>
<pre><code class="copyable">默认值：["node_modules", "bower_components", "jspm_packages"]
示例：

"exclude": ["./src/hello/**/*"]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>extends</code></p>
<p>定义被继承的配置文件</p>
<pre><code class="copyable">示例：

"extends": "./configs/base"
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>files</code></p>
<p>指定被编译文件的列表，只有需要编译的文件少时才会用到</p>
<p><code>compilerOptions</code></p>
<p>编译选项是配置文件中非常重要也比较复杂的配置选项</p>
<pre><code class="copyable">"compilerOptions": &#123;
    "target": "ES6"
&#125;

// 设置ts代码编译的目标版本

// 可选值：

ES3（默认）、ES5、ES6/ES2015、ES7/ES2016、ES2017、ES2018、ES2019、ES2020、ESNext
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>lib</code></p>
<p>指定代码运行时所包含的库（宿主环境）</p>
<pre><code class="copyable">"compilerOptions": &#123;
    "target": "ES6",
    "lib": ["ES6", "DOM"],
    "outDir": "dist",
    "outFile": "dist/aa.js"
&#125;

// 可选值：

ES5、ES6/ES2015、ES7/ES2016、ES2017、ES2018、ES2019、ES2020、ESNext、DOM、WebWorker、ScriptHost ......
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>module</code></p>
<p>设置编译后代码使用的模块化系统</p>
<pre><code class="copyable">"compilerOptions": &#123;
    "module": "CommonJS"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>outDir</code></p>
<p>编译后文件的所在目录</p>
<pre><code class="copyable">"compilerOptions": &#123;
    "outDir": "dist"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>outFile</code></p>
<p>将所有的文件编译为一个js文件</p>
<p>默认会将所有的编写在全局作用域中的代码合并为一个js文件，如果module制定了None、System或AMD则会将模块一起合并到文件之中</p>
<pre><code class="copyable">"compilerOptions": &#123;
    "outFile": "dist/app.js"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>rootDir</code></p>
<p>指定代码的根目录，默认情况下编译后文件的目录结构会以最长的公共目录为根目录</p>
<pre><code class="copyable">// 通过rootDir可以手动指定根目录
"compilerOptions": &#123;
    "rootDir": "./src"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>allowJs</code></p>
<p>是否对js文件编译</p>
<p><code>checkJs</code></p>
<p>是否对js文件进行检查</p>
<pre><code class="copyable">"compilerOptions": &#123;
    "allowJs": true,
    "checkJs": true
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>removeComments</code></p>
<ul>
<li>是否删除注释</li>
<li>默认值：false</li>
</ul>
<p><code>noEmit</code></p>
<ul>
<li>不对代码进行编译</li>
<li>默认值：false</li>
</ul>
<p><code>sourceMap</code></p>
<ul>
<li>是否生成<code>sourceMap</code></li>
<li>默认值：<code>false</code></li>
</ul>
<p><strong>严格检查</strong></p>
<pre><code class="copyable">strict
启用所有的严格检查，默认值为true，设置后相当于开启了所有的严格检查

alwaysStrict
总是以严格模式对代码进行编译

noImplicitAny
禁止隐式的any类型

noImplicitThis
禁止类型不明确的this

strictBindCallApply
严格检查bind、call和apply的参数列表

strictFunctionTypes
严格检查函数的类型

strictNullChecks
严格的空值检查

strictPropertyInitialization
严格检查属性是否初始化
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>额外检查</strong></p>
<p><code>noFallthroughCasesInSwitch</code></p>
<p>检查switch语句包含正确的break</p>
<p><code>noImplicitReturns</code></p>
<p>检查函数没有隐式的返回值</p>
<p><code>noUnusedLocals</code></p>
<p>检查未使用的局部变量</p>
<p><code>noUnusedParameters</code></p>
<p>检查未使用的参数</p>
<p><code>allowUnreachableCode</code></p>
<p>检查不可达代码</p>
<p>可选值：
true，忽略不可达代码
false，不可达代码将引起错误</p>
<p><code>noEmitOnError</code></p>
<p>有错误的情况下不进行编译，默认值：false</p>
<pre><code class="copyable">npm i -D less less-loader css-loader style-loader
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">问题：<code>request to https://registry.cnpmjs.org/ts-loader failed, reason: Hostname/IP does not match certificate's altnames: Host: registry.cnpmjs.org. is not in the cert's altnames: DNS:r.cnpmjs.org</code></h3>
<p>命令行下执行：</p>
<p>关闭<code>npm</code>的<code>https</code>（取消<code>npm</code>的<code>https</code>认证）</p>
<pre><code class="copyable">npm config set strict-ssl false
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">npm ERR! code ERR_TLS_CERT_ALTNAME_INVALID
npm ERR! errno ERR_TLS_CERT_ALTNAME_INVALID
npm ERR! request to https://registry.cnpmjs.org/cnpm failed, reason: Hostname/IP does not match certificate's altnames: Host: registry.cnpmjs.org. is not in the cert's altnames: DNS:r.cnpmjs.org

npm ERR! A complete log of this run can be found in:
npm ERR!     C:\Users\41586\AppData\Roaming\npm-cache\_logs\2020-08-23T00_26_46_591Z-debug.log
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解决办法：</p>
<pre><code class="copyable">npm config set registry http://registry.npmjs.org/
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用TypeScript + Webpack + Less项目依赖：</p>
<pre><code class="copyable">TypeScript：

typescript；
ts-loader；
Webpack：

webpack；
webpack-cli；
webpack-dev-server；
html-webpack-plugin；
clean-webpack-plugin；
Babel：

core-js；
babel-loader；
@babel/core；
@babel/preset-env；
Less & CSS资源：

style-loader；
css-loader；
less；
less-loader；
postcss；
postcss-loader；
postcss-preset-env；
<span class="copy-code-btn">复制代码</span></code></pre>
<p>分别执行下面的命令安装依赖并编译项目：</p>
<pre><code class="copyable"># 安装依赖
npm i
# 编译打包
npm run build
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用<code>npm run start</code>进入开发模式。</p>
<p>问题：</p>
<pre><code class="copyable">Invalid configuration object. Webpack has been initialised using a configuration object that does not match the API schema.
 - configuration.output has an unknown property 'environment'. These properties are valid:
   object &#123; auxiliaryComment?, chunkCallbackName?, chunkFilename?, chunkLoadTimeout?, crossOriginLoading?, devtoolFallbackModuleFilen
ameTemplate?, devtoolLineToLine?, devtoolModuleFilenameTemplate?, devtoolNamespace?, filename?, futureEmitAssets?, globalObject?, has
hDigest?, hashDigestLength?, hashFunction?, hashSalt?, hotUpdateChunkFilename?, hotUpdateFunction?, hotUpdateMainFilename?, jsonpFunc
tion?, jsonpScriptType?, library?, libraryExport?, libraryTarget?, path?, pathinfo?, publicPath?, sourceMapFilename?, sourcePrefix?,
strictModuleExceptionHandling?, umdNamedDefine?, webassemblyModuleFilename? &#125;
   -> Options affecting the output of the compilation. `output` options tell webpack how to write the compiled files to disk.
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">npm ERR! code ELIFECYCLE
npm ERR! errno 1
npm ERR! demo@1.0.0 build: `webpack`
npm ERR! Exit status 1
npm ERR!
npm ERR! Failed at the demo@1.0.0 build script.
npm ERR! This is probably not a problem with npm. There is likely additional logging output above.
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Mode</strong>模式（Mode）</p>
<p>提供 mode 配置选项，告知 webpack 使用相应模式的内置优化。</p>
<p><code>Providing the mode configuration option tells webpack to use its built-in optimizations accordingly.</code></p>
<pre><code class="copyable">string = 'production': 'none' | 'development' | 'production'
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>用法</strong></p>
<p>只需在配置对象中提供 mode 选项：</p>
<pre><code class="copyable">module.exports = &#123;
  mode: 'development',
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者从 CLI 参数中传递：</p>
<pre><code class="copyable">webpack --mode=development
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Mode: development</p>
<pre><code class="copyable">// webpack.development.config.js
module.exports = &#123;
 mode: 'development'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Mode: production</p>
<pre><code class="copyable">// webpack.production.config.js
module.exports = &#123;
  mode: 'production',
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Mode: none</p>
<pre><code class="copyable">// webpack.custom.config.js
module.exports = &#123;
 mode: 'none',
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果要根据 webpack.config.js 中的 mode 变量更改打包行为，则必须将配置导出为函数，而不是导出对象：</p>
<pre><code class="copyable">var config = &#123;
  entry: './app.js',
  //...
&#125;;

module.exports = (env, argv) => &#123;
  if (argv.mode === 'development') &#123;
    config.devtool = 'source-map';
  &#125;

  if (argv.mode === 'production') &#123;
    //...
  &#125;

  return config;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>css</p>
</blockquote>
<pre><code class="copyable">// 清除默认样式
* &#123;
 margin: 0;
 padding: 0;
 // 改变盒子模型的计算方式
 box-sizing: border-box;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>box-sizing属性用于更改用于计算元素的宽度和高度默认的CSS盒子模型，可以使用此属性来模拟不正确支持CSS盒子模型规范的浏览器行为。</p>
<p>框属性的基本规范：</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a3d48c49b6f49e2a884276f8857db87~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol>
<li>
<p><code>width</code>和<code>height</code>设置内容框的宽度和高度。内容框是框内容显示的区域，包括框内的文本内容。</p>
</li>
<li>
<p><code>padding</code>表示一个<code>css</code>框内边距，这一层位于内容框的外边缘与边界的内边缘之间。</p>
</li>
<li>
<p><code>border</code>即<code>css</code>框的边界是一个分隔层。</p>
</li>
<li>
<p><code>margin</code>即外边距代表<code>css</code>框周围的外部区域。</p>
</li>
</ol>
<ul>
<li><code>box-sizing:border-box</code>属性</li>
</ul>
<p>运用<code>box-sizing:border-box</code>属性下，框模型的变化</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc05b585c461432cb3a936989b2be1e3~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><code>width=content+padding+border</code></p>
<p>采用的是<code>flex</code>布局的方式，为了自适应，宽度<code>width</code>采用的是百分比<code>%</code>的形式，<code>border，padding，margin</code>采用的是<code>px</code>尺寸，所有外层的盒子运用了<code>box-sizing:border-box</code>，属性来改变盒子的结构。</p>
<p>背景裁剪（Background clip）属性</p>
<ul>
<li><code>background-clip: border-box</code>：背景被裁剪到边框盒</li>
</ul>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b0e5a26b296455fb871b6ef70228d86~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">#div &#123;
    padding: 25px;
    border:10px dotted #000;
    background-color: yellow;
    background-clip: border-box;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>background-cilp: padding-box;</code>背景被裁剪到内边距框；</li>
</ul>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ed55ee2260f4655a93490b8eac09613~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">#div &#123;
    padding: 25px;
    border:10px dotted #000;
    background-color: yellow;
    background-clip: padding-box;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>background-clip: content-box;</code>背景被裁剪到内容框。</li>
</ul>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7c8200039b94a988910580d56ce9230~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">#div &#123;
    padding: 25px;
    border:10px dotted #000;
    background-color: yellow;
    background-clip: content-box;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">块级盒子和内联盒子</h3>
<ul>
<li>块级盒子</li>
</ul>
<p>一个被定义成块级的（<code>block</code>）盒子会表现出以下行为:</p>
<ul>
<li>
<p>盒子会在内联的方向上扩展并占据父容器在该方向上的所有可用空间，在绝大数情况下意味着盒子会和父容器一样宽</p>
</li>
<li>
<p>每个盒子都会换行</p>
</li>
<li>
<p><code>width 和 height</code> 属性可以发挥作用</p>
</li>
<li>
<p>内边距（<code>padding</code>）, 外边距（<code>margin</code>） 和 边框（<code>border</code>） 会将其他元素从当前盒子周围“推开”</p>
</li>
<li>
<p>内联盒子</p>
</li>
</ul>
<p>一个被定义成内联的（<code>inline box</code>）盒子会表现出以下行为:</p>
<ul>
<li>盒子不会产生换行。</li>
<li><code>width 和 height</code> 属性将不起作用。</li>
<li>垂直方向的内边距、外边距以及边框会被应用但是不会把其他处于 <code>inline</code> 状态的盒子推开。</li>
<li>水平方向的内边距、外边距以及边框会被应用且会把其他处于 <code>inline</code> 状态的盒子推开。</li>
</ul>
<p><strong>CSS中组成一个块级盒子需要:</strong></p>
<p><code>Content box</code>: 这个区域是用来显示内容，大小可以通过设置 <code>width 和 height</code>.</p>
<p><code>Padding box</code>: 包围在内容区域外部的空白区域； 大小通过 <code>padding</code> 相关属性设置。</p>
<p><code>Border box</code>: 边框盒包裹内容和内边距。大小通过 <code>border</code> 相关属性设置。</p>
<p><code>Margin box</code>: 这是最外面的区域，是盒子和其他元素之间的空白区域。大小通过 <code>margin</code> 相关属性设置。</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7b9da12b1d04fec92d45e12d518217b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在标准模型中，如果你给盒设置 <code>width 和 height</code>，实际设置的是 <code>content box</code>。</p>
<p><code>padding 和 border</code> 再加上设置的宽高一起决定整个盒子的大小。</p>
<p>示例：</p>
<pre><code class="copyable">.box &#123;
  width: 350px;
  height: 150px;
  margin: 25px;
  padding: 25px;
  border: 5px solid black;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果使用标准模型宽度 = <code>410px (350 + 25 + 25 + 5 + 5)</code>，高度 = <code>210px (150 + 25 + 25 + 5 + 5)</code>，<code>padding 加 border 再加 content box</code>。</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5f39bdc0fae44b095340fa4775d1ae1~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-21">替代（IE）盒模型</h3>
<p>默认浏览器会使用标准模型。如果需要使用替代模型，您可以通过为其设置 <code>box-sizing: border-box</code> 来实现。</p>
<p>示例：</p>
<pre><code class="copyable">.box &#123;
  box-sizing: border-box;
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68fb50a35c80491e8102727a2d17637d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-22">回看笔者往期高赞文章，也许能收获更多喔！</h3>
<ul>
<li><a href="https://juejin.cn/post/6925197705832562696" target="_blank">一个合格的初级前端工程师需要掌握的模块笔记</a></li>
<li><a href="https://juejin.cn/post/6948576107163549732" target="_blank">前端模拟面试字数过23477万内容</a></li>
<li><a href="https://juejin.cn/post/6916664414422695949" target="_blank">Vue.js笔试题解决业务中常见问题</a></li>
<li><a href="https://juejin.cn/post/6923946134025191432" target="_blank">【初级】个人分享Vue前端开发教程笔记</a></li>
<li><a href="https://juejin.cn/post/6844904078934278158" target="_blank">长篇总结之JavaScript，巩固前端基础</a></li>
<li><a href="https://juejin.cn/post/6844904067764846600" target="_blank">前端面试必备ES6全方位总结</a></li>
<li><a href="https://juejin.cn/post/6913480482638266382" target="_blank">达达前端个人web分享92道JavaScript面试题附加回答</a></li>
<li><a href="https://juejin.cn/post/6844904117337341959" target="_blank">【图文并茂，点赞收藏哦！】重学巩固你的Vuejs知识体系</a></li>
<li><a href="https://juejin.cn/post/6844904106243391495" target="_blank">【思维导图】前端开发-巩固你的JavaScript知识体系</a></li>
<li><a href="https://juejin.cn/post/6850037263116533773" target="_blank">14期-连肝7个晚上，总结了计算机网络的知识点！（共66条）</a></li>
<li><a href="https://juejin.cn/post/6929701436276097032" target="_blank">这是我的第一次JavaScript初级技巧</a></li>
<li><a href="https://juejin.cn/post/6923331849708109838" target="_blank">localStorage和sessionStorage本地存储</a></li>
<li><a href="https://juejin.cn/post/6922602775947771911" target="_blank">HTML5中的拖放功能</a></li>
<li><a href="https://juejin.cn/post/6918735942710722574" target="_blank">挑战前端知识点HTTP/ECMAScript</a></li>
<li><a href="https://juejin.cn/post/6918011549231775751" target="_blank">必学必会-音频和视频</a></li>
<li><a href="https://juejin.cn/post/6917635279423537165" target="_blank">前端170面试题+答案学习整理（良心制作）</a></li>
<li><a href="https://juejin.cn/post/6917044041863397383" target="_blank">前端HTML5面试官和应试者一问一答</a></li>
<li><a href="https://juejin.cn/post/6916162359765663752" target="_blank">哪吒闹海，席卷图文学习前端Flex布局</a></li>
<li><a href="https://juejin.cn/post/6909784318856396808" target="_blank">腾讯位置服务开发应用</a></li>
<li><a href="https://juejin.cn/post/6905946191193325582" target="_blank">【进阶】面试官问我Chrome浏览器的渲染原理（6000字长文）</a></li>
<li><a href="https://juejin.cn/post/6900724539833516040" target="_blank">面试官一上来就问我Chrome底层原理和HTTP协议（万字长文）</a></li>
<li><a href="https://juejin.cn/post/6855448306517344263" target="_blank">熬夜总结了 “HTML5画布” 的知识点</a></li>
<li><a href="https://juejin.cn/post/6844904186069401607" target="_blank">this/call/apply/bind（万字长文）</a></li>
<li><a href="https://juejin.cn/post/6844904163453714445" target="_blank">HTTP/HTTPS/HTTP2/DNS/TCP/经典题</a></li>
<li><a href="https://juejin.cn/post/6844904161532706823" target="_blank">执行上下文/作用域链/闭包/一等公民</a></li>
<li><a href="https://juejin.cn/post/6844904104712470535" target="_blank">Web页面制作基础</a></li>
<li><a href="https://juejin.cn/post/6844904082629459975" target="_blank">学习总结之HTML5剑指前端（建议收藏，图文并茂）</a></li>
</ul>
<p>❤️关注+点赞+收藏+评论+转发❤️</p>
<h3 data-id="heading-23">点赞、收藏和评论</h3>
<p>我是<code>Jeskson</code>(达达前端)，感谢各位人才的：<strong>点赞、收藏和评论</strong>，我们下期见！(如本文内容有地方讲解有误，欢迎指出☞<strong>谢谢，一起学习了</strong>)</p>
<h3 data-id="heading-24">我们下期见！</h3>
<blockquote>
<p>文章持续更新，可以微信搜一搜「 <strong>程序员哆啦A梦</strong> 」第一时间阅读，回复【资料】有我准备的一线大厂资料，本文 <a href="http://www.dadaqianduan.cn/#/" target="_blank" rel="nofollow noopener noreferrer">www.dadaqianduan.cn/#/</a> 已经收录</p>
</blockquote>
<blockquote>
<p><code>github</code>收录，欢迎<code>Star</code>：<a href="https://github.com/webVueBlog/WebFamily" target="_blank" rel="nofollow noopener noreferrer">github.com/webVueBlog/…</a></p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            