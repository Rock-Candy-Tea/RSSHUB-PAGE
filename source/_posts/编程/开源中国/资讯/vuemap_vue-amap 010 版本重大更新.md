
---
title: 'vuemap_vue-amap 0.1.0 版本重大更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6499'
author: 开源中国
comments: false
date: Mon, 18 Apr 2022 11:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6499'
---

<div>   
<div class="content">
                                                                                            <p>@vuemap/vue-amap的vue2版本迎来了重大更新，新版本版本号0.1.0，该版本有三大重要变化</p> 
<p>1、地图组件现在支持包装使用了，可以将多个子组件按业务情况进行包装使用，比如叠加高精地图，可以将线和面封装到一个vue文件中，在多处使用</p> 
<p>2、新特性，现在支持自定义自己的地图组件，提供了registerMixin</p> 
<p>3、initAMapLoader增加securityJsCode<span>和</span>serviceHost<span>，用于适应新版本的</span>key</p> 
<p> </p> 
<p>下面是新版本的示例</p> 
<h4>1、地图组件包装</h4> 
<p>创建 <span style="background-color:#dddddd">CustomLoca.vue</span> 文件</p> 
<pre><span style="color:#6a8759"><template>
</span><span style="color:#6a8759">  <div>
</span><span style="color:#6a8759">    <el-amap-loca-line :source-url="sourceUrl" :layer-style="layerStyle"></el-amap-loca-line>
</span><span style="color:#6a8759">  </div>
</span><span style="color:#6a8759"></template>
</span>
<span style="color:#6a8759"><script>
</span><span style="color:#6a8759">var colors = ['#f7fcf5', '#e5f5e0', '#c7e9c0', '#a1d99b', '#74c476', '#41ab5d', '#238b45', '#006d2c', '#00441b'].reverse();
</span><span style="color:#6a8759">export default &#123;
</span><span style="color:#6a8759">  name: "CustomLoca",
</span><span style="color:#6a8759">  data()&#123;
</span><span style="color:#6a8759">    return &#123;
</span><span style="color:#6a8759">      sourceUrl: 'https://a.amap.com/Loca/static/loca-v2/demos/mock_data/bj_bus.json',
</span><span style="color:#6a8759">      layerStyle: &#123;
</span><span style="color:#6a8759">        color: function (index) &#123;
</span><span style="color:#6a8759">          var i = index % colors.length;
</span><span style="color:#6a8759">          return colors[i];
</span><span style="color:#6a8759">        &#125;,
</span><span style="color:#6a8759">        lineWidth: (index) => &#123;
</span><span style="color:#6a8759">          var i = index % colors.length;
</span><span style="color:#6a8759">          return i * 0.1 + 2;
</span><span style="color:#6a8759">        &#125;,
</span><span style="color:#6a8759">        altitude: function (index) &#123;
</span><span style="color:#6a8759">          var i = index % colors.length;
</span><span style="color:#6a8759">          return 100 * i;
</span><span style="color:#6a8759">        &#125;,
</span><span style="color:#6a8759">        // dashArray: [10, 5, 10, 0],
</span><span style="color:#6a8759">        dashArray: [10, 0, 10, 0],
</span><span style="color:#6a8759">      &#125;
</span><span style="color:#6a8759">    &#125;
</span><span style="color:#6a8759">  &#125;
</span><span style="color:#6a8759">&#125;
</span><span style="color:#6a8759"></script>
</span>
<span style="color:#6a8759"><style scoped>
</span>
<span style="color:#6a8759"></style></span></pre> 
<p>地图加载组件</p> 
<pre><span style="color:#6a8759"><template>
</span><span style="color:#6a8759">  <div id="app">
</span><span style="color:#6a8759">    <el-amap :center="[116.335036, 39.900082]" :zoom="8">
</span><span style="color:#6a8759">      <el-amap-loca>
</span><span style="color:#6a8759">        <custom-loca/>
</span><span style="color:#6a8759">      </el-amap-loca>
</span><span style="color:#6a8759">    </el-amap>
</span><span style="color:#6a8759">    <test-root />
</span><span style="color:#6a8759">  </div>
</span><span style="color:#6a8759"></template>
</span>
<span style="color:#6a8759"><script>
</span><span style="color:#6a8759">import CustomLoca from './components/CustomLoca'
</span>
<span style="color:#6a8759">export default &#123;
</span><span style="color:#6a8759">  name: 'App',
</span><span style="color:#6a8759">  components: &#123;
</span><span style="color:#6a8759">    CustomLoca
</span><span style="color:#6a8759">  &#125;
</span><span style="color:#6a8759">&#125;
</span><span style="color:#6a8759"></script>
</span>
<span style="color:#6a8759"><style>
</span><span style="color:#6a8759">#app &#123;
</span><span style="color:#6a8759">  height: 600px;
</span><span style="color:#6a8759">&#125;
</span><span style="color:#6a8759"></style></span></pre> 
<p>2、自定义地图组件</p> 
<p>创建 <span style="background-color:#dddddd">test.vue</span> 组件</p> 
<pre><span style="color:#6a8759"><template>
</span><span style="color:#6a8759">  <div>
</span><span style="color:#6a8759">  </div>
</span><span style="color:#6a8759"></template>
</span>
<span style="color:#6a8759"><script>
</span><span style="color:#6a8759">import &#123;registerMixin&#125; from "@vuemap/vue-amap";
</span>
<span style="color:#6a8759">export default &#123;
</span><span style="color:#6a8759">  name: "test",
</span><span style="color:#6a8759">  mixins: [registerMixin],
</span><span style="color:#6a8759">  methods: &#123;
</span><span style="color:#6a8759">    __initComponent()&#123;
</span><span style="color:#6a8759">      let map = this.parentInstance.$amapComponent;
</span><span style="color:#6a8759">      let position = this.parentInstance.$amapComponent.getCenter();
</span><span style="color:#6a8759">      let marker = new AMap.Marker(&#123;
</span><span style="color:#6a8759">        position: position
</span><span style="color:#6a8759">      &#125;)
</span><span style="color:#6a8759">      map.add(marker);
</span><span style="color:#6a8759">    &#125;
</span><span style="color:#6a8759">  &#125;
</span><span style="color:#6a8759">&#125;
</span><span style="color:#6a8759"></script>
</span>
<span style="color:#6a8759"><style scoped>
</span>
<span style="color:#6a8759"></style></span></pre> 
<p>地图加载test.vue组件</p> 
<pre><span style="color:#6a8759"><template>
</span><span style="color:#6a8759">  <div id="app">
</span><span style="color:#6a8759">    <el-amap :center="[116.335036, 39.900082]" :zoom="8">
</span><span style="color:#6a8759">      <test />
</span><span style="color:#6a8759">    </el-amap>
</span><span style="color:#6a8759">    <test-root />
</span><span style="color:#6a8759">  </div>
</span><span style="color:#6a8759"></template>
</span>
<span style="color:#6a8759"><script>
</span><span style="color:#6a8759">import test from './components/test'
</span>
<span style="color:#6a8759">export default &#123;
</span><span style="color:#6a8759">  name: 'App',
</span><span style="color:#6a8759">  components: &#123;
</span><span style="color:#6a8759">    test
</span><span style="color:#6a8759">  &#125;
</span><span style="color:#6a8759">&#125;
</span><span style="color:#6a8759"></script>
</span>
<span style="color:#6a8759"><style>
</span><span style="color:#6a8759">#app &#123;
</span><span style="color:#6a8759">  height: 600px;
</span><span style="color:#6a8759">&#125;
</span><span style="color:#6a8759"></style></span></pre> 
<p> </p> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            