
---
title: '事关我对于JavaScript高级的一些理解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2291'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 23:00:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=2291'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Javascript</h1>
<p>写在前面:这一篇是我总结的关于JavaScript高级的一些知识,包括但不限于ES6范围内,而且也基本都是面试用得上的知识</p>
<h2 data-id="heading-1">Promise和async await</h2>
<h3 data-id="heading-2">Promise定义</h3>
<ol>
<li>三种状态,不可逆,两个参数,成功回调,失败回调.then也是这两个参数</li>
<li>.then不传值,则为undefined,传普通数据,则为下一个函数的参数,传promise对象,则把异步结果作为参数传递</li>
<li>如果不设置失败回调,错误无法抛出,一般在最后设置一个.catch用来错误捕获 , 不会因此阻塞代码执行.</li>
<li>Promise.resolve 返回一个成功Promise,reject相反</li>
<li>Promise.all(),等待所有结束,有一个失败,就算失败</li>
<li>Promise.race(),等待最快的返回结果,最快的是什么,race就是什么</li>
<li>Promise.finally(),不管结果如何都会执行</li>
</ol>
<h3 data-id="heading-3">Promise的理解</h3>
<h4 data-id="heading-4">优点:</h4>
<p>异步代码同步化解决方案,可以将异步操作以同步操作的流程表达出来，避免了层层嵌套的回调函数,顺带解决了回调地狱的代码.(真正解决要靠async和await,他是Promise和Generator函数的语法糖,async函数包裹异步请求函数得到返回值操作才能跳出回调地狱.)</p>
<h4 data-id="heading-5">缺点:</h4>
<p>首先它状态不能被改变,其次如果处于pending状态,无法得知它是刚开始还是要结束,还有是如果没有回调函数,promise内部抛出的错误，不会反应到外部.</p>
<h3 data-id="heading-6">Promise/A+规范</h3>
<ol>
<li>promise表示异步操作的最终结果(状态) , 是一个包含了promise规范的then方法的对象或者函数.</li>
<li>必须要有个值响应当前promise的状态 , pengding(等待) , fulfilled(成功) , rejected(失败)</li>
<li>then方法需要可以被链式调用 , 因此需要返回一个promise对象</li>
<li>exception, 表示抛出的错误.</li>
<li>reason , 表示被拒绝的原因.</li>
</ol>
<h2 data-id="heading-7">执行上下文,执行上下文栈和作用域</h2>
<h3 data-id="heading-8">执行上下文</h3>
<blockquote>
<p>js代码预编译 , var变量提升,函数声明以及this赋值.</p>
</blockquote>
<ol>
<li>声明时确定自由变量的作用域</li>
<li>每次函数调用都会有新的执行上下文环境,因为函数相同,参数不同</li>
</ol>
<h3 data-id="heading-9">执行上下文栈</h3>
<blockquote>
<p>活跃的执行上下文只能有一个 , 多层嵌套形成先进后出的栈.</p>
</blockquote>
<h3 data-id="heading-10">自由变量</h3>
<blockquote>
<p>不在当前作用域声明却被调用的变量叫自由变量 , 取自由变量的值需要在声明当前函数的作用域去找</p>
</blockquote>
<h3 data-id="heading-11">作用域</h3>
<blockquote>
<p>不同作用域之间的同名变量不会冲突 , 只有函数能创建作用域 , 作用域在函数创建时确定 , 函数内变量的值在代码执行时才确定.不同作用域内可以有多个执行上下文(同一函数,不同参数调用) , 多个执行上下文同一时间只能执行一个，形成执行上下文栈 ,</p>
</blockquote>
<h3 data-id="heading-12">作用域链</h3>
<blockquote>
<p>最大的作用域是全局作用域 , 当前作用域没有就跨到更大的作用域找,一直到全局作用域,这条路线被称为作用域链.</p>
</blockquote>
<p>&#125;
闭包</p>
<blockquote>
<p>一个作用域访问另外一个作用域中的变量,并且不会随着函数执行完毕而回收.</p>
</blockquote>
<h2 data-id="heading-13">浅拷贝和深拷贝</h2>
<h3 data-id="heading-14">浅拷贝</h3>
<blockquote>
<p>只会复制第一层的属性(变量),无法拷贝方法(函数),只能拷贝方法地址值,</p>
</blockquote>
<p>通过hasOwnProperty方法遍历判断属性是否存在实现浅拷贝
Object.assign()方法也可以实现浅拷贝</p>
<h3 data-id="heading-15">深拷贝</h3>
<ul>
<li>通过递归遍历,在碰到有深层对象的时候继续遍历直到没有子对象为止.</li>
<li>通过递归遍历的方式以及先转Json字符串,赋值后再转Json对象的方式实现深拷贝.</li>
<li>通过扩展字符串实现深拷贝</li>
<li>Json方式的缺点:拷贝不了Date数据,正则对象,Error对象,undefined等等</li>
</ul>
<h2 data-id="heading-16">事件循环</h2>
<h3 data-id="heading-17">宏任务</h3>
<blockquote>
<p>tasks，包括定时器，循环器，I/O,以及script;</p>
</blockquote>
<h3 data-id="heading-18">微任务</h3>
<blockquote>
<p>jobs，包括promise的.then，观察者(object.observe) node里面的p                           rocess.nexttick;</p>
</blockquote>
<h3 data-id="heading-19">js只能单线程执行代码</h3>
<ol>
<li>同步代码优先执行，碰到异步请求加入消息队列，分为宏任务队列和微任务队列。</li>
<li>同步代码全部执行完成，开始执行消息队列的请求，优先级：微任务>宏任务，</li>
</ol>
<p>先执行完所有微任务，如果微任务执行过程中又有新的微任务或者宏任务，依旧分别加入消息队列，如果第一遍微任务执行完毕后没有新的微任务加入则开始执行宏任务，否则继续执行微任务，一直循环执行这个操作,叫做事件循环,直到消息队列中不存在微任务和宏任务。
3. 同步代码和微任务执行完成，开始执行宏任务，如果宏任务中包含微任务则下次循环会再优先执行微任务，然后再执行宏任务。</p>
<h2 data-id="heading-20">common.js和ES6模块化</h2>
<h3 data-id="heading-21">一 . common.js是模块化 , 每个模块都是单独的作用域</h3>
<blockquote>
<p>利用require方法读取module.export导出的对象.但因为require是同步的 , script标签天生异步的 , 所以需要处理方案</p>
</blockquote>
<h4 data-id="heading-22">AMD方案:</h4>
<blockquote>
<p>异步模块定义 , 借助require.js解决了多个js文件依赖的关系,以及js加载时浏览器会停止运行两个问题.(异步加载 ,解决浏览器卡顿 , 指定回调函数 , 一号位没加载完不会加载二号位,解决多文件依赖)</p>
</blockquote>
<h4 data-id="heading-23">CMD方案:</h4>
<blockquote>
<p>通用模块定义 , 借助sea.js , 推崇一个模块一个文件.</p>
</blockquote>
<h4 data-id="heading-24">关系和区别</h4>
<blockquote>
<p>都是解决的同样的问题,只是方法略有不同,AMD推崇依赖前置,定义的时候就要声明 ,  CMD推崇就近依赖,用到的时候才加载</p>
</blockquote>
<p>AMD用户体验好，因为没有延迟，依赖模块提前执行了，CMD性能好，因为只有用户需要的时候才执行</p>
<h3 data-id="heading-25">二.  ES6 Modules</h3>
<blockquote>
<p>是js自带的语法,是声明式的代码集合(集合里面保存可以导出的变量以及导出数据的内存地址)</p>
</blockquote>
<h3 data-id="heading-26">三.  关系和区别</h3>
<p>写法区分:</p>
<pre><code class="copyable">//导入
common.js:let a = require()
ES6      :import &#123;a&#125; from ''./index.js

//导出 
common.js: module.export
ES6      : export default 或 export const  mode = &#123;&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>ES6是在代码正式运行之前(编译阶段)执行, 而CommonJS必须在运行时执行</li>
<li>es6一般在浏览器环境 , common.js一般在node环境</li>
</ul>
<h2 data-id="heading-27">原型和原型链</h2>
<ol>
<li>所有的实例对象，都有一个隐式原型__proto__,构成原型链(尝试访问一个属性或方法,如果不存在,访问其构造函数,逐级查找,直到对象原型.)</li>
<li>所有的构造函数都有一个显式原型prototype. 同时显式原型有一个constructor(构造器)指回其构造函数.</li>
<li>实例对象的_proto_指向其构造函数的prototype</li>
<li>Object.prototype = null (原型链最深处,历史遗留问题)</li>
<li>Function的_proto_和prototype都指向Function.prototype(function的原型对象)</li>
</ol>
<h2 data-id="heading-28">面向对象的理解</h2>
<blockquote>
<p>面向对象就是把所有的事物都看作是对象 , 每个对象的出现都只为解决某个单一需求 , 对象拥有三大特点: 不跟其他对象有所关联. 每个对象都相对独立叫封装 , 实例对象可以调用原型对象的方法叫继承 , 对象的方法可以多种调用方式 , 不同的方法实现不同的功能叫多态.</p>
</blockquote>
<h2 data-id="heading-29">typeof,instanceof和toString</h2>
<blockquote>
<p>typeof(类型判断)无法检测复杂类型(array,object,null) , 查出来都是object,</p>
</blockquote>
<pre><code class="copyable">console.log(typeof(a))//number(返回类型)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>instanceof(实例),判断该对象是谁的实例,是否在其原型上(只能判断引用类型)</p>
</blockquote>
<pre><code class="copyable">obj1 instanceof obj2  //true or false(判断是否属于该类型,返回布尔值)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>Object.prototype.toString.call()</p>
</blockquote>
<p>Object对象和它的原型链上各自有一个toString()方法,第一个返回的是一个函数，第二个返回的是值类型,Array，Function，Date继承的是Object.toString() , 是一个函数 , 判断值得用object.prototype的toString,是一个值类型.</p>
<h2 data-id="heading-30">柯里化函数</h2>
<blockquote>
<p>柯里化函数是:是把接受多个参数的函数变换成接受一个单一参数（最初函数的第一个参数）的函数，并且返回接受余下的参数而且返回结果的新函数的技术。(改变函数传参方式)</p>
</blockquote>
<pre><code class="copyable">// 普通的add函数
function add(x, y) &#123;
    return x + y
&#125;

// 柯里化后
function curryingAdd(x) &#123;
    return function (y) &#123;
        return x + y
    &#125;
&#125;

add(1, 2)           // 3
curryingAdd(1)(2)   // 3
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-31">扁平化数据</h2>
<blockquote>
<p>扁平化概念的核心意义是：去除冗余、厚重和繁杂的装饰效果。其实就是多维数组降维成一维数组,嵌套对象解耦成一级对象(只有一级没有子级对象).</p>
</blockquote>
<h3 data-id="heading-32">扁平化方法:</h3>
<pre><code class="copyable">1.flat()
    let arr2 = [1, 2, [3, 4, [5, 6]]];
    arr2.flat(1); // [1, 2, 3, 4, [5, 6]]
2.扩展字符串
    let arr = [[1, 2, [3, 4], 5], [6, 7, 8], [[9, 10], 11]]
        function flat(arr) &#123;
          while (arr.some(item => Array.isArray(item))) &#123;
            arr = [].concat(...arr);
          &#125;
          return arr;
        &#125;
    console.log(flat(arr)); // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
3.reduce()
    let arr = [[1, 2, [3, 4], 5], [6, 7, 8], [[9, 10], 11]];
        function flat(arr) &#123;
          return arr.reduce(function (prev, cur) &#123;
            return prev.concat(Array.isArray(cur) ? flat(cur) : cur);
          &#125;, [])
        &#125;
    console.log(flat(arr)); // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
 //数组扁平化和对象扁平化大同小异
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-33">AST树形结构</h2>
<blockquote>
<p>AST树形结构,就是把js代码按照特定的规则,变成特殊对象,以至于在更改js逻辑的时候,其实就是修改了AST对象的属性值,然后再变成js源码,转换规则可以自定义,也可以使用社区规范</p>
</blockquote>
<h1 data-id="heading-34">End</h1></div>  
</div>
            