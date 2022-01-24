
---
title: 'vue-mapvgl vue3 版本正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7080'
author: 开源中国
comments: false
date: Mon, 24 Jan 2022 16:37:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7080'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">vue-mapvgl </span><span style="background-color:#ffffff; color:#333333">是一个基于vue和百度地图mapvgl封装的vue地图组件库，提供了常用组件封装，格外提供基础的模型加载和操作能力。</span></p> 
<h3>本次更新</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>组件全面升级支持vue3</li> 
 <li>代码使用typescript重写</li> 
 <li>增加IDE提示文件，快捷开发</li> 
 <li>文档全面更新，使用vuepress 2.0版本重新编写。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvue-mapvgl.guyixi.cn%2F" target="_blank">文档地址</a></li> 
 <li>支持treeshake</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">破坏性变更</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>库加载方式调整，需使用vue3的方式进行注册库</li> 
 <li>移除bmapManager，获取地图实例的方式将只支持ref和绑定init事件</li> 
 <li>移除所有组件events属性，事件绑定使用v-on形式</li> 
 <li>所有图层增加init事件，用于获取图层实例对象</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">NPM安装</h3> 
<pre><span style="color:#808080">npm install vue-bmap-gl@next --save
</span><span style="color:#808080">npm install vue-mapvgl@next --save</span></pre> 
<h3 style="margin-left:0; margin-right:0; text-align:left">引入组件</h3> 
<pre><span style="color:#808080">import App from './App.vue'
</span><span style="color:#808080">import VueBMap, &#123;initBMapApiLoader&#125; from 'vue-bmap-gl';
</span><span style="color:#808080">import 'vue-bmap-gl/dist/style.css'
</span><span style="color:#808080">import VueMapvgl from 'vue-mapvgl'
</span><span style="color:#808080">initBMapApiLoader(&#123;
</span><span style="color:#808080">    ak: 'YOUR_KEY'
</span><span style="color:#808080">&#125;)
</span>
<span style="color:#808080">createApp(App)
</span><span style="color:#808080">    .use(VueBMap)
</span><span style="color:#808080">    .use(VueMapvgl)
</span><span style="color:#808080">    .mount('#app')</span></pre> 
<h3><span style="background-color:#ffffff; color:#333333">示例</span></h3> 
<pre><span style="color:#e8bf6a"><template>
</span><span style="color:#e8bf6a">  <div </span><span style="color:#bababa">class</span><span style="color:#a5c261">="map-container"</span><span style="color:#e8bf6a">>
</span><span style="color:#e8bf6a">    <el-bmap
</span><span style="color:#e8bf6a">      </span><span style="color:#bababa">:center</span><span style="color:#a5c261">="</span>center<span style="color:#a5c261">"
</span><span style="color:#a5c261">      </span><span style="color:#bababa">:zoom</span><span style="color:#a5c261">="</span>zoom<span style="color:#a5c261">"
</span><span style="color:#a5c261">      </span><span style="color:#bababa">:tilt</span><span style="color:#a5c261">="</span><span style="color:#6897bb">75</span><span style="color:#a5c261">"
</span><span style="color:#a5c261">    </span><span style="color:#e8bf6a">>
</span><span style="color:#e8bf6a">      <el-bmapv-view>
</span><span style="color:#e8bf6a">        <el-bmapv-bar-layer
</span><span style="color:#e8bf6a">          </span><span style="color:#bababa">:visible</span><span style="color:#a5c261">="</span>visible<span style="color:#a5c261">"
</span><span style="color:#a5c261">          </span><span style="color:#bababa">type</span><span style="color:#a5c261">="light"
</span><span style="color:#a5c261">          </span><span style="color:#bababa">:data</span><span style="color:#a5c261">="</span>data<span style="color:#a5c261">"
</span><span style="color:#a5c261">          </span><span style="color:#bababa">:edge-count</span><span style="color:#a5c261">="</span><span style="color:#6897bb">50</span><span style="color:#a5c261">"
</span><span style="color:#a5c261">          </span><span style="color:#bababa">:size</span><span style="color:#a5c261">="</span><span style="color:#6897bb">200</span><span style="color:#a5c261">"
</span><span style="color:#a5c261">          </span><span style="color:#bababa">@init</span><span style="color:#a5c261">="</span>initLayer<span style="color:#a5c261">"
</span><span style="color:#a5c261">        </span><span style="color:#e8bf6a">/>
</span><span style="color:#e8bf6a">      </el-bmapv-view>
</span><span style="color:#e8bf6a">    </el-bmap>
</span><span style="color:#e8bf6a">  </div>
</span><span style="color:#e8bf6a">  <div </span><span style="color:#bababa">class</span><span style="color:#a5c261">="control-container"</span><span style="color:#e8bf6a">>
</span><span style="color:#e8bf6a">    <button </span><span style="color:#bababa">@click</span><span style="color:#a5c261">="</span>switchVisible<span style="color:#a5c261">"</span><span style="color:#e8bf6a">>
</span><span style="color:#e8bf6a">      </span>&#123;&#123; visible ? '<span>隐藏图层</span>' : '<span>显示图层</span>' &#125;&#125;
    <span style="color:#e8bf6a"></button>
</span><span style="color:#e8bf6a">  </div>
</span><span style="color:#e8bf6a"></template>
</span>
<span style="color:#e8bf6a"><script </span><span style="color:#bababa">lang</span><span style="color:#a5c261">="ts"</span><span style="color:#e8bf6a">>
</span><span style="color:#cc7832">import </span>&#123;defineComponent&#125; <span style="color:#cc7832">from </span><span style="color:#6a8759">"vue"</span><span style="color:#cc7832">;
</span>
<span style="color:#cc7832">export default </span>defineComponent(&#123;
  name: <span style="color:#6a8759">"Map"</span><span style="color:#cc7832">,
</span><span style="color:#cc7832">  </span>components: &#123;
  &#125;<span style="color:#cc7832">,
</span><span style="color:#cc7832">  </span>data()&#123;
    <span style="color:#cc7832">return </span>&#123;
      zoom: <span style="color:#6897bb">15</span><span style="color:#cc7832">,
</span><span style="color:#cc7832">      </span>center: [<span style="color:#6897bb">121.5273285</span><span style="color:#cc7832">, </span><span style="color:#6897bb">31.21515044</span>]<span style="color:#cc7832">,
</span><span style="color:#cc7832">      </span>visible: <span style="color:#cc7832">true,
</span><span style="color:#cc7832">      </span>data: [&#123;
        geometry: &#123;
          type: <span style="color:#6a8759">'Point'</span><span style="color:#cc7832">,
</span><span style="color:#cc7832">          </span>coordinates: [<span style="color:#6897bb">121.5273285</span><span style="color:#cc7832">, </span><span style="color:#6897bb">31.21515044</span>]<span style="color:#cc7832">,
</span><span style="color:#cc7832">        </span>&#125;<span style="color:#cc7832">,
</span><span style="color:#cc7832">        </span>height: <span style="color:#6897bb">100
</span><span style="color:#6897bb">      </span>&#125;<span style="color:#cc7832">,</span>&#123;
        geometry: &#123;
          type: <span style="color:#6a8759">'Point'</span><span style="color:#cc7832">,
</span><span style="color:#cc7832">          </span>coordinates: [<span style="color:#6897bb">121.5473285</span><span style="color:#cc7832">, </span><span style="color:#6897bb">31.21515044</span>]<span style="color:#cc7832">,
</span><span style="color:#cc7832">        </span>&#125;<span style="color:#cc7832">,
</span><span style="color:#cc7832">        </span>height: <span style="color:#6897bb">300
</span><span style="color:#6897bb">      </span>&#125;]
    &#125;
  &#125;<span style="color:#cc7832">,
</span><span style="color:#cc7832">  </span>methods: &#123;
    switchVisible()&#123;
      <span style="color:#cc7832">this</span>.visible = !<span style="color:#cc7832">this</span>.visible<span style="color:#cc7832">;
</span><span style="color:#cc7832">    </span>&#125;<span style="color:#cc7832">,
</span><span style="color:#cc7832">    </span>initLayer(layer)&#123;
      console.log(<span style="color:#6a8759">'init: '</span><span style="color:#cc7832">, </span>layer)
    &#125;
  &#125;
&#125;)
<span style="color:#e8bf6a"></script>
</span>

</pre>
                                        </div>
                                      
</div>
            