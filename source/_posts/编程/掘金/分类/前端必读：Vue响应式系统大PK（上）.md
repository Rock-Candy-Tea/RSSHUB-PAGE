
---
title: '前端必读：Vue响应式系统大PK（上）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5972'
author: 掘金
comments: false
date: Tue, 18 May 2021 19:45:15 GMT
thumbnail: 'https://picsum.photos/400/300?random=5972'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>转载请注明出处：葡萄城官网，葡萄城为开发者提供专业的开发工具、解决方案和服务，赋能开发者。</p>
</blockquote>
<p>响应式系统（Reactivity systems）是现代前端框架的关键部分之一。应用系统的的高度交互性、动态性和响应能力全靠它支持。每个Web开发人员而言都应该了解这一系统的功能和实践操作。</p>
<h1 data-id="heading-0">原理</h1>
<p>响应系统是一种使自动使数据源（模型）与数据表示（视图）层自动保持同步的机制。每次模型更改时，都会重新渲染视图。</p>
<p>以一个简单的Markdown编辑器为例。通常编辑器有两个窗格：一个窗格用于编写Markdown代码（用于修改基础模型），另一个窗格用于预览已编译的HTML（显示已更新的视图）。当我们在书写窗格中写东西时，它会立即在预览窗格中自动预览。这个例子比较简单，在实际情况中会复杂很多。</p>
<p>在许多情况下，我们要显示的数据取决于其他数据。在这种情况下，需要跟踪相关数据，并根据跟踪情况来更新数据。例如，我们有一个fullName，该属性由firstName和lastName属性组成。修改其任何依赖项后，fullName将自动重新评估，并在视图中显示结果。</p>
<p>了解什么是响应式系统后，在了解Vue 3中的响应系统如何工作以及如何在实践中使用之前，让我们一起来快速回顾一下Vue 2中的响应系统内容及其注意事项。</p>
<h1 data-id="heading-1">Vue 2的响应式系统简介</h1>
<p>Vue 2中的响应或多或少会被“隐藏”。无论我们放置在data对象中的是什么，Vue都会使其隐式反应（reactive implicitly）。这样虽然可以使开发人员的工作更加轻松，但灵活度却会不可避免的降低。
在幕后，Vue 2使用ES5 Object.defineProperty将data对象的所有属性转换为getter和setter。对于每个组件实例，Vue创建一个依赖关系观察程序实例，观察者会记录组件渲染期间依赖收集/跟踪的任何属性。当属性触发依赖项的设置器时，将通知观察者，并将组件重新渲染并更新视图。但是却也会有一些问题存在。</p>
<h2 data-id="heading-2">变更检测警告</h2>
<p>由于Object.defineProperty方法的限制，Vue无法检测到某些数据更改。包括：</p>
<ul>
<li>给对象添加属性或把对象移除属性（例如obj.newKey = value）</li>
<li>按索引设置数组项（例如arr[index] = newValue）</li>
<li>修改数组的长度（例如arr.length = newLength）</li>
</ul>
<p>不过为了解决这些问题， Vue为提供了Vue.set API方法，该方法向响应对象添加了一个属性，确保新属性也是响应性的，从而触发了视图更新。</p>
<p>用下述实例讨论该情况：</p>
<pre><code class="hljs language-<div copyable" lang="<div">  <h1>Hello! My name is &#123;&#123; person.name &#125;&#125;. I'm &#123;&#123; person.age &#125;&#125; years old.</h1>
  <button @click="addAgeProperty">Add "age" property</button>
  <p>Here are my favorite activities:</p>
  <ul>
    <li v-for="item, index in activities" :key="index">
      &#123;&#123; item &#125;&#125;
      <button @click="editActivity(index)">Edit</button>
    </li>
  </ul>
  <button @click="clearActivities">Clear the activities list</button>
</div>

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-const copyable" lang="const">  el: '#app',
  data: &#123;
    person: &#123;
      name: "David"
    &#125;,
    activities: [
      "Reading books",
      "Listening music",
      "Watching TV"
    ]
  &#125;,
  methods: &#123; 
    // 1. Add a new property to an object
    addAgeProperty() &#123;
      this.person.age = 30
    &#125;,
    // 2. Setting an array item by index
    editActivity(index) &#123;
      const newValue = prompt('Input a new value')
      if (newValue) &#123;
        this.activities[index] = newValue
      &#125;
    &#125;,
    // 3. Modifying the length of the array
    clearActivities() &#123; 
      this.activities.length = 0 
    &#125;
  &#125;
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的示例中，我们会发现这三种方法都不起作用。我们不能向该person对象添加新属性，无法使用activities的索引来编辑数组中的项目，也不能修改activities数组的长度。</p>
<p>优化如下：</p>
<pre><code class="hljs language-const copyable" lang="const">  el: '#app',
  data: &#123;
    person: &#123;
      name: "David"
    &#125;,
    activities: [
      "Reading books",
      "Listening music",
      "Watching TV"
    ]
  &#125;,
  methods: &#123; 
    // 1. Adding a new property to the object
    addAgeProperty() &#123;
      Vue.set(this.person, 'age', 30)
    &#125;,
    // 2. Setting an array item by index
    editActivity(index) &#123;
      const newValue = prompt('Input a new value')
      if (newValue) &#123;
        Vue.set(this.activities, index, newValue)
      &#125;
    &#125;,
    // 3. Modifying the length of the array
    clearActivities() &#123; 
      this.activities.splice(0)
    &#125;
  &#125;
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在此示例中，我们用Vue.setAPI方法将新age属性添加到person对象，并从活动数组中选择/修改特定项目。在最后一种情况下，使用JavaScript内置splice方法。</p>
<p>这个做法完全可行但却略显笨拙，而且会导致前后代码不一致。而Vue 3就解决了这个问题。
我们用下面示例继续看：</p>
<pre><code class="hljs language-const copyable" lang="const">  data() &#123;
    return &#123;
      person: &#123;
        name: "David"
      &#125;,
      activities: [
        "Reading books",
        "Listening music",
        "Watching TV"
      ]
    &#125;
  &#125;,
  methods: &#123; 
    // 1. Adding a new property to the object
    addAgeProperty() &#123;
      this.person.age = 30
    &#125;,
    // 2. Setting an array item by index
    editActivity(index) &#123;
      const newValue = prompt('Input a new value')
      if (newValue) &#123;
        this.activities[index] = newValue
      &#125;
    &#125;,
    // 3. Modifying the length of the array
    clearActivities() &#123; 
      this.activities.length = 0 
    &#125;
  &#125;
&#125;

Vue.createApp(App).mount('#app')

<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到在Vue 3中，所有方法都可以正常工作。</p>
<p>在Vue 2.6中，引入的Vue.observable API方法，一定程度的公开了响应式系统，使开发人员可以体验到响应式系统的内容。实际上，这和Vue内部用来包装data对象是完全相同的方法，对于在简单场景创建小的跨组件状态存储很有用。但依旧没办法和Vue3的响应式系统相比，接下来就为大家详细介绍。</p>
<p>注意：由于Object.defineProperty方法是仅限ES5且不可调整的功能，因此Vue 2不支持IE8及以下版本。</p>
<h1 data-id="heading-3">Vue 3响应式系统如何工作</h1>
<p>为了充分利用ES6 Proxy and Reflect API ，Vue 3中的响应式系统已被完全重写。新版本新增响应式API，该API使系统比以前更加灵活和强大。</p>
<p>Proxy API允许开发人员拦截和修改目标对象上的更低级对象操作。代理（proxy）是对象的克隆/包装（clone/wrapper），并提供特殊功能（称为target），这些功能响应特定的操作并覆盖JavaScript对象的内置行为（称为traps）。如果仍然需要使用默认行为，则可以使用相应的Reflection API，其名称顾名思义就是反映Proxy API的方法。这里有一个示例，用来了解如何在Vue 3中使用这些API：</p>
<pre><code class="hljs language-let copyable" lang="let">  name: "David",
  age: 27
&#125;;

const handler = &#123;
  get(target, property, receiver) &#123;
    // track(target, property)
    console.log(property) // output: name
    return Reflect.get(target, property, receiver)
  &#125;,
  set(target, property, value, receiver) &#123;
    // trigger(target, property)
    console.log(`$&#123;property&#125;: $&#123;value&#125;`) // output: "age: 30" and "hobby: Programming"
    return Reflect.set(target, property, value, receiver)
  &#125;
&#125;

let proxy = new Proxy(person, handler);   

console.log(person)

// get (reading a property value)
console.log(proxy.name)  // output: David

// set (writing to a property)
proxy.age = 30;

// set (creating a new property)
proxy.hobby = "Programming";

console.log(person) 

<span class="copy-code-btn">复制代码</span></code></pre>
<p>要创建一个新的代理，使用new Proxy(target, handler)构造函数。它带有两个参数：目标对象（person对象）和处理程序对象，该对象定义将拦截哪些操作（get和set操作）。在handler对象中， get和set陷阱来跟踪何时读取属性以及何时修改/添加属性。设置控制台语句以确保运行正确。</p>
<p>在get和set陷阱采用下列参数：</p>
<ul>
<li>target：代理包装的目标对象</li>
<li>property：属性名称</li>
<li>value：属性值（此参数仅用于设置操作）</li>
<li>receiver：进行操作的对象（通常是代理）</li>
<li></li>
</ul>
<p>Reflect API方法与其相应的代理方法接受相同的参数</p>
<p>注释中track函数和trigger函数特定用于Vue，用于跟踪何时读取属性以及何时修改/添加属性。</p>
<p>在示例的最后一部分，用控制台语句输出原始person对象。然后用另一份声明中读取属性name的proxy对象。接下来，修改age属性并创建一个新hobby属性。最后，再次输出该对象以查看它是否正确更新。</p>
<p>以上就是Vue3响应式系统的完整工作流程，但在实际工作中会复杂得多。</p>
<p>使用Vue 3响应式系统，还有一些注意事项：</p>
<ul>
<li>仅适用于支持ES6 +的浏览器</li>
<li>响应代理不等于原始对象</li>
</ul>
<h1 data-id="heading-4">总结</h1>
<p>以上我们将Vue2和Vue3中响应式系统部分进行了比较，并对响应式系统的工作原理进行了说明，在后面的文章中，我们会进一步为大家介绍Vue3中响应式系统的API，敬请期待。</p></div>  
</div>
            