
---
title: 'Vue源码之transition-group'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/118eafc0ab834d5fa2dfe88d8830309c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 06 Apr 2021 22:03:42 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/118eafc0ab834d5fa2dfe88d8830309c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><div class="output_wrapper" id="user-content-output_wrapper_id"><h1 id="user-content-htransitiongroup" data-id="heading-0"><span>transition-group组件解析</span></h1>
<blockquote>
  <p>Function</p>
</blockquote>
<figure><img alt title class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/118eafc0ab834d5fa2dfe88d8830309c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><figcaption></figcaption></figure>
<figure><img alt title class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1896ef760ba94d2da1a4b584915487b6~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><figcaption></figcaption></figure>
<figure><img alt title class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9887e7ab53a046c382668387a744072c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><figcaption></figcaption></figure>
<figure><img alt title class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc437792f9954b4b897c92bf61cfc660~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><figcaption></figcaption></figure>
<figure><img alt title class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b852c473547f4dc385f232dc24f73851~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><figcaption></figcaption></figure>
<blockquote>
  <p>工具函数</p>
</blockquote>
<ul>
<li><span>recordPosition</span></li>
</ul>
<figure><img alt title class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3571383a92f5494c8967cd0dd4672d61~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><figcaption></figcaption></figure>
<ul>
<li><span>applyTranslation</span></li>
</ul>
<figure><img alt title class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e374ff5b496d4e3c8ed25c0bc9257f04~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><figcaption></figcaption></figure>
<h1 id="user-content-h" data-id="heading-1"><span>首次渲染</span></h1>
<blockquote>
  <p>流程</p>
</blockquote>
<figure><img alt title class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38a6f15e4c2f45b689845f4d8409b489~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><figcaption></figcaption></figure>
<blockquote>
  <p>总结</p>
</blockquote>
<p>1.执行transition-group的render函数，获取定义的tag，未定义就获取默认值。</p>
<p>2.创建map空对象 ，创建prevChildren数组，创建rawChildren为组件包裹的内容，创建children数组。</p>
<p>3.通过transition-group的属性和事件提取数据赋值给transitionData。</p>
<p>4.遍历rawChildren对节点的key做判断，不存在会报错，存在就把节点push到children中，其次以节点的key为key，节点为value存储到map中。接着设置节点data的transition为transitionData。这点很关键，只有这样才能实现列表中单个元素的过渡动画。</p>
<p>5.最终调用h也就是createElment将children传入渲染tag Vnode。</p>
<p>6.执行updated时，在beforeMount中对_update进行了重写，首先保存之前的_update，首先调用<strong>patch</strong>此时this._vnode和this.kept为undefined啥也不做 ，然后在调用原始的update函数再次进行patch渲染tag Vnode为DOM节点。</p>
<h1 id="user-content-hadd" data-id="heading-2"><span>点击add</span></h1>
<blockquote>
  <p>流程</p>
</blockquote>
<figure><img alt title class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3626808b9c5494f8f300fe1b4498b39~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><figcaption></figcaption></figure>
<blockquote>
  <p>总结</p>
</blockquote>
<p>1.执行transition-group的render函数，获取定义的tag，未定义就获取默认值。</p>
<p>2.创建map空对象 ，创建prevChildren数组为上一次渲染的children（9条），创建rawChildren为组件包裹的内容（10条），创建children数组。</p>
<p>3.通过transition-group的属性和事件提取数据赋值给transitionData。</p>
<p>4.遍历rawChildren对节点的key做判断，不存在会报错，存在就把节点push到children中，其次以节点的key为key，节点为value存储到map中。接着设置节点data的transition为transitionData。这点很关键，只有这样才能实现列表中单个元素的过渡动画。</p>
<p>5.此时存在prevChildren，首先创建kept和removed数组。循环prevChildren，把当前的transitionData赋值到上一次每个节点的data的transition属性中，通过原生dom节点api getBoundingClientRect获取到位置数据保留到上一次每个节点的data的pos属性中。</p>
<p>6.如果上次渲染的节点也在这次渲染的节点中，把节点往kept数组里丢。否则把节点往removed数组里丢。调用h也就是createElment将kept传入渲染tag Vnode。保存到this.kept中，把removed数组保存到this.removed中。</p>
<p>7.最终调用h也就是createElment将children传入渲染tag Vnode。</p>
<p>8.执行updated时，在beforeMount中对_update进行了重写，首先保存之前的_update，接着调用<strong>patch</strong>此时this._vnode为首次渲染的组件vnode（9条），this.kept为tag为p的vnode（9条）两者为相同节点执行patchVnode。然后在调用原始的update函数再次进行patch，此时是旧vnode(9条)与新vnode（10条）的对比，执行patchVnode。this._update执行完成后调用update钩子，执行transition-group的update函数.</p>
<p>9.update函数首先获取prevChildren,然后获取获取move类，通过hasMove函数判断是否存在move类并且css属性是否与缓动相关。</p>
<p>10.接着对prevChildren遍历执行callPendingCbs在前⼀个过渡动画没执⾏完⼜再次执⾏到updated的时候，会提前执⾏ _moveCb 和 _enterCb 确保执行顺序没问题。</p>
<p>11.对prevChildren遍历执行recordPosition记录节点的新位置赋值给节点data的newPos属性。</p>
<p>12.对prevChildren遍历执行applyTranslation先计算节点新位置和旧位置的差值，如果差值不为 0，则说明这些节点是需要移动的，所以记录 vnode.data.moved 为 true，并且通过设置 transform 把需要移动的节点的位置⼜偏移到之前的旧位置，⽬的是为了做move缓动做准备。</p>
<p>13.强制重绘。</p>
<p>14.对prevChildren遍历，对于标志moved的节点，添加move class，移除动画，由于有move class 所以就有了move 的动画，添加transition结束事件 结束后执行cb函数一系列清理操作。</p>
<h1 id="user-content-hremove" data-id="heading-3"><span>点击remove</span></h1>
<blockquote>
  <p>流程</p>
</blockquote>
<figure><img alt title class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6ea19fa9e8a45a1908092960f748f0b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><figcaption></figcaption></figure>
<blockquote>
  <p>总结</p>
</blockquote>
<p>1.执行transition-group的render函数，获取定义的tag，未定义就获取默认值。</p>
<p>2.创建map空对象 ，创建prevChildren数组为上一次渲染的children（10条），创建rawChildren为组件包裹的内容（8条），创建children数组。</p>
<p>3.通过transition-group的属性和事件提取数据赋值给transitionData。</p>
<p>4.遍历rawChildren对接点的key做判断，不存在会报错，存在就把节点push到children中，其次以节点的key为key，节点为value存储到map中。接着设置节点data的transition为transitionData。这点很关键，只有这样 才能实现列表中单个元素的过渡动画。</p>
<p>5.此时存在prevChildren，首先创建kept和removed数组。循环prevChildren，把当前的transitionData赋值到上一次每个节点的data的transition属性中，通过原生dom节点api getBoundingClientRect获取到位置数据保留到上一次每个节点的data的pos属性中。</p>
<p>6.如果上次渲染的节点也在这次渲染的节点中，把节点往kept数组里丢（8条）。否则把节点往removed数组里丢。调用h也就是createElment将kept传入渲染tag Vnode。保存到this.kept中，把removed数组保存到this.removed中（2条）。</p>
<p>7.最终调用h也就是createElment将children传入渲染tag Vnode。</p>
<p>8.执行updated时，在beforeMount中对_update进行了重写，首先保存之前的_update，调用<strong>patch</strong>此时this._vnode为上一次渲染的组件vnode（10条子节点），this.kept为tag为p的vnode（8条子节点）两者为相同节点执行patchVnode对比将当前仍存在的标签节点作为新节点，移除当前不存在的节点。然后将this.kept赋值给this._vnode，最后调用原始的update函数再次进行patch，此时是旧vnode也就是this._vnode(8条)与新vnode（8条）的对比，执行patchVnode。this._update执行完成后调用update钩子，执行transition-group的update函数。（两次patch：第一次是从document移除当前不存在的旧节点，因为数据更新过程是不稳定的，第一次调用patch第四个参数为true，那么节点就不会移动。第二次是如果节点有新增的情况添加新节点到document中，完成更新。）</p>
<p>9.update函数首先获取prevChildren,然后获取获取move类，通过hasMove函数判断是否存在move类并且css属性是否与缓动相关。</p>
<p>10.接着对prevChildren遍历执行callPendingCbs在前⼀个过渡动画没执⾏完⼜再次执⾏到updated的时候，会提前执⾏ _moveCb 和 _enterCb 确保执行顺序没问题。</p>
<p>11.对prevChildren遍历执行recordPosition记录节点的新位置赋值给节点data的newPos属性。</p>
<p>12.对prevChildren遍历执行applyTranslation先计算节点新位置和旧位置的差值，如果差值不为 0，则说明这些节点是需要移动的，所以记录 vnode.data.moved 为 true，并且通过设置 transform 把需要移动的节点的位置⼜偏移到之前的旧位置，⽬的是为了做move缓动做准备。</p>
<p>13.强制重绘。</p>
<p>14.对prevChildren遍历，对于标志moved的节点，添加move class，移除动画，由于有move class 所以就有了move 的动画，添加transition结束事件 结束后执行cb函数一系列清理操作。</p>
<h1 id="user-content-h-1" data-id="heading-4"><span>总结</span></h1>
<figure><img alt title class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11a46d01875b4c3c81733e00ac37f92c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><figcaption></figcaption></figure></div></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            