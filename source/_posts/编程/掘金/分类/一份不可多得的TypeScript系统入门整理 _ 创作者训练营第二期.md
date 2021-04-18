
---
title: '一份不可多得的TypeScript系统入门整理 _ 创作者训练营第二期'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5738c22d3d6f4726a0427f06c1bff788~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 18 Apr 2021 02:11:13 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5738c22d3d6f4726a0427f06c1bff788~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><ul>
<li>推荐： <a href="https://juejin.cn/post/6950052678927908901" target="_blank">TypeScript趁早学习提高职场竞争力</a></li>
</ul>
<p><a href="https://github.com/webVueBlog/WebFamily" target="_blank" rel="nofollow noopener noreferrer">Github来源：</a> | 求星星 ✨ | 给个❤️关注，❤️点赞，❤️鼓励一下作者</p>
<p>希望能够帮助更多的小伙伴。加我😚即可交流问题（不是大佬，互相学习，创造良好的学习环境）。以下哪些你不懂呢？</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5738c22d3d6f4726a0427f06c1bff788~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="TypeScript.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bdfb34fcac30412db26acbe0d9e0672e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="TS基础篇.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d59f2c57c2e14dac9afa670b2e3a2b52~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在另一页面打开即可高清</p>
<p><img alt="TypeScript.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8cf145d46ea847bea2d3747140e23d91~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">TypeScript开发</h3>
<p>全局安装typescript，使用安装命令可以使用<code>npm</code>也可以使用<code>yarn</code>：</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17dcf3a1c70d4c539a8f99f61073628e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">npm install typescript -g

yarn global add typescript
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">demo.ts</h3>
<pre><code class="copyable">function jeskson() &#123;
 let web: string = "hello world"
 console.log(web)
&#125;

jeskson()

// tsc
tes demo.ts
node demo.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6ee77ca17254fbfb69fc1dcc3fbfb62~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de47fe245e484bce93c1bf8ee08562b1~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">npm install -g ts-node
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">数据类型</h3>
<ul>
<li>TS的数据类型</li>
</ul>
<pre><code class="copyable">// ES6的数据类型：
基本数据类型：Boolean,Number,String,Symbol,undefined,null

引用类型：Array,Function,Object

// TS的数据类型，增加
void,any,never,元组,枚举,高级类型
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类型注解：</p>
<pre><code class="copyable">let hello : string = 'Hello TypeScript'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原始类型</p>
<pre><code class="copyable">let bl: boolean = true
let num: number = 123
let str: string = "123"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>数组泛型</p>
<pre><code class="copyable">let arrType: Array<number> = [0, 1, 2, 3, 5];
let arrType1: Array<string> = ['0', '1', '2', '3', '5'];
let arrType2: Array<any> = [1, '1', 2, 's', true];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用接口表示数组</p>
<pre><code class="copyable">interface Person&#123;
  name: string;
  age: number;
&#125;
interface NumberArray &#123;
       [index:number]: Person;         
&#125;
let arrType3: NumberArray = [&#123;name:'张三'，age: 20&#125;]
let arrType4：Array<Person> = [&#123;name:'张三'，age: 20&#125;]
let arrType5：Person[] = [&#123;name:'张三'，age: 20&#125;]
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>类数组</p>
</blockquote>
<p>类数组（Array-like Object）不是数组类型:</p>
<pre><code class="copyable">function sum() &#123;
    let args: number[] = arguments;
&#125;

// index.ts(2,7): error TS2322: Type 'IArguments' is not assignable to type 'number[]'.
//   Property 'push' is missing in type 'IArguments'.

function sum() &#123;
    let args: IArguments = arguments;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>元组类型</p>
</blockquote>
<pre><code class="copyable">let tuple: [number, string] = [0, '1']
// 此时,如果改变数组的元素类型或添加元素数量,编辑器都会报错
// TS允许向元组中使用数组的push方法插入新元素(但不允许访问)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">函数</h3>
<p>函数声明（Function Declaration）和函数表达式（Function Expression）</p>
<pre><code class="copyable">// 函数声明（Function Declaration）
function sum(x, y) &#123;
    return x + y;
&#125;

// 函数表达式（Function Expression）
let mySum = function (x, y) &#123;
    return x + y;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// 函数声明的类型定义
function sum(x:number,y:number):number&#123;
       return x+y  
&#125;
// 输入多余的或者少于要求的参数，是不被允许的

// 函数表达式
let mySun = function(x:number,y:number):number&#123;
      return x + y  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用接口定义函数的形状</p>
<pre><code class="copyable">interface SearchFunc&#123;
       （source:string,subString:string）:boolean
&#125;    

let mySearch:SearchFunc;
mySearch = function(source: string,subString:string)&#123;
     return source.search(subString) !== -1  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>与接口中的可选属性类似，我们用 <code>?</code> 表示可选的参数：</p>
<pre><code class="copyable">function buildName(firstName: string, lastName?: string) &#123;
    if (lastName) &#123;
        return firstName + ' ' + lastName;
    &#125; else &#123;
        return firstName;
    &#125;
&#125;
let tomcat = buildName('dada', 'Cat');
let tom = buildName('dada');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参数默认值</p>
<pre><code class="copyable">function buildName(firstName:string,lastName:string='Cat')&#123;
    return firstName + ' ' + lastName;
&#125;
let tomcat = buildName('dada', 'Cat');
let tom = buildName('dada');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>剩余参数</p>
<pre><code class="copyable">// 可以使用 ...rest 的方式获取函数中的剩余参数

function push(array,...items)&#123;
     items.forEach(function(item)&#123;
        array.push(item)
　　&#125;)  
&#125;

let a = [];
push(a,1,2,3)


function push(array:any[],...items:any[])&#123;
     items.forEach(function(item)&#123;
         array.push(item);
    &#125;)  
&#125;

let a = []
push(a,1,2,3)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">重载</h3>
<p>重载允许一个函数接受不同数量或类型的参数时，作出不同的处理</p>
<pre><code class="copyable">function reverse(x: number | string): number | string &#123;
    if (typeof x === 'number') &#123;
        return Number(x.toString().split('').reverse().join(''));
    &#125; else if (typeof x === 'string') &#123;
        return x.split('').reverse().join('');
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用重载定义多个 <code>reverse</code> 的函数类型：</p>
<pre><code class="copyable">function reverse(x: number): number;
function reverse(x: string): string;
function reverse(x: number | string): number | string &#123;
    if (typeof x === 'number') &#123;
        return Number(x.toString().split('').reverse().join(''));
    &#125; else if (typeof x === 'string') &#123;
        return x.split('').reverse().join('');
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">静态类型</h3>
<pre><code class="copyable">let count : number = 1;

interface dada &#123;
 uname: string,
 age: number
&#125;

const jeskson :dada = &#123;
 uname: 'jeskson',
 age: 12
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对象类型：</p>
<pre><code class="copyable">const gege: &#123;
 name: string,
 age: number
&#125; = &#123;
 name: 'jeskson',
 age: 12
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">const person : string [] = ['dada', 'jeskson', '掘金魔王哪吒']
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">class Person&#123;&#125;
const dada : Person = new Person()

const dada :()=>string = ()=>&#123;return 'jeskson'&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>静态类型：对象类型，数组类型，类类型，函数类型</p>
<h3 data-id="heading-6">类型注解与类型推断</h3>
<p>局部变量：</p>
<pre><code class="copyable">let count : number;
count=12;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果ts能够自动分析判断变量类型，就不需要，否则就需要使用类型注解。</p>
<blockquote>
<p>函数参数和函数的返回类型的注解</p>
</blockquote>
<pre><code class="copyable">function getNum(a : number, two : number) : number &#123;
 return a + b
&#125;
const total = getNum(1,2)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>never</p>
</blockquote>
<pre><code class="copyable">function errorFunction() : never &#123;
 throw new Error()
 console.log('hello world')
&#125;

function forNever() : never &#123;
 while(true) &#123;&#125;
 console.log('hello world')
&#125;

function add(&#123;one,two&#125; : &#123;one : number,two : number&#125;) &#123;
 return one + two
&#125;
const total = add(&#123;one:1,two:2&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>数组类型注解</p>
</blockquote>
<pre><code class="copyable">const numberArr : number[] = [1,2,3]

const stringArr : string[] = ['a','b','c']

const undefinedArr : undefined[] = [undefined, undefined]

const arr : (number | string)[] = [1,'string',2]

const dada : &#123;name:string,age:number&#125;[] = [
 &#123;name:'jeskson',age:12&#125;,
 &#123;name:'魔王哪吒',age:12&#125;,
]

// 类别别名
// type alias
type typeMy = &#123;name:string,age:number&#125;

const dada : typeMy[] = [&#123;name:'jeskson',age:12&#125;]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">元组</h3>
<p>加强版：</p>
<pre><code class="copyable">const dada : (string | number)[] = ['魔王哪吒','jeskson',12]

// 不常用-元组
const dada1 : [string,string,number] = ["jeskson",12,"dadaqianduan"]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">接口</h3>
<pre><code class="copyable">interface dada &#123;
 name: 'jeskson';
 age: 12;
 work ?: string;
 say():string;
&#125;

class obj implements dada &#123;
 name="dada"
 age=12
 work="it"
 say()&#123;
  return "dadaqianduan"
 &#125;
&#125;

const selected = (person: dada)=>&#123;
&#125;

// obj.name && console.log(obj.name)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">类</h3>
<pre><code class="copyable">class Da &#123;
 content = "掘金魔王哪吒"
 sayHello() &#123;
  return this.content
 &#125;
&#125;

consot da = new Da()
console.log(da.sayHello())
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">class Person &#123;
 name: string;
&#125;
const person = new Person()
person.name = "jeskson"
console.log(person.name)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类的构造函数</p>
<pre><code class="copyable">class Person &#123;
 public name : string;
 constructor(name:string)&#123;
  this.name = name
 &#125;
&#125;

// 优化
class Person &#123;
 constructor(public name:string)&#123;&#125;
&#125;
class Teacher extends Person&#123;
 constructor(public age:number)&#123;
  super('jeskson')
 &#125;
&#125;

const person = new Person('jeskson')

const dada = new Teacher(12)
console.log(dada.age)
console.log(person.name)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">Getter,Setter,static</h3>
<pre><code class="copyable">class Da &#123;
 constructor(private _age:number)&#123;&#125;
 get age() &#123;
  return this._age
 &#125;
 set age(age:number) &#123;
  this._age = age
 &#125;
&#125;

const dada = new Da(12)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">class Da&#123;
 static sayHello() &#123;
  return "魔王哪吒"
 &#125;
&#125;
console.log(Da.sayHello())
<span class="copy-code-btn">复制代码</span></code></pre>
<p>只读属性：</p>
<pre><code class="copyable">class Person&#123;
 public readonly _name:string
 constructor(name:string) &#123;
  this._name = name
 &#125;
&#125;
const person = new Person('jeskson');
console.log(person.name);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>抽象类，使用继承抽象类：</p>
<pre><code class="copyable">abstract class Da &#123;
 abstract say()
&#125;
class da extends Da &#123;
 say() &#123;
  console.log('jeskson')
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>tsc -init</code>生成<code>tsconfig.json</code>文件：</p>
<p><code>compilerOptions</code>配置项</p>
<pre><code class="copyable">"files": []

removeComments 为 true，去掉注释
strict为true，书写规范

// 允许你的注解类型any不用特意标明
"noImplicitAny": true

// 不允许有null值出现
"strictNullChecks": true

// 入口文件
"rootDir": "./src"
// 编译好的文件
"outDir": "./build"

// Generates corresponding '.map' file
// 信息文件，存储位置信息
"sourceMap": true

// Report errors on unused locals
"noUnusedLocals": true
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">联合类型和类型保护</h3>
<pre><code class="copyable">interface Teacher&#123;
 teacher: boolean;
 say:()=>&#123;&#125;
&#125;
interface Student&#123;
 teacher: boolean;
 say:()=>&#123;&#125;
&#125;

//联合类型，类型保护，类型断言
function da(study: Teacher | Student) &#123;
 if(study.teacher) &#123;
  (study as Teacher).say();
 &#125;else&#123;
  (study as Student).say();
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">泛型</h3>
<pre><code class="copyable">function fn<T>(params: Array<T>)&#123;
 return params;
&#125;
fn<string>(["12","123"]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用：</p>
<pre><code class="copyable">class Select &#123;
 constructor(private da: string[]) &#123;&#125;
 getDa(index:number):string&#123;
  return this.da[index];
 &#125;
&#125;
const dada = new Select(["1","2","3"]);
onsole.log(dada.getDa(1));
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">class Select<T> &#123;
 constructor(private da: T[])&#123;&#125;
 getDa(index: number): T&#123;
  return this.da[index];
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">interface Girl &#123;
 name: string;
&#125;
class SelectGirl<T extends Girl> &#123;
 constructor(private girls: T[]) &#123;&#125;
 getGirl(index: number): string &#123;
  return this.girls[index].name;
 &#125;
&#125;

class SelectGirl<T extends number | string> &#123;
 constructor(private girls: T[]) &#123;&#125;
 getGirl(index: number): T &#123;
  return this.girls[index];
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">NameSpace</h3>
<p><code>npm init -y</code>生成<code>package.json</code>文件</p>
<p><code>tsc -init</code>生成<code>tsconfig.json</code>文件</p>
<blockquote>
<p>安装VsCode编辑器：</p>
</blockquote>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e45eaf9cdd54ceaa0dadaa7937fa890~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">interface Person &#123;
 name: string
&#125;
const teacher: Person = &#123;
 name: 'jeskson'
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>基础类型和对象类型</p>
</blockquote>
<pre><code class="copyable">// 基础类型 null, undefined, symbol, boolean, void
const count:number = 12;
const name:string = '掘金魔王哪吒';

// 对象类型
const teacher: &#123;
 name: string;
 age: number;
&#125; = &#123;
 name: 'jeskson',
 age: 12
&#125;;

const nums:number[] = [1,2,3]

const goTotal: ()=>number = () => &#123;
 return 123;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>类型注解和类型推断</p>
</blockquote>
<pre><code class="copyable">// type annotation 类型注解

let count:number;
count=123;

// type inference 类型推断，TS会自动的尝试分析变量的类型
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// 推动不出来，就自己加
function getTotal(firstNumber:number, secondNumber:number) &#123;
 return firstNumber + secondNumber;
&#125;
const total = getTotal(1,2);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>函数相关类型</p>
</blockquote>
<pre><code class="copyable">// 实战
function getTotal(firstNumber:number, secondNumber:number):number &#123;
 return firstNumber + secondNumber;
&#125;
const total = getTotal(1,2);

// void这个函数不应该有返回值
function sayHello(): void &#123;
 console.log('hello');
&#125;

// never 表示这个函数永远不能执行完成
function errorEmitter(): never &#123;
 while(true)&#123;&#125; // 或抛出异常
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">function add(&#123;first,second&#125;:&#123;first:number;second:number&#125;):number&#123;
 return first+second;
&#125;
function getNumber(&#123;first&#125;:&#123;first:number&#125;)&#123;
 return first;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>小结：</p>
<pre><code class="copyable">// 基础类型 boolean,number,string,void,undefined,symbol,null

let count: number;
count = 12;

// 对象类型 &#123;&#125;,Class,function,[]
const fun = (str:string) => &#123;
 return parseInt(str,10);
&#125;
const fun1: (str:string)=>number = (str) => &#123;
 return parseInt(str,10);
&#125;

const date = new Date();
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>数组和元组</p>
</blockquote>
<pre><code class="copyable">const arr: (number|string)[] = [1,'2',3];
const stringArr: string[] = ['a','b','c'];
const undefinedArr:undefined[] = [undefined];

const objectArr: &#123;name:string,age:number&#125;[] = [&#123;
 name: '掘金魔王哪吒',
 age: 12
&#125;]

// type alias 类型别名
type User = &#123;name:string;age:number&#125;;
const objectArr: User[] = [&#123;
 name: '掘金魔王哪吒',
 age: 12
&#125;]

class Teacher &#123;
 name: string;
 age: number;
&#125;
const objectArr: Teacher[] = [
 new Teacher();
 &#123;
  name: 'jeskson',
  age: 12
 &#125;
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>元组</p>
<pre><code class="copyable">const teacherInfo: [string, string, number] = ['dadaqianduan','1024bibi.com',12];
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>Interface接口</p>
</blockquote>
<pre><code class="copyable">interface Person &#123;
 // readonly name: string;
 name: string;
 age?: number;
&#125;
const getPersonName = (person: Person): void => &#123;
 console.log(person.name);
&#125;;
const setPersonName = (person: Person, name: string): void=>&#123;
 persono.name = name;
&#125;;
const person = &#123;
 name: '掘金魔王哪吒',
 age: 12
&#125;;
getPersonName(person);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>类的定义与继承</p>
</blockquote>
<pre><code class="copyable">class Person &#123;
 name='掘金魔王哪吒';
 getName() &#123;
  return this.name;
 &#125;
&#125;
class Teacher textends Person &#123;
 getTeacherName() &#123;
  return 'teacher';
 &#125;
 getName() &#123;
  return '1024bibi.com' + super.getName()
 &#125;
&#125;

const teacher = new Teacher();
// 重写，字类可以重写父类的东西
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>类中的访问类型和构造器</p>
</blockquote>
<pre><code class="copyable">// private protected public 
class Person &#123;
 public name: string;
 sayHi() &#123;
  console.log('1024bibi.com')
 &#125;
&#125;
const person = new Person();
person.name = '掘金魔王哪吒'
console.log(person.name);

// public 允许我在类的内外被调用
// private 允许在类内被使用
// protected 允许在类内以及继承的子类中是使用
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>constructor</code></li>
</ul>
<pre><code class="copyable">class Person &#123;
 public name: string;
 constructor(name: string) &#123;
  this.name = name;
 &#125;
&#125;

const person = new Person('dadaqianduan');
console.log(person.name);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// 简化写法
class Person &#123;
 constructor(public name: string) &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">class Teacher extends Person &#123;
 constructor(public age:number) &#123;
  super('dadaqianduan');
 &#125;
&#125;

// 如果父类没有构造器，也使用空的 super()
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>静态属性，Setter和Getter</p>
</blockquote>
<pre><code class="copyable">class Person &#123;
 constructor(private name: string) &#123;&#125;
 get getName() &#123;
  return this.name;
 &#125;
&#125;

const person = new Person('dadaqianduan');
console.log(person.getName);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">class Person &#123;
 constructor(private _name: string) &#123;&#125;
 get name() &#123;
  return this._name;
 &#125;
 set name(name: string) &#123;
  this._name = name;
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设计模式：单例模式，一个类只允许通过这个类，获取一个单例实例</p>
<pre><code class="copyable">class Demo &#123;
 private static instance: Demo;
 private constructor(public name:string) &#123;&#125;
 
 static getInstance(name: string) &#123;
  if(!this.instance) &#123;
   this.instance = new Demo('1024bibi.com');
  &#125;
  return this.instance;
 &#125;
&#125;

//const demo1 = new Demo();
//const demo2 = new Demo();

const demo1 = Demo.getInstance();
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>抽象类</p>
</blockquote>
<p>抽象类只能被继承，不能被实例化</p>
<pre><code class="copyable">abstract class Da &#123;
 width: number;
 getType() &#123;
  return 'dadaqianduan';
 &#125;
 abstract getAra(): number;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">npm init -y
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成<code>package.json</code>文件：</p>
<pre><code class="copyable">&#123;
 "name": "TypeScript",
 "version": "1.0.0",
 "description": "",
 "main": "index.js",
 "scripts": &#123;
  "test: "echo \"Error: no test specified\" && exit 1"
 &#125;,
 "keywords": [],
 "author": "",
 "license": "ISC"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">tsc --init
// Successfully created a tsconfig.json file

// npm uninstall ts-node -g
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">npm install -D ts-node
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">npm install typescript -D
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">TypeScript中的配置文件</h3>
<pre><code class="copyable">// 编译配置文件
// tsconfig.json
要编译的文件
"include" ["./demo.ts"],
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">联合类型和类型保护</h3>
<pre><code class="copyable">interface Bird &#123;
 fly: boolean;
 sing: ()=>&#123;&#125;;
&#125;
interface Dog &#123;
 fly: boolean;
 bark: ()=>&#123;&#125;;
&#125;
// 类型断言的方式
function trainAnial(animal: Bird | Dog) &#123;
 if(animal.fly) &#123;
  (animal as Bird).sing();
 &#125; else &#123;
  (animal as Dog).bark();
 &#125;
&#125;

// in 语法来做类型保护
function trainAnialSecond(animal: Bird | Dog) &#123;
 if('sing' in animal) &#123;
  animal.sing();
 &#125; else &#123;
  animal.bark();
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// typeof 语法来做类型保护
function add(first: string | number, second: string | number) &#123;
 if(typeof first === 'string' || typeof second === 'string') &#123;
  return `$&#123;first&#125;$&#123;second&#125;`;
 &#125;
 return first + second;
&#125;

// 使用instanceof语法来做类型保护
class NumberObj &#123;
 count: number;
&#125;

function addSecond(first: object | NumberObj, second: object | NumberObj) &#123;
 if(first instanceof NumberObj && second instanceof NumberObj) &#123;
  return first.count + second.count;
 &#125;
 return 0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">Enum枚举类型</h3>
<pre><code class="copyable">const Status = &#123;
 OFFLINE: 0,
 ONLINE: 1,
 DELETED: 2
&#125;
function getResult(status) &#123;
 if(status === Status.OFFLINE)&#123;
  return 'offline';
 &#125;else if(status === Status.ONLINE) &#123;
  return 'online';
 &#125;else if(status === Status.DELETED) &#123;
  return 'deleted';
 &#125;
 return 'error';
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">enum Status &#123;
 OFFLINE,
 ONLINE,
 DELETED2
&#125;
function getResult(status) &#123;
 if(status === Status.OFFLINE)&#123;
  return 'offline';
 &#125;else if(status === Status.ONLINE) &#123;
  return 'online';
 &#125;else if(status === Status.DELETED) &#123;
  return 'deleted';
 &#125;
 return 'error';
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">函数泛型</h3>
<pre><code class="copyable">// 泛型generic泛指的 类型
function join<T,P>(first: T, second: P) &#123;
 return `$&#123;first&#125;$&#123;second&#125;`;
&#125;
function anotherJoin<T>(first: T,second: T): T &#123;
 return first;
&#125;

// T[]
function map<T>(params: Array<T>) &#123;
 return params;
&#125;
// join<number,string>(1,'1');
// map<string>(['123']);
join(1,'1');
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">类中如何使用泛型</h3>
<pre><code class="copyable">interface Item &#123;
 name: string;
&#125;
class DataManager<T extends Item> &#123;
 constructor(private data: T[]) &#123;&#125;
 getItem(index: number):string &#123;
  return this.data[index].name;
 &#125;
&#125;

const data = new DataManager(&#123;
 &#123;
  name: 'jeskson'
 &#125;
]&#125;;

// 用泛型可以声明一些类型：
// 如何使用泛型作为一个具体的类型注解
function hello<T>(params: T) &#123;
 return params;
&#125;
const func: <T>(param: T) => T = hello;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">命名空间</h3>
<pre><code class="copyable">"use strict"
var Header = (function() &#123;
 function Header() &#123;
  var elem = document.createElement('div');
  elem.innerText = 'This is Header';
  document.body.appendChild(elem);
 &#125;
 return Header;
&#125;());

var Content = (function()=>&#123;
 function Content() &#123;
  var elem = document.createElement('div');
  elem.innerText = 'This is Content';
  document.body.appendChild(elem);
 &#125;
 return Content
&#125;());
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">使用Parcel打包TS代码</h3>
<pre><code class="copyable">yarn add --dev parcel@next
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">泛型中keyof语法的使用</h3>
<blockquote>
<p>某一数据类型的key的数组集合，既适用于数组，也适用于对象</p>
</blockquote>
<pre><code class="copyable">interface testInter &#123;
    name: string,
    age: number
&#125;
let testArr: string[] = ['dada', 'dada1'];
let testObj: testInter = &#123;name: 'tate', age: 26&#125;

// 数组
function showKey<K extends keyof T, T> (key: K, obj: Array<string>) &#123;
    return key;
&#125;
showKey<number, Array<string>>(1, testArr);

// 对象
function showKey<K extends keyof T, T> (keyItem: K, obj: T): K &#123;
    return keyItem;
&#125;
let val = showKey('name', testObj)

function showKey<K extends keyof T, T> (items: K[], obj: T): T[K][] &#123;
    return items.map(item => obj[item])
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">interface Person &#123;
 name: string;
 age: number;
 gender: string;
&#125;
class Teacher &#123;
 constructor(private info: Person) &#123;&#125;
 getInfo(key: string) &#123;
  if(key==='name' || key==='age' || key==='gender') &#123;
   return this.info[key];
  &#125;
 &#125;
&#125;
 
const teacher = new Teacher(&#123;
 name: 'jeskson',
 age: 12,
 gender: 'male'
&#125;);
const test = teacher.genInfo('name');
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">class Teacher &#123;
 constructor(private info: Person) &#123;&#125;
 // getInfo<T extends keyof Person>(key:string) &#123;
 getInfo<T extends keyof Person>(key: T):Person[T]&#123;
  return this.info[key];
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">装饰器</h3>
<pre><code class="copyable">// 类的装饰器
// 装饰器本身是一个函数
// 装饰器通过@符号来使用
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// 普通方法，target对应的是类的prototype
// 静态方法，target对应的是类的构造函数
function getNameDecorator(target:any,key:string)&#123;
 console.log(target,key);
&#125;
class Test &#123;
 name: string;
 constructor(name: string)&#123;
  this.name = name;
 &#125;
 @getNameDecorator
 static getName() &#123;
  return '123';
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">接口Interface</h3>
<p>有时候我们传入的参数可能会包含很多的属性，但编译器只会检查那些必须的属性是否存在，以及类型是否匹配，而接口就是用来描述这样的结构。</p>
<pre><code class="copyable">function Person(config: &#123;name:string,age:number&#125;) &#123;
 console.log(config.name+config.age);
&#125;
console.log(Person(&#123;name:'魔王哪吒',age:12&#125;));
// 重构
interface Config &#123;
 name: string;
 age: number;
&#125;
function Person(config: Config) &#123;
 console.log(config.name+config.age);
&#125;
// 接口类型检查会检测属性有没有在Config接口中而进行限制
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>可选属性</p>
</blockquote>
<p>接口中的属性有时候是不必须的，有的用得到，有的用不到的情况下，是可选属性，这样对可能存在的属性进行预先定义。</p>
<pre><code class="copyable">interface Config &#123;
 name: string;
 age?: number;
 // [propName: string]: any 转字符串索引签名
&#125;
// [propName: string]: any
// 这个索引签名是为了你能够预见某个对象可能有某些特殊的用途而准备的
// 属性名写错，可以通过索引签名的方式进行屏蔽错误
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>只读属性</p>
</blockquote>
<p>对于一些对象属性只能在对象刚刚创建的时候修改其值，在属性前用readonly来指定只读属性：</p>
<pre><code class="copyable">interface Point &#123;
  readonly x: number;
  readonly y: number;
&#125;
let p:Point = &#123; x: 12, y: 14 &#125;
p.x = 15 // 错误
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>函数类型</p>
</blockquote>
<p>接口能够描述JavaScript中对象拥有的各种各样的外形</p>
<p>函数类型接口：</p>
<pre><code class="copyable">interface Fun &#123;
 (source: string, subString: string): Boolean
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>接口继承</p>
</blockquote>
<p>接口是可以相互继承的，能够从一个接口里复制成员到另一个接口里。</p>
<pre><code class="copyable">interface Animal &#123;
 name: string;
 say(): void;
&#125;
interface Person extends Animal &#123;
 work(): void;
 closer: string;
&#125;
class Pro implements Person &#123;
 closer: string;
 name: string;
 say(): void &#123;
 
 &#125;
 work(): void &#123;
 
 &#125;
 constructor(name:string, closer:string) &#123;
  this.name = name;
  this.closer = closer;
 &#125;
&#125;
let g:Person = new Pro("jeskson","it");
g.say();
g.work();
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>对象类型接口</li>
<li>函数类型接口</li>
</ul>
<p>接口的定义方式：使用interface关键字</p>
<p>接口中可定义：</p>
<ul>
<li>确定属性</li>
<li>可选属性</li>
<li>任意属性</li>
<li>只读属性</li>
</ul>
<ol>
<li>确定属性</li>
</ol>
<pre><code class="copyable">interface UserInfo &#123;
 name: string;
 age: number;
&#125;

const myInfo: UserInfo = &#123;
 name: '魔王哪吒',
 age: 12
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>接口中约束好的确定属性，定义对象变量的时候，不能少，也不能多🙅‍</p>
</blockquote>
<ol start="2">
<li>可选属性</li>
</ol>
<pre><code class="copyable">interface UserInfo &#123;
 name: string;
 age: number;
 sex?: string;
&#125;

const myInfo: UserInfo = &#123;
 name: '魔王哪吒',
 age: 12
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>接口中的可选属性，是表示在对象变量中可以不存在</p>
</blockquote>
<ol start="3">
<li>任意属性</li>
</ol>
<pre><code class="copyable">interface UserInfo &#123;
 name: string;
 age: number;
 sex?: string;
 [proName: string]: any;
&#125;

const myInfo: UserInfo = &#123;
  name: "dadaqianduan",
  age: 12,
  test1: '123',
  test2: 'abc',
  test3: 123
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>一旦定义了任意属性，那么确定属性和可选属性的类型都必须是任意属性类型的子类，定义了任意属性后，对象变量中的属性个数才可以出现比接口的属性数量多的情况。</p>
</blockquote>
<ol start="4">
<li>只读属性</li>
</ol>
<pre><code class="copyable">interface UserInfo &#123;
  readonly id: number;
  name: string;
  age: number;
  sex?: string;
  [propName: string]: any;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">const myInfo: UserInfo = &#123;
  id: 1,
  name: "dada",
  age: 12,
  test1: "123",
  test2: "abc",
  test3: 123
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>只读属性，也是确定属性，在对象变量定义的时候必须有值，后面不能修改</p>
</blockquote>
<ul>
<li>对象接口，以查询商品列表接口API示例：</li>
</ul>
<pre><code class="copyable">interface ResponseData &#123;
    resCode: number;
    resData: ResultData[];
    message: string;
&#125;

interface ResultData &#123;
    productId: number;
    productName: string;
&#125;

let resultData = &#123;
    resCode: 0,
    resData: [
        &#123; productId: 1, productName:"TypeScipt实战" &#125;,
        &#123; productId: 2, productName:"TypeScipt从入门到精通" &#125;,
    ],
    message: "success"
&#125;

function render(res: ResponseData) &#123;
    console.log(res.resCode, res.message)
    res.resData.forEach((obj) => &#123;
        console.log(obj.productId, obj.productName)
    &#125;)
&#125;

render(resultData);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>只要传入的对象满足接口的必要条件就可以被允许,即使传入多余的字段也可以通过类型检查</p>
</blockquote>
<ul>
<li>绕过检查的方法有3种:</li>
</ul>
<ol>
<li>将对象字面量赋值给一个变量</li>
</ol>
<pre><code class="copyable">let result = &#123;
    resCode: 0,
    resData: [
        &#123; productId: 1, productName:"TypeScipt实战", remark: "备注"&#125;,
        &#123; productId: 2, productName:"TypeScipt从入门到精通" &#125;,
    ],
    message: "success"
&#125;
render(result)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>使用类型断言</li>
</ol>
<blockquote>
<p>使用类型断言方式,明确告诉编译器类型是什么,编译器就会绕过类型检查</p>
</blockquote>
<pre><code class="copyable">render(&#123;
    resCode: 0,
    resData: [
        &#123; productId: 1, productName:"TypeScipt实战", remark:""&#125;,
        &#123; productId: 2, productName:"TypeScipt从入门到精通" &#125;,
    ],
    message: "success"
&#125; as ResponseData)

render(<ResponseData>&#123;
    resCode: 0,
    resData: [
        &#123; productId: 1, productName:"TypeScipt实战", remark: "备注"&#125;,
        &#123; productId: 2, productName:"TypeScipt从入门到精通" &#125;,
    ],
    message: "success"
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>使用字符串索引签名</li>
</ol>
<pre><code class="copyable">interface ResultData &#123;
    productId: number;
    productName: string;
    [remark: string]: any;  // 字符串索引签名
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>函数接口</p>
</blockquote>
<ul>
<li>函数定义方式：</li>
</ul>
<ol>
<li>在TS中，使用一个变量直接定义函数</li>
</ol>
<pre><code class="copyable">let add: (x: number, y: number) => number
= (x, y)&#123;
  return x+y;
&#125;;
add(1,2)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>使用接口定义函数</li>
</ol>
<pre><code class="copyable">interface Add &#123;
    (x: number, y: number): number
&#125;
let myFunc: Add = function(x, y)&#123;
  return x+y;
&#125;;
myFunc(1,2);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>使用类型别名来定义函数</li>
</ol>
<p>类型别名使用type关键字</p>
<pre><code class="copyable">type Add = (x: number, y: number) => number
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>可索引类型的接口</p>
</blockquote>
<pre><code class="copyable">// 数字索引接口
interface numberIndex &#123;
    [x: number]: string
&#125;
// 相当于声明了一个字符串类型的数组
let chars: numberIndex = ['A', 'B']
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// 声明一个字符串索引类型的接口
interface stringIndex &#123;
    [x: string]: string
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// 两种索引签名混用
interface stringIndex &#123;
    [x: string]: string
    [z: number]: number    // // Numeric index type 'number' is not assignable to string index type 'string'.
&#125;

interface stringIndex &#123;
    [x: string]: any
    [z: number]: number // Numeric index type 'number' is not assignable to string index type 'string'.
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">上手TypeScipt</h3>
<p>对于npm的用户</p>
<pre><code class="copyable">npm install -g typescript
<span class="copy-code-btn">复制代码</span></code></pre>
<p>构建第一个TypeScript文件，dada.ts 文件：</p>
<pre><code class="copyable">function dada(person) &#123;
 return "hello" + person;
&#125;
let user = "jeskson";
document.body.innerHTML = dada(uer);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>编译代码</p>
</blockquote>
<p>在命令行上，运行TypeScript编译器：</p>
<pre><code class="copyable">tsc dada.ts
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>添加类型注解<code>: string</code></p>
</blockquote>
<pre><code class="copyable">function dada(person: string) &#123;
 return "jeskson"+person;
&#125;
let user = "jeskson";
document.body.innerHTML = dada(user);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>类型注解</p>
</blockquote>
<p>TypeScript里的类型注解是一种轻量级的为函数或变量添加约束的方式。</p>
<p>接口</p>
<p>允许我们在实现接口的时候只要保证包含了接口要求的结构就可以</p>
<pre><code class="copyable">// implements语句
interface Person &#123;
 firstName: string;
 lastName: string;
&#125;

function func(peson: Person) &#123;
 return person.firstName + person.lastName;
&#125;

let user = &#123; firstName: "jeskson", lastName: "User" &#125;;

document.body.innerHTML = func(user);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类，支持基于类的面向对象编程</p>
<pre><code class="copyable">class Student &#123;
 fullName: string;
 constructor(public firstName: string, public lastName: string) &#123;
  this.fullName = firstName + lastName;
 &#125;
&#125;

interface Person &#123;
 firstName: string;
 lastName: string;
&#125;

function dada(person: Person) &#123;
 return person.firstName+person.lastName;
&#125;

let user = new Student("jeskson","魔王哪吒");
document.body.innerHTML = dada(user);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>运行TypeScript Web应用</p>
</blockquote>
<p>在<code>index.html</code>里输入内容:</p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
    <head><title>TypeScript dada</title></head>
    <body>
        <script src="dada.js"></script>
    </body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25">对象</h3>
<p>在JS中,可以任意修改对象属性,TS中不允许</p>
<pre><code class="copyable">// 这是因为,仅声明了对象obj的类型注解是object
let obj: object = &#123;x: 'a', y: 'b'&#125;
obj.x = 3    // Property 'x' does not exist on type 'object'.
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">let obj: &#123;x: string, y: string&#125; = &#123;x: 'a', y: 'b'&#125;
obj.x = 'c'
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">Symbol</h3>
<p>具有唯一的值,可以显式声明,也可直接创建</p>
<pre><code class="copyable">let symbol1: Symbol = Symbol()  // 显示声明
let symbol2 = Symbol()  // 直接创建

// 验证:是否是同一个对象
console.log(symbol1 === symbol2)    // fasle
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-27">undefined 和 null</h3>
<pre><code class="copyable">// 一旦声明了undefined,就不能再被赋值为任何其他的数据类型了
let udf: undefined = undefined
let nu: null = null

let undf: undefined = 1 
// Type '1' is not assignable to type 'undefined'.

// 默认情况下,undefined和null也不能被赋值给任何其他类型

let num1: number = undefined    
// Type 'undefined' is not assignable to type 'number'.

let num2: number = null 
// Type 'null' is not assignable to type 'number'.
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在TS中,<code>undefined和null</code>是任何类型的子类型,所以可以被赋值给其他类型</li>
<li>设置允许被赋值为其他类型</li>
</ul>
<blockquote>
<p>打开<code>tsconfig.js,将strictNullChecks = false(默认true)</code></p>
</blockquote>
<h3 data-id="heading-28"><code>void,any,never</code></h3>
<ul>
<li>在<code>js</code>中,<code>void</code>操作符可以使任何一个表达式返回<code>undefined</code></li>
<li><code>void 0 // 将返回undefined</code></li>
</ul>
<pre><code class="copyable">// void
let voidFunc = () => &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>any</code>:如果不指定<code>TS</code>的变量类型,默认为<code>any</code>类型,可以赋值为任何类型</li>
<li><code>never</code>:永远不会有返回值的类型</li>
</ul>
<pre><code class="copyable">// 函数抛出异常,永远不会有返回值,类型为never
let error = () => &#123;
    throw new Error('error')
&#125;

// 死循环函数永远没有返回值,类型为never
let endless = () => &#123;
    while(true) &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-29">对数组中的对象按对象的值进行去重</h3>
<pre><code class="copyable">let listData = [
  &#123; firstName: "dada", lastName: "abc", size: 18 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">//js
let obj = &#123;&#125;;
listData = listData.reduce((item, next) => &#123;
  if (!obj[next.lastName]) &#123;
    item.push(next);
    obj[next.lastName] = true;
  &#125;
  return item;
&#125;, []);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">//ts
const obj: &#123;[key: string]: boolean;&#125; = &#123;&#125;;
listData = listData.reduce<ListDataItem[]>((item, next) => &#123;
  if (!obj[next.lastName]) &#123;
    item.push(next);
    obj[next.lastName] = true;
  &#125;
  return item;
&#125;,[]);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-30">在微信小程序开发中使用<code>Typescript</code></h3>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80c267b51415499e9e0d2537446b7e04~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5452e288b2348a9a33bfac2e2010969~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ddd5e782a0745808370946543680af8~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f3e2ebef36e4527b6bb2095c8e245db~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-31">模块的概念</h3>
<p>“内部模块”现在称为“命令空间”，“外部模块”现在简称为“模块”，模块字其自身的作用域里执行，而不是在全局作用域里。</p>
<p>这意味着定义在一个模块里的变量，函数，类等等在模块外部是不可见的，除非你明确地使用export形式之一导出它们。</p>
<p>相反，如果想使用其它模块导出的变量，函数，类，接口等的时候，你必须要导入它们，可以使用 <code>import</code> 形式之一。</p>
<p>模块的概念：</p>
<p>我们可以把一些公共的功能单独抽离成一个文件作为一个模块，模块里面的变量，函数，类等默认是私有的，如果我们要在外部访问模块里面的数据，我们需要通过<code>export</code>暴露模块里面的数据。暴露后使用<code>import</code>引入模块就可以使用模块里面暴露的数据。</p>
<h3 data-id="heading-32">命名空间</h3>
<p>命名空间和模块的区别</p>
<ul>
<li>命名空间：内部模块，主要用于组织代码，避免命名冲突</li>
<li>模块：ts的外部模块的简称</li>
</ul>
<pre><code class="copyable">namespace A &#123;
interface Animal &#123;
 name: string;
 eat(): void;
&#125;
class Dog implements Animal &#123;
 name: string;
 constructor(theName: string) &#123;
  this.name = theName;
 &#125;
 eat() &#123;
  console.log('dog');
 &#125;
&#125;
class Cat implements Animal &#123;
 name: string;
 constructor(theName: string) &#123;
  this.name = theName;
 &#125;
 eat() &#123;
  console.log('cat');
 &#125;
&#125;
let dog = new Dog('dogdog');
dog.eat();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">import &#123;A,B&#125; from './modules/animal';

var dog = new A.Dog('hei');
dog.eat();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-33">装饰器</h3>
<p>装饰器是一种特殊类型的声明，它能够被附加到类声明，方法，属性或参数上，可以修改类的行为。</p>
<p>通俗的讲装饰器就是一个方法，可以注入到类，方法，属性参数上扩展类，属性，方法，参数的功能。</p>
<p>常见的装饰器有：<strong>类装饰器，属性装饰器，方法装饰器，参数装饰器</strong></p>
<p>装饰器的写法：</p>
<ul>
<li>普通装饰器（无法传参）</li>
<li>装饰器工厂（可传参）</li>
</ul>
<blockquote>
<p>方法参数装饰器：</p>
</blockquote>
<p>参数装饰器表达式会在运行时当作函数被调用，可以使用参数装饰器为类的原型增加一些元素数据，传入下列3个参数：</p>
<ul>
<li>对于静态成员来说是类的构造函数，对于实例成员是类的原型对象</li>
<li>方法的名字</li>
<li>参数在函数参数列表中的索引</li>
</ul>
<pre><code class="copyable">function logParams(params:any)&#123;
 return function(target:any,methodName:any,paramsIndex:any)&#123;
  console.log(params);
  console.log(target);
  console.log(methodName);
  console.log(paramsIndex);
 &#125;
&#125;
class HttpClient&#123;
 public url:any|undefined;
 constructor()&#123;&#125;
 getDate(@logParams('xxx') uuid:any)&#123;
  console.log(uuid);
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-34">keyof</h3>
<pre><code class="copyable">keyof与Object.keys相似，keyof取interface的键
interface Point &#123;
 x: number;
 y: number;
&#125;
// type keys = "x" | "y"
type keys = keyof Point;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// 无法确认返回类型
// 无法对 key 做约束
const data = &#123;
 a: 1,
 b: 2
&#125;

function get(o: object, name: string) &#123;
 return o[name]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用keyof：</p>
<pre><code class="copyable">function get<T extends object, K extends keyof T>(o: T, name: K): T[K] &#123;
  return o[name]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-35"><code>?: 运算符</code></h3>
<pre><code class="copyable">T extends U ? X : Y

type isTrue<T> = T extends true ? true : false
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-36"><code>tsconfig.json</code></h3>
<p><code>tsconfig.json</code>文件中指定了用来编译这个项目的根文件和编译选项</p>
<p><code>tsconfig.json</code>示例文件:</p>
<pre><code class="copyable">//"compilerOptions"可以被忽略，这时编译器会使用默认值。
//使用"files"属性
//"files"指定一个包含相对或绝对文件路径的列表。
&#123;
    "compilerOptions": &#123;
        "module": "commonjs",
        "noImplicitAny": true,
        "removeComments": true,
        "preserveConstEnums": true,
        "sourceMap": true
    &#125;,
    "files": [
        "core.ts",
        "sys.ts",
        "types.ts",
        "scanner.ts",
        "parser.ts",
        "utilities.ts",
        "binder.ts",
        "checker.ts",
        "emitter.ts",
        "program.ts",
        "commandLineParser.ts",
        "tsc.ts",
        "diagnosticInformationMap.generated.ts"
    ]
&#125;
//使用"include"和"exclude"属性
//如果"files"和"include"都没有被指定，编译器默认包含当前目录和子目录下所有的TypeScript文件
//排除在"exclude"里指定的文件
&#123;
    "compilerOptions": &#123;
        "module": "system",
        "noImplicitAny": true,
        "removeComments": true,
        "preserveConstEnums": true,
        "outFile": "../../built/local/tsc.js",
        "sourceMap": true
    &#125;,
    "include": [
        "src/**/*"
    ],
    "exclude": [
        "node_modules",
        "**/*.spec.ts"
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>查看模式: <a href="http://json.schemastore.org/tsconfig" target="_blank" rel="nofollow noopener noreferrer">json.schemastore.org/tsconfig</a>.</p>
<h3 data-id="heading-37">回看笔者往期高赞文章，也许能收获更多喔！</h3>
<ul>
<li><a href="https://juejin.cn/post/6951545839307194375" target="_blank">JS葵花宝典秘籍笔记，为你保驾护航金三银四</a></li>
<li><a href="https://juejin.cn/post/6950052678927908901" target="_blank">TypeScript趁早学习提高职场竞争力</a></li>
<li><a href="https://juejin.cn/post/6925197705832562696" target="_blank">一个合格的初级前端工程师需要掌握的模块笔记</a></li>
<li><a href="https://juejin.cn/post/6948576107163549732" target="_blank">前端模拟面试字数过23477万内容</a></li>
<li><a href="https://juejin.cn/post/6916664414422695949" target="_blank">Vue.js笔试题解决业务中常见问题</a></li>
<li><a href="https://juejin.cn/post/6923946134025191432" target="_blank">【初级】个人分享Vue前端开发教程笔记</a></li>
<li><a href="https://juejin.cn/post/6844904078934278158" target="_blank">长篇总结之JavaScript，巩固前端基础</a></li>
<li><a href="https://juejin.cn/post/6844904067764846600" target="_blank">前端面试必备ES6全方位总结</a></li>
<li><a href="https://juejin.cn/post/6913480482638266382" target="_blank">达达前端个人web分享92道JavaScript面试题附加回答</a></li>
<li><a href="https://juejin.cn/post/6844904117337341959" target="_blank">【图文并茂，点赞收藏哦！】重学巩固你的Vuejs知识体系</a></li>
<li><a href="https://juejin.cn/post/6844904106243391495" target="_blank">【思维导图】前端开发-巩固你的JavaScript知识体系</a></li>
<li><a href="https://juejin.cn/post/6850037263116a533773" target="_blank">14期-连肝7个晚上，总结了计算机网络的知识点！（共66条）</a></li>
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
<h3 data-id="heading-38">点赞、收藏和评论</h3>
<p>我是<code>Jeskson</code>(达达前端)，感谢各位人才的：<strong>点赞、收藏和评论</strong>，我们下期见！(如本文内容有地方讲解有误，欢迎指出☞<strong>谢谢，一起学习了</strong>)</p>
<h3 data-id="heading-39">我们下期见！</h3>
<blockquote>
<p>文章持续更新，可以微信搜一搜「 <strong>程序员哆啦A梦</strong> 」第一时间阅读，回复【资料】有我准备的一线大厂资料，本文 <a href="https://www.1024bibi.com/" target="_blank" rel="nofollow noopener noreferrer">www.1024bibi.com</a> 已经收录</p>
</blockquote>
<blockquote>
<p><code>github</code>收录，欢迎<code>Star</code>：<a href="https://github.com/webVueBlog/WebFamily" target="_blank" rel="nofollow noopener noreferrer">github.com/webVueBlog/…</a></p>
</blockquote>
<ul>
<li><a href="https://juejin.cn/post/6952060423759724581#heading-0" target="_blank">技术创作者们，快来这里交作业啦 | 创作者训练营第二期</a></li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            