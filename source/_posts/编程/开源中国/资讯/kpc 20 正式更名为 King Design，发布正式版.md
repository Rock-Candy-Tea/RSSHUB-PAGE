
---
title: 'kpc 2.0 正式更名为 King Design，发布正式版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7383'
author: 开源中国
comments: false
date: Thu, 28 Apr 2022 17:08:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7383'
---

<div>   
<div class="content">
                                                                    
                                                        <p>经过1年多的时间，KPC组件库完成了TypeScript的重构工作，重构的过程中，我们也进一步打磨组件，引入更流畅的动效，也支持了最新的框架React17 / React18(WIP) / Vue2 / Vue3。另外，除了组件库外，我们还提供了从”产品“到”设计“再到”开发“和最后”验收“各个阶段的一条完成的工具链，现在我们正式更名为King Design对外发布，欢迎大家尝试由金山云打造的这一套完整的设计开发解决方案。</p> 
<p>官网：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdesign.ksyun.com%2F" target="_blank">https://design.ksyun.com/</a></p> 
<h1>组件库新特性</h1> 
<h4>支持TypeScript</h4> 
<div class="ckeditor-html5-video" data-responsive="true"> 
 <video autoplay="autoplay" controls="controls" loop="loop" src="https://damife.ks3-cn-beijing.ksyuncs.com/kpc/TypeScript.mp4" style="height:auto; max-width:100%" width="800">
   
 </video> 
</div> 
<h4>支持React / Vue3 / Vue2</h4> 
<pre><code class="language-bash"># React
npm install @king-design/react -S
yarn add @king-design/react

# Vue 3
npm install @king-design/vue -S
yarn add @king-design/vue

# Vue 2
npm install @king-design/vue-legacy -S
yarn add @king-design/vue-legacy</code></pre> 
<h4>新的动画效果</h4> 
<p>一切变化都有过渡效果</p> 
<div> 
 <div class="ckeditor-html5-video"> 
  <video autoplay="autoplay" controls="controls" loop="loop" src="https://damife.ks3-cn-beijing.ksyuncs.com/kpc/table.mov">
    
  </video> 
 </div> 
 <p> </p> 
</div> 
<h4>支持动态主题切换</h4> 
<p>采用CSS-in-JS实现样式，可以动态细粒度地切换每一个组件的样式，实现动态主题</p> 
<div class="ckeditor-html5-video" data-responsive="true"> 
 <video autoplay="autoplay" controls="controls" loop="loop" src="https://damife.ks3-cn-beijing.ksyuncs.com/kpc/theme.m4v" style="height:auto; max-width:100%" width="800">
   
 </video> 
</div> 
<h1>Changelog</h1> 
<ol> 
 <li>底层到组件库全面采用<code>TypeScript</code>重写，来支持类型检测</li> 
 <li>组件库使用<code>Hooks</code>的思想来拆分逻辑，提高维护性</li> 
 <li>使用<code>@emotion/css</code>的css-in-js方案取代之前的<code>stylus</code>方案，支持运行时切换主题</li> 
 <li>重新设计组件事件<code>Event</code>和扩展点<code>Slot</code>的属性名，使其满足TS的类型检测 
  <ol> 
   <li>React 
    <ol> 
     <li>默认事件名由之前的<code>on$change-value</code>形式，变为<code>onChangeValue</code>形式</li> 
     <li>扩展点名由之前的<code>b-value</code>形式，变为<code>slotValue</code>形式</li> 
    </ol> </li> 
   <li>Vue 
    <ol> 
     <li>默认事件名由之前的<code>@$change:value</code>形式，变为<code>@changeValue</code>形式</li> 
    </ol> </li> 
  </ol> </li> 
 <li>默认主题改变，使用之前的<code>ksyun</code>主题作为默认主题，原来的默认主题不再支持</li> 
</ol> 
<p>组件变更请参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdesign.ksyun.com%2Fdocs%2Fchangelog%2F" target="_blank">https://design.ksyun.com/docs/changelog/</a></p>
                                        </div>
                                      
</div>
            