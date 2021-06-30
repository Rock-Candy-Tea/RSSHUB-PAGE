
---
title: '前端开发：基于移动端的Vue项目的Loading使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/332e59cd94f1499a840f796854f473c7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 09:29:21 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/332e59cd94f1499a840f796854f473c7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第30天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h3 data-id="heading-0">前言</h3>
<p>在前端开发过程中，常用的组件有必要做一下使用的总结，尤其是对于刚入门的前端开发者来说既有利于知识点的掌握，又有利于总结归纳方便后期使用查看。不管是基于移动端还是PC端的前端Vue项目都是如此，那么本文就来分享一下在前端开发的时候经常使用的一个功能：Loading的使用，本文以基于移动端Vant的Loading使用为例来讲解，方便有需要的开发者学习使用。</p>
<h3 data-id="heading-1">Loading介绍</h3>
<p>Loading加载：加载图标，用来表示加载过程中的过渡状态，或者说是在加载数据的时候显示动效，起到缓冲作用。</p>
<h3 data-id="heading-2">引入Loading</h3>
<p>本示例以Vant下的Loading组件引入的方法为主，具体的引入步骤如下所示：
打开基于移动端的Vue项目，然后在项目的根目录里面找到main.js文件，然后直接引入Loading组件，其实项目里面如果引入了Vant组件，就不需要引入。这里直接在main.js文件中引入Loading组件即可。</p>
<pre><code class="copyable">import Vue from 'vue';  //框架如果已经引入过的话，这句就不用再加进去了

import &#123; Loading &#125; from 'vant';
Vue.use(Loading);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/332e59cd94f1499a840f796854f473c7~tplv-k3u1fbpfcp-watermark.image" alt="001.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">使用场景</h3>
<p>Loading的使用其实也可以根据实际开发过程中的具体需求来选择，可以自定义Loading加载的图标样式、颜色、大小、以及显示的位置和背景、文案等设置，具体的使用还是要根据实际的业务需求来做决定，这里不再一一介绍Loading加载的全部样式设置和显示情况。</p>
<h3 data-id="heading-4">示例</h3>
<p>本文示例以Loading加载的常规使用来做介绍，具体的核心代码如下所示：
1、</p>
<pre><code class="copyable"><template>
  <van-tabs v-model="tabActive" color="#459CFF" title-active-color="#459CFF"  sticky line-width="100px" class="talent-scout">
    <van-tab  class="tab-talent-scout"  title="推荐" :badge="boleRecommendTotal" >
      <BoleScreening  :detailData="boleDetail" :tabActive="tabActive" @searchEvent="onSearch"  @cancelEvent="cancelClick" />
          <van-cell-group class="recommend-group">
            <BoleScreeningItem :detailData="boleRecommendList" />
           <van-empty v-if="boleRecommendList.length === 0"  description="暂无数据" />
         </van-cell-group>
    </van-tab>
    <van-tab class="tab-talent-scout"  title="我的"  :badge="myRecommendTotal">
      <RecommendScreening  :subTicketNameData="subTicketName"  :tabActive="tabActive"  @serchData="serchClick" @serchCancel="serchCancel" />
          <van-cell-group class="recommend-group">
            <RecommendListItem :recommendData="myRecommendData" />
            <van-empty  v-if="myRecommendData.myRecommendList.length === 0"  description="暂无数据"  />
          </van-cell-group>
    </van-tab>
    <van-loading class="loading-bg" type="spinner" size="24px" v-show="httpLoading"/>
  </van-tabs>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/807209f7bcf94415a41e66aa8bf96884~tplv-k3u1fbpfcp-watermark.image" alt="002.jpeg" loading="lazy" referrerpolicy="no-referrer">
2、</p>
<pre><code class="copyable"><script>
import Container from "../../components/Container.vue";
export default &#123;
  data() &#123;
    return &#123;
      httpLoading:false,  //设置loading的默认初始值，默认状态是关闭状态，所以要置为false
    &#125;;
  &#125;,
  activated() &#123;
    this.getBoleRecommendList();
    this.getMyRecommendList();
  &#125;,
  created() &#123;&#125;,
  methods: &#123;
    //获取推荐列表
    async getBoleRecommendList(val = &#123;&#125;) &#123;
      this.httpLoading = true;  //网络请求开始的时候把loading设置为true，显示loading
      this.$service.java_recruit
        .getBoleRecommendList(&#123;
          params: &#123;
            search: val.keyword,
          &#125;,
        &#125;)
        .then((r) => &#123;
          if (r.status == 200) &#123;
            this.httpLoading = false;  //网络请求成功之后，把loading设置为false，隐藏loading
            r.data.rows[0].boleRecommendList.forEach((e) => &#123;
              this.boleRecommendList.push(e);
            &#125;);
          &#125;
        &#125;).catch((r) => &#123;
          this.httpLoading = false; //网络请求失败这里也要对loading做隐藏处理，不然在失败之后会一直显示loading
          this.$toast("加载失败！");
        &#125;);
    &#125;,
  &#125;,
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af4bbb98165745d29e68fd23f701b2a4~tplv-k3u1fbpfcp-watermark.image" alt="003.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e85720aa32d6421eabf742f43704c0bd~tplv-k3u1fbpfcp-watermark.image" alt="004.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>3、</p>
<pre><code class="copyable"><style scoped>
.talent-scout &#123;
  height: 100%;
&#125;

/*设置loading显示的样式*/
.loading-bg &#123;
  position: fixed;
  width: 60px;
  height: 60px;
  margin: -30px 0 0 -30px;
  background: rgba(0, 0, 0, 0.5);
  z-index: 9999;
  top: 50%;
  left: 50%;
  text-align: center;
  line-height: 60px;
  border-radius: 5px;
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6efd5a8f75c045ef8b9281878e67a289~tplv-k3u1fbpfcp-watermark.image" alt="005.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>4、示例效果</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cdc223b48d4e4be2b564d1dfa5161d6c~tplv-k3u1fbpfcp-watermark.image" alt="006.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>经过以上内容的操作之后，就实现了loading的加载和隐藏的使用。以上就是本章的全部内容，欢迎关注三掌柜的微信公众号“程序猿by三掌柜”，三掌柜的新浪微博“三掌柜666”，欢迎关注！</p></div>  
</div>
            