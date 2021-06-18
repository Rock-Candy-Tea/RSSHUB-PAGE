
---
title: 'vue 高德地图鼠标选取地址并可以选择地址，经纬度、vue-amap安装和使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1125'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 01:49:54 GMT
thumbnail: 'https://picsum.photos/400/300?random=1125'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">这只一个按钮，可选择并有弹出框的按钮</h2>
<pre><code class="copyable"><div style="display:inline-block;color:#409EFF;cursor:pointer">
      <i class="el-icon-location"></i>
      <span @click="opensetdi">选择地址</span>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">弹出框展示的方法</h2>
<pre><code class="copyable">opensetdi()&#123;
    this.$store.commit('setgdDialogVisible',true);
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">高德地铁弹出框html</h2>
<pre><code class="copyable"><el-dialog title="选取地址"  :visible.sync="this.$store.state.gdDialogVisible"  :before-close="addressclosedialog" width="30%" center>
<gdmap></gdmap>
<span class="dialog-footer" style="height: 60px;display: block;"></span>
</el-dialog>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">弹出框关闭</h2>
<pre><code class="copyable">addressclosedialog()&#123;
    this.$store.state.gdDialogVisible=false;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">import gdmap from '../components/Map'
    components:&#123;
        'gdmap':gdmap
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">vue-amap安装和使用</h2>
<p><a href="https://elemefe.github.io/vue-amap/#/zh-cn/introduction/install" target="_blank" rel="nofollow noopener noreferrer">vue-amap安装和使用文档</a></p>
<h3 data-id="heading-5">npm 安装</h3>
<pre><code class="copyable">npm install vue-amap --save
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">vue-amap main.js使用</h3>
<pre><code class="copyable">import VueAMap from 'vue-amap'

Vue.use(VueAMap);
VueAMap.initAMapApiLoader(&#123;
  key: 'b205a764fd89262a00033ccc515f623c',
  plugin: ['AMap.Autocomplete', 'AMap.PlaceSearch', 'AMap.Scale', 'AMap.OverView', 'AMap.ToolBar', 'AMap.MapType', 'AMap.PolyEditor', 'AMap.CircleEditor','AMap.Geocoder','AMap.Geolocation','AMap.MarkerClusterer'],
  // 默认高德 sdk 版本为 1.4.4
  v: '1.4.4'
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">新建组件Map.vue使用</h3>
<pre><code class="copyable"><!--
 * @Author: shh
 * @Date: 2021-04-02 10:31:58
 * @LastEditTime: 2021-05-06 18:40:52
 * @LastEditors: Please set LastEditors
 * @Description: 高德地图定位插件
 * @FilePath: 
-->

<template>
  <div
    class="amap-page-container"
    style="width: 95%; height:400px;margin:0 auto;margin-bottom:100px"
  >
    <el-amap-search-box
      class="search-box"
      :search-option="searchOption"
      :on-search-result="onSearchResult"
    ></el-amap-search-box>
    <el-amap
      ref="map"
      vid="amapDemo"
      :amap-manager="amapManager"
      :center="center"
      :zoom="zoom"
      :plugin="plugin"
      :events="events"
      class="amap-demo"
    ></el-amap>
    <p>&#123;&#123; address &#125;&#125;</p>
    <p>&#123;&#123; center &#125;&#125;</p>
    <span class="dialog-footer">
      <button type="button" class="el-button el-button--default" @click="sendcenaddress(1)">
        <span>取 消</span>
      </button>
      <button
        data-v-5d351510
        type="button"
        class="el-button el-button--primary"
        @click="sendcenaddress"
      >
        <span>确 定</span>
      </button>
    </span>
  </div>
</template>
<script>
import &#123; AMapManager &#125; from 'vue-amap'
let amapManager = new AMapManager()
export default &#123;
  data() &#123;
    const self = this
    return &#123;
      searchOption: &#123;
        //根据定位获取当前城市
        city: '上海',
        citylimit: false,
      &#125;,
      lng: '',
      lat: '',
      address: '',
      city: '',
      province: '',
      granaryCounty: '',
      granaryAddress: '',
      marker: '',
      amapManager,
      zoom: 12,
      center: [121.59996, 31.197646],
      events: &#123;
        init: (o) => &#123;
          o.getCity((result) => &#123;
            // console.log(result);
            // this.searchOption.city=result.city
          &#125;)
        &#125;,
        moveend: () => &#123;&#125;,
        zoomchange: () => &#123;&#125;,
        click: (e) => &#123;
          debugger
          //   console.log(e.lnglat);
          self.lng = e.lnglat.lng
          self.lat = e.lnglat.lat
          self.center = [self.lng, self.lat]
          //   console.log(e.lnglat, 1999);

          let o = amapManager.getMap()
          if (!self.marker) &#123;
            self.marker = new AMap.Marker(&#123;
              position: e.lnglat,
            &#125;)
            self.marker.setMap(o)
          &#125;
          self.marker.setPosition(e.lnglat)
          let geocoder = new AMap.Geocoder(&#123;&#125;)
          geocoder.getAddress(e.lnglat, function (status, result) &#123;
            if (status === 'complete' && result.regeocode) &#123;
              self.address = result.regeocode.formattedAddress
              self.city = result.regeocode.addressComponent.city
              self.province = result.regeocode.addressComponent.province
              self.granaryCounty = result.regeocode.addressComponent.district
              self.granaryAddress = result.regeocode.addressComponent.township
              self.$store.commit('setgranaryCity', self.city)
              self.$store.commit('setgranaryProvince', self.province)
              self.$store.commit('setgranaryCounty', self.granaryCounty)
              self.$store.commit('setgranaryAddress', self.granaryAddress)
            &#125; else &#123;
              log.error('根据经纬度查询地址失败')
            &#125;
          &#125;)
        &#125;,
      &#125;,
      plugin: [
        'ToolBar',
        &#123;
          pName: 'MapType',
          defaultType: 0,
          events: &#123;
            init(o) &#123;
              //   console.log(o);
            &#125;,
          &#125;,
        &#125;,
      ],
      plugin: [
        &#123;
          pName: 'Geolocation',
          events: &#123;
            init(o) &#123;
              debugger
              // o 是高德地图定位插件实例
              o.getCurrentPosition((status, result) => &#123;
                // console.log(JSON.stringify(result));
                if (result && result.position) &#123;
                  debugger
                  self.lng = result.position.lng
                  self.lat = result.position.lat
                  self.address = result.formattedAddress
                  self.center = [self.lng, self.lat]
                  self.city = result.addressComponent.city
                  self.province = result.addressComponent.province
                  self.granaryCounty = result.addressComponent.district
                  self.granaryAddress = result.addressComponent.township
                  self.$store.commit('setgranaryCity', self.city)
                  self.$store.commit('setgranaryProvince', self.province)
                  self.$store.commit('setgranaryCounty', self.granaryCounty)
                  self.$store.commit('setgranaryAddress', self.granaryAddress)
                  //   console.log(self.center, 99666);
                  let o = amapManager.getMap()
                  if (!self.marker) &#123;
                    self.marker = new AMap.Marker(&#123;
                      position: self.center,
                    &#125;)
                    self.marker.setMap(o)
                  &#125;
                  self.marker.setPosition(self.center)
                &#125;
              &#125;)
            &#125;,
          &#125;,
        &#125;,
      ],
    &#125;
  &#125;,
  methods: &#123;
    sendcenaddress(inde) &#123;
      debugger
      if (inde == 1) &#123;
        this.$store.commit('setmapcenter', '')
        this.$store.commit('setmapaddress', '')
        this.$store.commit('setgdDialogVisible', false)
      &#125; else &#123;
        this.$store.commit('setmapcenter', this.center)
        this.$store.commit('setmapaddress', this.address)
        this.$store.commit('setgdDialogVisible', false)
        this.$store.commit('setgranaryCity', this.city)
        this.$store.commit('setgranaryProvince', this.province)
        this.$store.commit('setgranaryCounty', this.granaryCounty)
        this.$store.commit('setgranaryAddress', this.granaryAddress)
      &#125;
    &#125;,
    onSearchResult(pois) &#123;
      debugger
      if (pois.length > 0) &#123;
        debugger
        let &#123; lng, lat, name, location &#125; = pois[0]
        let center = [lng, lat]
        this.lng = lng
        this.lat = lat
        this.center = [lng, lat]
        let o = amapManager.getMap()
        if (!this.marker) &#123;
          this.marker = new AMap.Marker(&#123;
            position: center,
          &#125;)
          this.marker.setMap(o)
        &#125;
        this.marker.setPosition(center)
        // 近来补充  根据经纬度查询地址
        let geocoder = new AMap.Geocoder(&#123;&#125;)
        let that = this
        geocoder.getAddress(location, function (status, result) &#123;
          console.log(status, result)
          if (status === 'complete' && result.regeocode) &#123;
            that.address = result.regeocode.formattedAddress
            that.city = result.regeocode.addressComponent.city
            that.province = result.regeocode.addressComponent.province
            that.granaryCounty = result.regeocode.addressComponent.district
            that.granaryAddress = result.regeocode.addressComponent.township
            that.$store.commit('setgranaryCity', self.city)
            that.$store.commit('setgranaryProvince', self.province)
            that.$store.commit('setgranaryCounty', self.granaryCounty)
            that.$store.commit('setgranaryAddress', self.granaryAddress)
          &#125; else &#123;
            console.log('根据经纬度查询地址失败')
          &#125;
        &#125;)
      &#125;
    &#125;,
  &#125;,
&#125;
</script>
<style scoped>
.search-box &#123;
  position: absolute;
  top: 25px;
  left: 20px;
&#125;
.amap-page-container &#123;
  position: relative;
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            