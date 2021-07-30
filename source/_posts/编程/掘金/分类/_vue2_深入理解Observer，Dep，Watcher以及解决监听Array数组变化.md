
---
title: '_vue2_深入理解Observer，Dep，Watcher以及解决监听Array数组变化'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7c03c101fc940ba92f409c9ec78eaa8~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 29 Jul 2021 23:53:14 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7c03c101fc940ba92f409c9ec78eaa8~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";@keyframes spin&#123;0%&#123;transform:rotate(0)&#125;to&#123;transform:rotate(1turn)&#125;&#125;.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#36ace1;background-image:linear-gradient(90deg,rgba(217,234,251,.25) 3%,transparent 0),linear-gradient(1turn,rgba(217,234,251,.25) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;color:#36ace1&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"";display:block;position:absolute;left:0;top:0;bottom:0;margin:auto;background-image:url(data:image/png;base64,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);animation:spin 2s linear 1s infinite&#125;.markdown-body h1&#123;position:relative;font-size:30px;padding:12px 38px;margin:30px 0&#125;.markdown-body h1:before&#123;width:30px;height:30px;background-size:30px 30px&#125;.markdown-body h2&#123;position:relative;font-size:24px;padding:12px 36px;margin:28px 0&#125;.markdown-body h2:before&#123;width:28px;height:28px;background-size:28px 28px&#125;.markdown-body h3&#123;position:relative;font-size:18px;padding:4px 32px;margin:26px 0&#125;.markdown-body h3:before&#123;width:24px;height:24px;background-size:24px 24px&#125;.markdown-body h4&#123;position:relative;padding:4px 28px;font-size:16px;margin:22px 0&#125;.markdown-body h4:before&#123;width:20px;height:20px;background-size:20px 20px&#125;.markdown-body h5&#123;position:relative;padding:4px 26px;font-size:15px;margin:20px 0&#125;.markdown-body h5:before&#123;width:18px;height:18px;background-size:18px 18px&#125;.markdown-body h6&#123;position:relative;padding:4px 22px;font-size:14px;margin:16px 0&#125;.markdown-body h6:before&#123;width:16px;height:16px;background-size:16px 16px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;border:none;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#36ace1,#dff0fe,#36ace1);overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:50px;height:24px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAEgElEQVRIS72Va0xbZRjH/z2FcimbchEQFDYRCIRAAWFQ2MaCXBwmUxYDLGGEcRFkH9wmk04zG0Bo2dwNIisERANqhjqdEmhd4nRbuwpsXDYWLLoRgeG4Chu9QHvMOQ0dpTAKH3y/tDnv8/5/z/Oc//scBv6nxdgoJ14gVYPEuITHdTdHY12gRIH0T0KljlqwthqUFHGtzAEsxqwLtPvkdc+FeeI3BgMeAMEhdOqR1mM7xswBrgmKE8pfIUhtm7fbZsft/i7wc98MtrUFxmbU6ByYgFwxjtFp5Q+WpF1mCy9wajXoqqD4E91saOf603e+5B7t99xTkyZJEiKJAl2DE9Xio1HvrBS8IuhVwVUP503swdJ9QWAw1izaoDs6pQT/655BMS9yy3KYiUoM/7adu7NmtnQfx5zWm8Q8Ui3gyGcddyU8rv/STRNQouDGP5/mhTubX4dpPv3DMzh1qS9LwuPWr+i63WVyn5QYj/4d/i4bqmbpoQ+auvBlQYghX6PE4wTSOzV5EUYlb5Q4MDqLk9/3cMRF27spDSNQamUnWZ4ebNB+OKNCyYVeFCZ5wZ5tiePN/UiP2YoQL0cUX+iFt4sNUiLdcaVvHJLecQiWnKVE8s5LvxAXRWeYgHLre0hecgAN0sxr0XBZgbJUP6OiLnaM4ivZCBrzOWBZEIY9rY5E8pl2nM0KMzzLq5aPiXmRzgbQm2VyR8KGGK/ICAFB6IusbvsDwhRf+n/jtSHc/nsGgjR9V6/1TyLa1wGU+FtnO1CbHQTHTSzIFJOYJ1jwcGLTccMTcyhp7oW4KFJ/SV4/IScrc55kQj07WNuOn94Lpw8kCm/Qv3W5HLjbWxsyfuNUO1TzWjAJBloKt2FBS+Jz6ShiA12NupBdLWugQcmn28lPMkONNql3U5cTSD9Lq+qEUqPFt++G0aKL687wDAqb+pAU7IKCuK2493AOPQ9UCNpib6T1tkg+RZ9KKJcNn8sJc1vac8o16jklLWLuOiDqwvHUIKPw7vtTON+iCDKkl/Cx9FeSYET5um1mHt6jN0Dz9ftwYjORudNjTdaBmi7kxvvA1d6Gjs0X/Q5Sp3tMEMSHre9HnDEZAPFCWUNVdliGJVPvqEP1Hbh4yPj9LadSY6fu6gPsCX+B3mq7NYLv2od8fj4aoViMNQGFijos/XVMTXGavgUisQIle71hwVx9KFEutLVjw8GORTuxoEbeJS7iPrmQyy/sIj2hQpqYHO7ZGs95nnZS4y8K8Pfqrb58UZ+IlKqbqNgfQm8da+pC9xjLqo8foFkau2qaCeXSyvzXfA9SDrp1bxJ/DU/jSJKXEWdBR2J/9U0UpwXTFZ/+8S76h/71FvO4A8sTeuqQThDKalOiPLN3BbhiYlaNsm964elkCztrC4xMqeDqYIus2JdB3cbS5l4MTag44qJt9GxbF4gKThRKY59lW13+KCUQ1pZMEwHKviKx4pFSqXzxCn/X9Gr2NO+zw+cTiTbxmUyCqH3GlsWg2kRNhOnHmhlrFkIvHTZt1borWvMCmRnwH4usn58STiycAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body del&#123;color:#36ace1&#125;.markdown-body code&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#282c34;color:#4ec9b0;padding:.24em .46em;margin:0 4px&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;font-size:12px;border-radius:10px;padding:15px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#4ec9b0;background:#282c34&#125;.markdown-body a&#123;text-decoration:none;color:#409eff;border-bottom:1px solid #409eff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#007bff;border-bottom:1px solid #007bff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;position:relative;padding:8px 26px;background-color:rgba(54,172,225,.75);margin:16px 0;border-left:4px solid #409eff;border-radius:5px&#125;.markdown-body blockquote:before&#123;content:"❝";top:10px;left:8px;color:#409eff;font-size:20px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:20px;position:absolute;right:8px;bottom:0;color:#409eff;opacity:.7&#125;.markdown-body blockquote>p&#123;color:#fff&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">双向绑定</h2>
<ol>
<li>
<p>首先通过一次渲染操作触发Data的getter进行依赖收集</p>
</li>
<li>
<p>在data发生变化的时候会触发它的setter</p>
</li>
<li>
<p>setter通知Watcher</p>
</li>
<li>
<p>Watcher进行回调通知组件重新渲染的函数</p>
</li>
<li>
<p>diff算法来决定是否发生视图的更新</p>
</li>
</ol>
<h2 data-id="heading-1">Observe</h2>
<ol>
<li>
<p>每个数据都有一个标记，防止重复绑定</p>
</li>
<li>
<p>Observer为数据加上响应式属性进行双向绑定，如果是对象，则进行深度遍历，为每一个子对象都绑定上方法，如果是数组，对每个成员进行遍历绑定方法</p>
</li>
</ol>
<p><strong>Observer源码逐步解析:</strong></p>
<pre><code class="copyable">export class Observer &#123;
  value: any;
  dep: Dep;
  vmCount: number;

constructor (value: any) &#123;
    this.value = value
    this.dep = new Dep() // 建立发布者
    this.vmCount = 0
    def(value, '**ob**', this)
    
    if (Array.isArray(value)) &#123;
        // 是数组对每个成员进行遍历绑定方法
        if (hasProto) &#123;
            // **proto**指向重写过后的原型
            protoAugment(value, arrayMethods)
        &#125; else &#123;
            //遍历 arrayMethods 把它身上的这些方法直接给 value
            copyAugment(value, arrayMethods, arrayKeys)
        &#125;
        this.observeArray(value)
        
    &#125; else &#123;
        // 是对象，则进行深度遍历，为每一个子对象都绑定上方法
        // defineReactive 通过 Object.defineProperty 定义 getter 和 setter 收集依赖通知更新
        const keys = Object.keys(obj)
        for (let i = 0; i < keys.length; i++) &#123;
            defineReactive(obj, keys[i])
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">Watcher</h2>
<p><strong>观察者对象</strong></p>
<ol>
<li>
<p>依赖收集后保存在deps里</p>
</li>
<li>
<p>变动的时候deps作为发布者通知watcher watcher进行回调渲染</p>
</li>
</ol>
<h2 data-id="heading-3">Dep</h2>
<ol>
<li>
<p>发布者，可以订阅多个观察者</p>
</li>
<li>
<p>收集依赖后会有一个或者多个watcher</p>
</li>
<li>
<p>一旦有变动便通知所有watcher</p>
</li>
</ol>
<h2 data-id="heading-4">Watch监听Array数组变化</h2>
<p><strong>监听对象：</strong></p>
<pre><code class="copyable">
data()&#123;
    return &#123;
        objVal: &#123;
            name: 'obj',
            type: 'obj'
        &#125;
   &#125;
&#125;,
watch:&#123;
    objVal:&#123;
        handler(val,oldval)&#123;

        &#125;,
        deep: true,
        immediate:true
      &#125;
    &#125;,
    methods:&#123;
      changeObj()&#123;
        this.objVal.name = 'newobj';
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>deep：</strong> 当需要监听一个对象的改变时，普通的watch方法无法监听到对象内部属性的改变，只有data中的数据才能够监听到变化，深入监听，即监听对象里面的值的变化</p>
</blockquote>
<blockquote>
<p><strong>immediate：</strong> watch默认当值第一次绑定的时候，不会执行监听函数，immediate的作用就是首次获取值也执行函数</p>
</blockquote>
<p>以上demo是监听对象，如果换成数组的话，会出现vue不会响应数据变化而重新去渲染页面，则监听失败</p>
<p><strong>解决方法：</strong></p>
<pre><code class="copyable">// Vue.set
Vue.$set(vm.items, indexOfItem, newValue)

// Array.prototype.splice
vm.items.splice(indexOfItem, 1, newValue)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>原理： Object.defineProperty对数组进行响应式化是有缺陷的 Vue使用了重写原型的方案代替</p>
</blockquote>
<ol>
<li>先获取原生 Array 的原型方法，因为拦截后还是需要原生的方法帮我们实现数组的变化。</li>
<li>对 Array 的原型方法使用 Object.defineProperty 做一些拦截操作。</li>
<li>把需要被拦截的 Array 类型的数据原型指向改造后原型</li>
</ol>
<pre><code class="copyable">const arrayProto = Array.prototype // 获取Array的原型
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">function def (obj, key) &#123;
  Object.defineProperty(obj, key, &#123;
    enumerable: true,
    configurable: true,
    value: function(...args) &#123;
      console.log(key); // 控制台输出 push
      console.log(args); // 控制台输出 [Array(2), 7, "hello!"]
       
      // 获取原生的方法
      let original = arrayProto[key];
      
      // 将开发者的参数传给原生的方法，保证数组按照开发者的想法被改变
      const result = original.apply(this, args);
 
      // do something 比如通知Vue视图进行更新
      console.log('我的数据被改变了，视图该更新啦');
      this.text = 'hello Vue';
      return result;
    &#125;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// 新的原型
let obj = &#123;
  push() &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// 重写赋值
def(obj, 'push');
 
let arr = [0];
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// 原型的指向重写
arr.__proto__ = obj;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// 执行push
arr.push([1, 2], 7, 'hello!');
console.log(arr);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7c03c101fc940ba92f409c9ec78eaa8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>源码解析 array.js</strong></p>
<blockquote>
<p>Vue在array.js中重写了methodsToPatch中七个方法，并将重写后的原型暴露出去。</p>
</blockquote>
<pre><code class="copyable">// Object.defineProperty的封装
import &#123; def &#125; from '../util/index'
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// 获得原型上的方法
const arrayProto = Array.prototype
export const arrayMethods = Object.create(arrayProto)

// Vue拦截的方法
const methodsToPatch = [
 'push',
 'pop',
 'shift',
 'unshift',
 'splice',
 'sort',
 'reverse'
];
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// 1.拦截方法
// 2.将开发者的参数传给原生的方法
// 3.重写
// 4.视图更新
methodsToPatch.forEach(function (method) &#123;
  // 原型方法进行赋值，不会去重新改写Array.prototype
  const original = arrayProto[method]
  //ob为成员唯一标识
  def(arrayMethods, method, function mutator (...args) &#123;
    const result = original.apply(this, args)
    const ob = this.__ob__
    let inserted
    //判断方法
    switch (method) &#123;
      case 'push':
      case 'unshift':
        inserted = args
        break
      case 'splice':
        inserted = args.slice(2)
        break
    &#125;
    //判断后observeArray为每个成员绑定方法
    if (inserted) ob.observeArray(inserted)
    // 通知视图更新
    ob.dep.notify()
    return result
  &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">问答</h2>
<p><strong>问：遇到过改变对象或者数组的时候视图没有更新的情况吗？为什么？怎么解决？</strong></p>
<p>场景：</p>
<p>1.利用索引直接设置一个项时:vm.items[indexOfItem] = newValue</p>
<p>2.修改数组的长度时： vm.items.length = newLength</p>
<p>3.Vue 不能检测到对象属性的添加或删除</p>
<p>原因：</p>
<ol>
<li>
<p>因为没有用被重写的方法去修改数组，导致没有响应式的监听到</p>
</li>
<li>
<p>而vue官方文档有明确说明，Vue 会在初始化实例时对属性执行 getter/setter 转化过程，所以属性必须在 data 对象上存在才能让 Vue 转换它，这样才能让它是响应的</p>
</li>
</ol>
<p>解决方法：</p>
<pre><code class="copyable">// 1. 利用this.$set(this.object,key,value)
this.$set(this.obj,"sex","man")
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// 2. 利用this.$delete(target, propertyName/index )
this.$delete(this.testData,"name")
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// 3. 利用Object.assign(&#123;&#125;,this.obj)
this.obj = Object.assign(&#123;&#125;,this.obj,&#123;"myName","jojo"&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>set()通过defineReactive(ob.value, key, val)触发响应式</p>
</blockquote></div>  
</div>
            