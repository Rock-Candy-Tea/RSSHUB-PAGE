
---
title: 'uniapp入门级最佳实践（三） _ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6989'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 19:03:26 GMT
thumbnail: 'https://picsum.photos/400/300?random=6989'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第20天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831?utm_campaign=31day&utm_medium=Push&utm_source=20210803" title="https://juejin.cn/post/6987962113788493831?utm_campaign=31day&utm_medium=Push&utm_source=20210803" target="_blank">8月更文挑战</a></strong></p>
<h3 data-id="heading-0">一、tab切换</h3>
<p>这里写的是tab页名字不一样，但是内容差不多，只是展示的切换后的标题栏状态不一样而已，内容还是同一个，如果每个内容都不一样，推荐用uniapp自带的，或者mui里的插件。</p>
<pre><code class="copyable"><view class="headNavBox flex">
<view class="headNavItem" v-for="item,index in navList" :key="index" @click="changeTab(index)">
<view class="headNavTitle">&#123;&#123;item.title&#125;&#125;</view>
<view :class="navIdx===index ? 'activeTab' : ''" :style="&#123;'margin-left': item.marginLeftNavBottom + '%' &#125;"></view>
</view>
</view>
<view class="dataItem" v-for="item,index in dataList" :key="index">&#123;&#123;item.name&#125;&#125;
</view>

js:
data() &#123;
return &#123;
navIdx: 0,
navList: [
&#123;
title: '全部的',
marginLeftNavBottom: 38,//这个是写死的，自己调样式看多大合适
state: ''
&#125;,&#123;
title: '待处理',
marginLeftNavBottom: 38,
state: 2
&#125;,&#123;
title: '处理中',
marginLeftNavBottom: 38,
state: 3
&#125;,&#123;
title: '已结束',
marginLeftNavBottom: 38,
state: 4
&#125;
],
dataList: []&#125;
&#125;,
methods: &#123;
//切换tab页
changeTab(idx) &#123;
this.navIdx = idx;
let state = this.navList[idx].state;
this.searchList(state);//state是状态调接口需要的
&#125;
&#125;

css:
.flex &#123;
display: flex;
&#125;
.headNavBox &#123;
width: 100%;
height: 80rpx;
background: #FFFFFF;
&#125;
.headNavItem &#123;
width: 33%;
text-align: center;
line-height: 74rpx;
&#125;
.headNavTitle &#123;
font-size: 28rpx;
color: #222222;
&#125;
.activeTab &#123;
width: 46rpx;
height: 6rpx;
background-image: linear-gradient(to right, #1eaf7b , #c7e2ac);
background-size: 100% 100%;
background-repeat: no-repeat;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>导航栏的tab里写死了marginLeftNavBottom是因为不太需要动态计算，因为是固定的，只要在开发的时候看哪个位置是居中的就可以了。</p>
<h3 data-id="heading-1">二、form表单使用</h3>
<p>这里主要写的是单选和多选框的使用，当时看着文档写了半个小时也没写对，感觉有点难理解。。。我这里开发的是类似做题目的项目，所以这里记录一下难点：</p>
<p>单选框：</p>
<pre><code class="copyable"><view class="questionItem" v-for="item,index in questionList">
<radio-group @change="changeCheck" :data-idx='index'>
<label class="uni-list-cell uni-list-cell-pd flex" v-for="(temp,jdx) in item.surveyOptionList" :key="jdx">
<view>
<radio :value="temp.optionId" color='#19AD78' :checked="temp.optionId == item.checkVal" :disabled="flag==2" />
</view>
<view>&#123;&#123;temp.sorting&#125;&#125;.&#123;&#123;temp.optionName&#125;&#125;</view>
</label>
</radio-group>
</view>
js:
changeCheck: function(evt) &#123;
let idx = evt.target.dataset.idx;
this.questionList[idx].checkVal = evt.detail.value;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个组件当时以为要设置name一直才会实现单选，原来在里就会自动单选，不会影响其他的，但是这里的change事件只能拿到当前的，拿不到里面选择了第几个选项，这就挺鸡肋的，但是我后来也没因为这个问题写不下去，也用不到了。</p>
<p>在用了data-index，方便下面写change事件的时候赋值，看文档那种写法，不好给这种数组类型的赋值。</p>
<p>单选框和多选框都差不多，就把组件名称换下就好了，连change事件都可以用一样的</p>
<h3 data-id="heading-2">三、生成二维码</h3>
<p>动态生成二维码，用的是<a href="https://link.juejin.cn/?target=https%3A%2F%2Funiapp.dcloud.io%2FuniCloud%2FREADME" target="_blank" rel="nofollow noopener noreferrer" title="https://uniapp.dcloud.io/uniCloud/README" ref="nofollow noopener noreferrer">uni-Cloud</a>里开源的插件，找了好几个，发现这个最好用，uni-cloud里可以直接用Hbuilder X导入组件，一键导入真的太方便了，但是这个有点问题，小程序正常展示，但是H5上面要调用第二次才展示，不知道是不是就我遇到了这个问题。</p>
<pre><code class="copyable"><view class="qrImg">
<tki-qrcode 
ref="qrcode" 
:val="val" 
:size="size" 
:unit="unit" 
:iconSize="iconsize" 
 :lv="lv" 
 :onval="onval" 
 :loadMake="loadMake"
 :showLoading="showLoading" 
 :loadingText="loadingText" />
<view class="appointmentInfoSubTxt" @click="scanImg()">刷新二维码</view>
</view>

<script>
import tkiQrcode from "@/components/tki-qrcode/tki-qrcode.vue";
export default &#123;
components: &#123;
tkiQrcode,
&#125;,
data() &#123;
return &#123;
//下面是二维码用到的参数
qrCode:"",
val: '',
size: 200,
iconsize: 30,
lv: 3,
onval: true,
unit: 'rpx',
loadMake: true,
showLoading: true,
loadingText: '二维码生成中'
&#125;
&#125;,
methods: &#123;
//生成二维码
scanImg(flag='') &#123;
let _this = this;
this.$utils.requestFun('/getCode',&#123;
token: getApp().globalData.token
&#125;,'GET').then(res=> &#123;
if(res.data.data && res.data.data != '') &#123;
_this.val = res.data.data;
// #ifdef H5
if(flag == '') &#123;
this.scanImg(1);//H5情况下要点两次才能出来二维码，很奇怪，所以多调用一次
&#125;
// #endif
&#125;
&#125;);
&#125;
&#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里只要把Val赋值就可以了，然后因为只有H5的平台上出现要调用两次才会生成二维码的问题，我就加了一个变量并且判断是否在H5平台上，不然就调用一次即可。</p>
<h3 data-id="heading-3">四、定时器轮询</h3>
<p>这个轮询就是在二维码的基础上进行开发的，需求是这个页面要一直调用接口，判断二维码是否被扫描过，一秒钟调用一次，如果扫描后就弹框提示，否则就一直调用接口，如果出页面就关闭定时器，所以在上面的代码加上一个searchTime: null的变量，然后在生成二维码接口的地方调用一个轮询的方法就行了，然后在生命周期里移除定时器：</p>
<pre><code class="copyable">searchTimer: null //轮询

methods: &#123;
//轮询查询二维码是否打开
invertalSearch() &#123;
let _this = this; 
this.searchTimer = setInterval(()=> &#123;
_this.searchState();//调用接口的方法，这里就不具体展示了
&#125;,1000)
&#125;
&#125;,
//这两个方法的格式一定要这样写，不然在H5里没用！不知道为啥，解决了好久才知道是这个问题！
onHide: function() &#123;
if(this.searchTimer) &#123;
clearInterval(this.searchTimer);
this.searchTimer = null;
&#125;
&#125;,
//页面卸载
onUnload: function() &#123;
if(this.searchTimer) &#123;
clearInterval(this.searchTimer);
this.searchTimer = null;
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            