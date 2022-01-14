
---
title: 'vue-bmap-gl vue3 版本正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7930'
author: 开源中国
comments: false
date: Fri, 14 Jan 2022 18:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7930'
---

<div>   
<div class="content">
                                                                                            <p>vue-bmap-gl <span data-darkreader-inline-bgcolor data-darkreader-inline-color style="--darkreader-inline-bgcolor:#181a1b; --darkreader-inline-color:#c8c3bc; background-color:#ffffff; color:#333333">是一个基于vue和百度地图GL版本封装的vue地图组件库，提供了常用组件封装。</span></p> 
<h3>本次更新</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>组件全面升级支持vue3</li> 
 <li>代码使用typescript重写</li> 
 <li>增加IDE提示文件，快捷开发</li> 
 <li>文档全面更新，使用vuepress 2.0版本重新编写。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvue-bmap-gl.guyixi.cn" target="_blank">文档地址</a></li> 
 <li>支持treeshake</li> 
</ul> 
<h3>破坏性变更</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>库加载方式调整，需使用vue3的方式进行注册库</li> 
 <li>infoWindow的visible属性不再支持.sync使用，需要调整为v-model:visible</li> 
 <li>移除bmapManager，获取地图实例的方式将只支持ref和绑定init事件</li> 
 <li>移除所有组件events属性，事件绑定使用v-on形式</li> 
</ul> 
<h3>NPM安装</h3> 
<pre style="margin-left:0; margin-right:0; text-align:left"><span data-darkreader-inline-color style="--darkreader-inline-color:#988f81; color:#808080"><span data-darkreader-inline-color style="--darkreader-inline-color:#da4b58; color:#d73a49">npm</span> <span data-darkreader-inline-color style="--darkreader-inline-color:#da4b58; color:#d73a49">install</span> vue-bmap-gl@<span data-darkreader-inline-color style="--darkreader-inline-color:#da4b58; color:#d73a49">next</span> --save</span></pre> 
<h3>引入组件</h3> 
<pre><span data-darkreader-inline-color style="--darkreader-inline-color:#988f81; color:#808080">import App from './App.vue'
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#988f81; color:#808080">import VueBMap, &#123;initBMapApiLoader&#125; from 'vue-bmap-gl';
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#988f81; color:#808080">import 'vue-bmap-gl/dist/style.css'
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#988f81; color:#808080">initBMapApiLoader(&#123;
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#988f81; color:#808080">    ak: 'YOUR_KEY'
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#988f81; color:#808080">&#125;)
</span>
<span data-darkreader-inline-color style="--darkreader-inline-color:#988f81; color:#808080">createApp(App)
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#988f81; color:#808080">    .use(VueBMap)
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#988f81; color:#808080">    .mount('#app')</span></pre> 
<p>示例</p> 
<pre><span data-darkreader-inline-color style="--darkreader-inline-color:#e8bf6b; color:#e8bf6a"><template>
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#e8bf6b; color:#e8bf6a">  <div </span><span data-darkreader-inline-color style="--darkreader-inline-color:#bcb7ae; color:#bababa">class</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">="bmap-page-container"</span><span data-darkreader-inline-color style="--darkreader-inline-color:#e8bf6b; color:#e8bf6a">>
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#e8bf6b; color:#e8bf6a">    <el-bmap
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#e8bf6b; color:#e8bf6a">      </span><span data-darkreader-inline-color style="--darkreader-inline-color:#bcb7ae; color:#bababa">ref</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">="map"
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">      </span><span data-darkreader-inline-color style="--darkreader-inline-color:#bcb7ae; color:#bababa">:lazy</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">="</span><span data-darkreader-inline-color style="--darkreader-inline-color:#729fc0; color:#6897bb">2000</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">"
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">      </span><span data-darkreader-inline-color style="--darkreader-inline-color:#bcb7ae; color:#bababa">:map-style-v2</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">="</span><span data-darkreader-inline-color style="--darkreader-inline-color:#a29a8e; color:#9876aa">darkStyle</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">"
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">      </span><span data-darkreader-inline-color style="--darkreader-inline-color:#bcb7ae; color:#bababa">:preserve-drawing-buffer</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">="</span><span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">true</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">"
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">      </span><span data-darkreader-inline-color style="--darkreader-inline-color:#bcb7ae; color:#bababa">:min-zoom</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">="</span><span data-darkreader-inline-color style="--darkreader-inline-color:#729fc0; color:#6897bb">10</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">"
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">      </span><span data-darkreader-inline-color style="--darkreader-inline-color:#bcb7ae; color:#bababa">:max-zoom</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">="</span><span data-darkreader-inline-color style="--darkreader-inline-color:#729fc0; color:#6897bb">22</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">"
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">      </span><span data-darkreader-inline-color style="--darkreader-inline-color:#bcb7ae; color:#bababa">:tilt</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">="</span><span data-darkreader-inline-color style="--darkreader-inline-color:#a29a8e; color:#9876aa">tilt</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">"
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">      </span><span data-darkreader-inline-color style="--darkreader-inline-color:#bcb7ae; color:#bababa">:heading</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">="</span><span data-darkreader-inline-color style="--darkreader-inline-color:#a29a8e; color:#9876aa">heading</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">"
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">      </span><span data-darkreader-inline-color style="--darkreader-inline-color:#bcb7ae; color:#bababa">:center</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">="</span><span data-darkreader-inline-color style="--darkreader-inline-color:#a29a8e; color:#9876aa">center</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">"
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">      </span><span data-darkreader-inline-color style="--darkreader-inline-color:#bcb7ae; color:#bababa">:zoom</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">="</span><span data-darkreader-inline-color style="--darkreader-inline-color:#a29a8e; color:#9876aa">zoom</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">"
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">      </span><span data-darkreader-inline-color style="--darkreader-inline-color:#bcb7ae; color:#bababa">,@click</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">="click"
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">      </span><span data-darkreader-inline-color style="--darkreader-inline-color:#bcb7ae; color:#bababa">@tilesloaded</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">="</span><span data-darkreader-inline-color style="--darkreader-inline-color:#ffc366; color:#ffc66d">tilesloaded</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">"
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">    </span><span data-darkreader-inline-color style="--darkreader-inline-color:#e8bf6b; color:#e8bf6a">/>
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#e8bf6b; color:#e8bf6a">  </div>
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#e8bf6b; color:#e8bf6a">  <div </span><span data-darkreader-inline-color style="--darkreader-inline-color:#bcb7ae; color:#bababa">class</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">="control-container"</span><span data-darkreader-inline-color style="--darkreader-inline-color:#e8bf6b; color:#e8bf6a">>
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#e8bf6b; color:#e8bf6a">    <button </span><span data-darkreader-inline-color style="--darkreader-inline-color:#bcb7ae; color:#bababa">@click</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">="</span><span data-darkreader-inline-color style="--darkreader-inline-color:#ffc366; color:#ffc66d">getMap</span>()<span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">"</span><span data-darkreader-inline-color style="--darkreader-inline-color:#e8bf6b; color:#e8bf6a">>
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#e8bf6b; color:#e8bf6a">      </span><span>获取地图示例
</span><span>    </span><span data-darkreader-inline-color style="--darkreader-inline-color:#e8bf6b; color:#e8bf6a"></button>
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#e8bf6b; color:#e8bf6a">  </div>
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#e8bf6b; color:#e8bf6a"></template>
</span>

<span data-darkreader-inline-color style="--darkreader-inline-color:#e8bf6b; color:#e8bf6a"><script </span><span data-darkreader-inline-color style="--darkreader-inline-color:#bcb7ae; color:#bababa">lang</span><span data-darkreader-inline-color style="--darkreader-inline-color:#abc66c; color:#a5c261">="ts"</span><span data-darkreader-inline-color style="--darkreader-inline-color:#e8bf6b; color:#e8bf6a">>
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">import </span>&#123;<span data-darkreader-inline-color style="--darkreader-inline-color:#ffc366; color:#ffc66d">defineComponent</span>&#125; <span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">from </span><span data-darkreader-inline-color style="--darkreader-inline-color:#a1998d; color:#6a8759">"vue"</span><span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">;
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">import </span>darkStyle <span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">from </span><span data-darkreader-inline-color style="--darkreader-inline-color:#a1998d; color:#6a8759">'../../../assets/mapStyle'
</span>
<span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">export default </span><span data-darkreader-inline-color style="--darkreader-inline-color:#ffc366; color:#ffc66d">defineComponent</span>(&#123;
  <span data-darkreader-inline-color style="--darkreader-inline-color:#ffc366; color:#ffc66d">data</span>() &#123;
    <span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">return </span>&#123;
      <span data-darkreader-inline-color style="--darkreader-inline-color:#a29a8e; color:#9876aa">zoom</span>: <span data-darkreader-inline-color style="--darkreader-inline-color:#729fc0; color:#6897bb">16</span><span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">,
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">      </span><span data-darkreader-inline-color style="--darkreader-inline-color:#a29a8e; color:#9876aa">center</span>: [<span data-darkreader-inline-color style="--darkreader-inline-color:#729fc0; color:#6897bb">121.59996</span><span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">, </span><span data-darkreader-inline-color style="--darkreader-inline-color:#729fc0; color:#6897bb">31.197646</span>]<span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">,
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">      </span><span data-darkreader-inline-color style="--darkreader-inline-color:#a29a8e; color:#9876aa">tilt</span>: <span data-darkreader-inline-color style="--darkreader-inline-color:#729fc0; color:#6897bb">60</span><span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">,
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">      </span><span data-darkreader-inline-color style="--darkreader-inline-color:#a29a8e; color:#9876aa">heading</span>: <span data-darkreader-inline-color style="--darkreader-inline-color:#729fc0; color:#6897bb">0</span><span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">,
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">      </span>darkStyle<span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">,
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">      </span><span data-darkreader-inline-color style="--darkreader-inline-color:#a29a8e; color:#9876aa">timer</span>: <span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">null,
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">    </span>&#125;<span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">;
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">  </span>&#125;<span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">,
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">  </span><span data-darkreader-inline-color style="--darkreader-inline-color:#ffc366; color:#ffc66d">mounted</span>() &#123;
    <span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">const </span><span data-darkreader-inline-color style="--darkreader-inline-color:#ffc366; color:#ffc66d">change </span>= () =>&#123;
      <span data-darkreader-inline-color style="--darkreader-inline-color:#ffc366; color:#ffc66d">clearTimeout</span>(<span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">this</span>.<span data-darkreader-inline-color style="--darkreader-inline-color:#a29a8e; color:#9876aa">timer</span>)<span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">;
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">      </span><em>window</em>.<span data-darkreader-inline-color style="--darkreader-inline-color:#ffc366; color:#ffc66d">removeEventListener</span>(<span data-darkreader-inline-color style="--darkreader-inline-color:#a1998d; color:#6a8759">'hashchange'</span><span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">,</span><span data-darkreader-inline-color style="--darkreader-inline-color:#ffc366; color:#ffc66d">change</span>)
    &#125;
    <em>window</em>.<span data-darkreader-inline-color style="--darkreader-inline-color:#ffc366; color:#ffc66d">addEventListener</span>(<span data-darkreader-inline-color style="--darkreader-inline-color:#a1998d; color:#6a8759">'hashchange'</span><span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">,</span><span data-darkreader-inline-color style="--darkreader-inline-color:#ffc366; color:#ffc66d">change</span>)
  &#125;<span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">,
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">  </span><span data-darkreader-inline-color style="--darkreader-inline-color:#a29a8e; color:#9876aa">methods</span>: &#123;
    <span data-darkreader-inline-color style="--darkreader-inline-color:#ffc366; color:#ffc66d">getMap</span>() &#123;
      <span data-darkreader-inline-color style="--darkreader-inline-color:#988f81; color:#808080">// bmap vue component
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#988f81; color:#808080">      // </span><span data-darkreader-inline-color style="--darkreader-inline-color:#988f81; color:#808080">百度</span><span data-darkreader-inline-color style="--darkreader-inline-color:#988f81; color:#808080"> map instance
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#988f81; color:#808080">      </span><em>console</em>.<span data-darkreader-inline-color style="--darkreader-inline-color:#ffc366; color:#ffc66d">log</span>(<span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">this</span>.<span data-darkreader-inline-color style="--darkreader-inline-color:#a29a8e; color:#9876aa">$refs</span>.<span data-darkreader-inline-color style="--darkreader-inline-color:#a29a8e; color:#9876aa">map</span>.$$getInstance())<span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">;
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">    </span>&#125;<span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">,
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">    </span><span data-darkreader-inline-color style="--darkreader-inline-color:#ffc366; color:#ffc66d">panMap</span>() &#123;
      <span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">this</span>.<span data-darkreader-inline-color style="--darkreader-inline-color:#a29a8e; color:#9876aa">timer </span>= <span data-darkreader-inline-color style="--darkreader-inline-color:#ffc366; color:#ffc66d">setTimeout</span>( () => &#123;
        <span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">this</span>.<span data-darkreader-inline-color style="--darkreader-inline-color:#a29a8e; color:#9876aa">center </span>= [(<span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">this</span>.<span data-darkreader-inline-color style="--darkreader-inline-color:#a29a8e; color:#9876aa">center</span>[<span data-darkreader-inline-color style="--darkreader-inline-color:#729fc0; color:#6897bb">0</span>]+<span data-darkreader-inline-color style="--darkreader-inline-color:#729fc0; color:#6897bb">0.0001</span>)<span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">, this</span>.<span data-darkreader-inline-color style="--darkreader-inline-color:#a29a8e; color:#9876aa">center</span>[<span data-darkreader-inline-color style="--darkreader-inline-color:#729fc0; color:#6897bb">1</span>]]<span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">;
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">        this</span>.<span data-darkreader-inline-color style="--darkreader-inline-color:#ffc366; color:#ffc66d">panMap</span>()<span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">;
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">      </span>&#125;<span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">,</span><span data-darkreader-inline-color style="--darkreader-inline-color:#729fc0; color:#6897bb">1000</span>)<span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">;
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">    </span>&#125;<span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">,
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">    </span><span data-darkreader-inline-color style="--darkreader-inline-color:#ffc366; color:#ffc66d">click</span>()&#123;
      <span data-darkreader-inline-color style="--darkreader-inline-color:#ffc366; color:#ffc66d">alert</span>(<span data-darkreader-inline-color style="--darkreader-inline-color:#a1998d; color:#6a8759">'map clicked'</span>)<span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">;
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">    </span>&#125;<span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">,
</span><span data-darkreader-inline-color style="--darkreader-inline-color:#d28647; color:#cc7832">    </span><span data-darkreader-inline-color style="--darkreader-inline-color:#ffc366; color:#ffc66d">tilesloaded</span>(e)&#123;
      <em>console</em>.<span data-darkreader-inline-color style="--darkreader-inline-color:#ffc366; color:#ffc66d">log</span>(<span data-darkreader-inline-color style="--darkreader-inline-color:#a1998d; color:#6a8759">'tilesloaded'</span>)
    &#125;
  &#125;
&#125;)
<span data-darkreader-inline-color style="--darkreader-inline-color:#e8bf6b; color:#e8bf6a"></script>
</span></pre> 
<p> </p>
                                        </div>
                                      
</div>
            