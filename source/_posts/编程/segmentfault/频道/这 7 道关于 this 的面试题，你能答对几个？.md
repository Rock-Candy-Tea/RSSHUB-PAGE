
---
title: '这 7 道关于 this 的面试题，你能答对几个？'
categories: 
    - 编程
    - segmentfault
    - 频道

author: segmentfault
comments: false
date: 2021-03-22 17:48:17
thumbnail: 'https://segmentfault.com/img/bVbJA9m'
---

<div>   
<p>在 JavaScript 中，<code>this</code> 是函数调用上下文。正是由于 <code>this</code> 的行为很复杂，所以在 JavaScript 面试中，总是会问到有关  <code>this</code> 的问题。</p><p>做好的准备面试的方法是练习，所以本文针对 <code>this</code> 关键字整理了 7 个有趣的面试。</p><p>注意：下面的 JavaScript 代码段以非严格模式运行。</p><h2>1：变量与属性</h2><p>以下代码输出什么：</p><pre><code class="javascript">const object = &#123;
  message: 'Hello, World!',

  getMessage() &#123;
    const message = 'Hello, Earth!';
    return this.message;
  &#125;
&#125;;

console.log(object.getMessage()); // => ?</code></pre><h4>答案：</h4><p>输出： <code>'Hello, World!'</code> </p><p><code>object.getMessage()</code> 是方法调用，这就是为什么方法中的 <code>this</code> 等于 <code>object</code> 的原因。</p><p>方法中还有一个变量声明 <code>const message ='Hello，Earth!'</code>，该变量不会影响 <code>this.message</code> 的值。</p><h2>2：猫的名字</h2><p>以下代码输出什么：</p><pre><code class="javascript">function Pet(name) &#123;
  this.name = name;

  this.getName = () => this.name;
&#125;

const cat = new Pet('Fluffy');

console.log(cat.getName()); // => ?

const &#123; getName &#125; = cat;
console.log(getName());     // =>?</code></pre><h4>答案：</h4><p>输出：<code>'Fluffy'</code> 和  <code>'Fluffy'</code> </p><p>当一个函数被当作构造函数调用时（ <code>new Pet('Fluffy')</code> ），构造函数内部的 <em>this</em> 等于构造的对象。</p><p><code>Pet</code> 构造函数中的 <code>this.name = name</code>  表达式在构造的对象上创建 <code>name</code> 属性。</p><p><code>this.getName = () => this.name</code> this.getName =（）=> this.name  在构造的对象上创建方法 <code>getName</code>。因为使用了箭头函数，所以箭头函数中的 <em>this</em> 等于外部作用域中的 <code>this</code> ，也就是构造函数 <code>Pet</code>。</p><p>调用 <code>cat.getName()</code> 和 <code>getName()</code> 会返回表达式 <code>this.name</code>，其结果为 <code>'Fluffy'</code>。</p><h2>3：延迟输出</h2><p>以下代码输出什么：</p><pre><code class="javascript">const object = &#123;
  message: 'Hello, World!',

  logMessage() &#123;
    console.log(this.message); // => ?
  &#125;
&#125;;

setTimeout(object.logMessage, 1000);</code></pre><h4>答案：</h4><p>延迟1秒钟后，输出：<code>undefined</code> </p><p>尽管  <code>setTimeout()</code> 函数使用 <code>object.logMessage</code> 作为回调，但仍把 <code>object.logMessage</code> 作为常规函数而非方法调用。并且在常规函数调用中 <em>this</em> 等于全局对象，在浏览器环境中是 <code>window</code>。这就是 <code>logMessage</code> 方法内的 <code>console.log(this.message)</code> 输出 <code>window.message</code> 的原因，后者是 <code>undefined</code>。</p><p><strong>挑战：怎样修改这段代码使其输出 <code>'Hello, World!'</code>？在下面的评论中写出你的解决方案</strong>*</p><h2>4：补全代码</h2><p>补全代码，使结果输出 <code>"Hello，World!"</code> 。</p><pre><code class="javascript">const object = &#123;
  message: 'Hello, World!'
&#125;;

function logMessage() &#123;
  console.log(this.message); // => "Hello, World!"
&#125;

// Write your code here...</code></pre><h4>答案：</h4><p>至少有 3 种方式可以把 <code>logMessage()</code> 作为对象上的方法调用。任何一个都被看作是正确答案：</p><pre><code class="javascript">const object = &#123;
  message: 'Hello, World!'
&#125;;

function logMessage() &#123;
  console.log(this.message); // => 'Hello, World!'
&#125;

// 使用 func.call() 方法
logMessage.call(object);

// 使用 func.apply() 方法
logMessage.apply(object);

// 使用函数绑定
const boundLogMessage = logMessage.bind(object);
boundLogMessage();</code></pre><h2>5：问候与告别</h2><p>以下代码输出什么：</p><pre><code class="javascript">const object = &#123;
  who: 'World',

  greet() &#123;
    return `Hello, $&#123;this.who&#125;!`;
  &#125;,

  farewell: () => &#123;
    return `Goodbye, $&#123;this.who&#125;!`;
  &#125;
&#125;;

console.log(object.greet());    // => ?
console.log(object.farewell()); // => ?</code></pre><h4>答案：</h4><p>输出： <code>'Hello, World!'</code> 和 <code>'Goodbye, undefined!'</code> </p><p>当调用 <code>object.greet()</code> 时，在方法 <code>greet()</code> 内部 <code>this</code> 的值等于 <code>object</code>，因为 <code>greet</code> 是常规函数。所以 <code>object.greet()</code> 返回 <code>'Hello，World！'</code>。</p><p>但是 <code>farewell()</code> 是一个箭头函数，所以箭头函数中 <em>this</em> 的值<strong>总是</strong>等于外部作用域的 <code>this</code>。<code>farewell()</code> 的外部作用域是全局作用域，其中 <code>this</code> 是全局对象。所以 <code>object.farewell()</code> 实际上会返回 <code>'Goodbye, $&#123;window.who&#125;!'</code> ，其结果为 <code>'Goodbye, undefined!'</code>。</p><h2>6：棘手的 length</h2><p>以下代码输出什么：</p><pre><code class="javascript">var length = 4;
function callback() &#123;
  console.log(this.length); // => ?
&#125;

const object = &#123;
  length: 5,
  method(callback) &#123;
    callback();
  &#125;
&#125;;

object.method(callback, 1, 2);</code></pre><h4>答案：</h4><p>输出：<code>4</code> </p><p>使用 <code>method()</code> 内部的常规函数调用来调用 <code>callback()</code> 。因为在常规函数调用期间的 <em>this</em> 值等于全局对象，所以在 <code>callback()</code>  函数中 <code>this.length</code> 为 <code>window.length</code>。</p><p>位于最外层的第一个语句 <code>var length = 4</code> 在全局对象上创建了属性 <code>length</code>，所以 <code>window.length</code> 变为 <code>4</code>。</p><p>最后，在 <code>callback()</code>  函数内部，<code>`this.length</code> 的值为 <code>window.length</code> ，最后输出 <code>4</code>。</p><h2>7：调用参数</h2><p>以下代码输出什么：</p><pre><code class="javascript">var length = 4;
function callback() &#123;
  console.log(this.length); // 输出什么
&#125;

const object = &#123;
  length: 5,
  method() &#123;
    arguments[0]();
  &#125;
&#125;;

object.method(callback, 1, 2);</code></pre><h4>答案：</h4><p>输出：<code>3</code></p><p><code>obj.method(callback, 1, 2)</code> 用了 3 个参数进行调用：<code>callback</code>、<code>1</code> 和 <code>2</code>。结果 <code>method()</code> 内的<code>arguments</code> 特殊变量是有以下结构的类似数组的对象：</p><pre><code class="javascript">&#123;
  0: callback,
  1: 1, 
  2: 2, 
  length: 3 
&#125;</code></pre><p>因为 <code>arguments[0]()</code>  是对 <code>arguments</code> 对象上 <code>callback</code> 的方法调用，所以 <code>callback</code> 内部的 <code>this</code> 等于 <code>arguments</code>。结果在 <code>callback()</code> 内部的 <code>this.length</code> 与 <code>arguments.length</code> 是相同的，都是<code>3</code>。</p><h2>总结</h2><p>如果你答对了 5 个以上，那么你对 <code>this</code> 关键字掌握的情况是很不错的。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVbJA9m" alt="173382ede7319973.gif" title="173382ede7319973.gif" referrerpolicy="no-referrer"></span></p><hr><h4>本文首发微信公众号：前端先锋</h4><h4>欢迎扫描二维码关注公众号，每天都给你推送新鲜的前端技术文章</h4><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVRyYe" alt="欢迎扫描二维码关注公众号，每天都给你推送新鲜的前端技术文章" title="欢迎扫描二维码关注公众号，每天都给你推送新鲜的前端技术文章" referrerpolicy="no-referrer"></span></p><hr><h3>欢迎继续阅读本专栏其它高赞文章：</h3><ul><li><a href="https://segmentfault.com/a/1190000019115050">深入理解Shadow DOM v1</a></li><li><a href="https://segmentfault.com/a/1190000019135847">一步步教你用 WebVR 实现虚拟现实游戏</a></li><li><a href="https://segmentfault.com/a/1190000019154021">13个帮你提高开发效率的现代CSS框架</a></li><li><a href="https://segmentfault.com/a/1190000019085935">快速上手BootstrapVue</a></li><li><a href="https://segmentfault.com/a/1190000019205065">JavaScript引擎是如何工作的？从调用栈到Promise你需要知道的一切</a></li><li><a href="https://segmentfault.com/a/1190000019216390">WebSocket实战：在 Node 和 React 之间进行实时通信</a></li><li><a href="https://segmentfault.com/a/1190000019315509">关于 Git 的 20 个面试题</a></li><li><a href="https://segmentfault.com/a/1190000019302858">深入解析 Node.js 的 console.log</a></li><li><a href="https://segmentfault.com/a/1190000019283751">Node.js 究竟是什么？</a></li><li><a href="https://segmentfault.com/a/1190000019268920">30分钟用Node.js构建一个API服务器</a></li><li><a href="https://segmentfault.com/a/1190000018903274">Javascript的对象拷贝</a></li><li><a href="https://segmentfault.com/a/1190000018224157">程序员30岁前月薪达不到30K，该何去何从</a></li><li><a href="https://segmentfault.com/a/1190000018646425">14个最好的 JavaScript 数据可视化库</a></li><li><a href="https://segmentfault.com/a/1190000018439250">8 个给前端的顶级 VS Code 扩展插件</a></li><li><a href="https://segmentfault.com/a/1190000018660861">Node.js 多线程完全指南</a></li><li><a href="https://segmentfault.com/a/1190000018701596">把HTML转成PDF的4个方案及实现</a></li></ul><hr><ul><li><a href="http://blog.yidengxuetang.com/" rel="nofollow">更多文章...</a></li></ul>  
</div>
            