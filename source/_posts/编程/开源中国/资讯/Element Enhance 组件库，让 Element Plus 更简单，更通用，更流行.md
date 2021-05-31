
---
title: 'Element Enhance 组件库，让 Element Plus 更简单，更通用，更流行'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-c3b0bdd1949c7e48db256f1c3e05a9730f0.png'
author: 开源中国
comments: false
date: Mon, 31 May 2021 11:13:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-c3b0bdd1949c7e48db256f1c3e05a9730f0.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Element Enhance 是基于 Element Plus 而开发的模板组件，提供了更高级别的抽象支持，开箱即用，更加专注于页面。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjmysy.github.io%2Felement-enhance%2Fzh-CN%2Fcomponents%2Flayout" target="_blank">开发文档</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjmysy.github.io%2Felement-enhance%2Fzh-CN%2Fguide%2Fchange" target="_blank">更新日志</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJmysy%2Felement-enhance%2Fissues" target="_blank">常见问题</a> | <a href="https://gitee.com/Jmysy/element-enhance/issues/I3TIE4">发布需求</a></p> 
<p><img height="128" src="https://oscimg.oschina.net/oscnet/up-c3b0bdd1949c7e48db256f1c3e05a9730f0.png" width="719" referrerpolicy="no-referrer"></p> 
<p> 📢 理念</p> 
<p>Element Plus 定义了基础的设计规范，对应也提供了大量的基础组件。但是对于中后台类应用，我们希望提供更高程度的抽象，提供更上层的设计规范，并且对应提供相应的组件使得开发者可以快速搭建出高质量的页面。</p> 
<p>列表页应该可以用 EleLayout + EleTable 完成，编辑页应该使用 EleLayout + EleForm 完成，详情页可以用 EleLayout + EleDescriptions 完成。 一个页面在开发工程中只需要关注几个重型组件，降低心智负担，专注于更核心的业务逻辑。</p> 
<p> ⚡ 设计</p> 
<p>在实际开发中我们也经常会碰到一些设计问题，比如经典的按钮应该放在左面还是右面，查询表单怎么布局，日期怎么格式化，数字的对齐问题，在重型组件中都进行了抽象，对于各种行为与样式我们都经过了设计师的讨论与设计可以达到默认好看及好用。</p> 
<p>如果你还是想自定义相关渲染可以通过自定义 ModelValue 的方式来实现。默认的不一定是最好的，但是一定不差，如果你要自定义最好考虑一下投入产出比，毛坯房里雕花真的好吗？</p> 
<p> ✒️ 特性</p> 
<p>该组件库的开发理念就是面向未来，如果查看源码你就会发现像是 vue 3 的实验性功能、像是 CSSNext 的 [CSS Variables]。在保证大部分浏览器的兼容性的情况下，会更多的使用新特性、新功能来开发</p> 
<p> ☁️ 入门</p> 
<p>让 Element Plus 更简单, 更通用, 更流行</p> 
<p><img height="392" src="https://oscimg.oschina.net/oscnet/up-cf33e4b66bfb4999c341c6f66930a4e658a.png" width="1758" referrerpolicy="no-referrer"></p> 
<p>安装</p> 
<pre>npm install element-enhance --save</pre> 
<p>引入</p> 
<pre>import &#123; createApp &#125; from 'vue'
import App from './App.vue'
import ElementEnhance from 'element-enhance'
import 'element-enhance/lib/style.css'

const app = createApp(App)

app.use(ElementEnhance)
app.mount('#app')</pre> 
<p>使用</p> 
<pre><template>
  <ele-layout multi-tab="true" breadcrumb="true">
    <template #logo></template>
  </ele-layout>
</template></pre> 
<p>效果</p> 
<p><img height="895" src="https://oscimg.oschina.net/oscnet/up-bb0263155382290535817e69b1ab0cc7f40.png" width="1871" referrerpolicy="no-referrer"></p> 
<p>🍚 贡献</p> 
<p>组件库还处于早期开发阶段，功能还需要完善。如果你希望参与贡献，欢迎 [Pull Request]。如果只是简单的文档相关的错误修正，你可以直接 PR，但如果是当前组件的 BUG 或者新功能、新组件等，最好优先提 [issues]</p>
                                        </div>
                                      
</div>
            