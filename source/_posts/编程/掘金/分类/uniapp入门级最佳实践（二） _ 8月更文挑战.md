
---
title: 'uniapp入门级最佳实践（二） _ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a28400b357e4f9a8e6b57b2780d8477~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 19:18:24 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a28400b357e4f9a8e6b57b2780d8477~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第19天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831?utm_campaign=31day&utm_medium=Push&utm_source=20210803" title="https://juejin.cn/post/6987962113788493831?utm_campaign=31day&utm_medium=Push&utm_source=20210803" target="_blank">8月更文挑战</a></strong></p>
<h3 data-id="heading-0">一、封装请求接口</h3>
<p>1、创建utils/utils.js在根目录与pages同级</p>
<pre><code class="copyable">//封装请求方法
let baseUrl = 'https://abc.cn';
function requestFun(url,data=&#123;&#125;,method='GET') &#123;
if(data.token && data.token == '') &#123;
uni.showToast(&#123; title: '请登录', icon: 'none' ,success() &#123;
uni.navigateTo(&#123;
url: '/pages/login/login',
&#125;);
&#125;&#125;)
return false;
&#125;
return new Promise((resolve, reject) => &#123;
uni.showLoading(&#123;title:'加载中',mask: true&#125;)
uni.request(&#123;
url: baseUrl + url,
method: method,
data: data,
header: &#123;
'content-type': 'application/json'
&#125;,
success: (res) => &#123;
uni.hideLoading();
if(res.statusCode == 200) &#123;
    resolve(res);
&#125;else &#123;
    uni.showToast(&#123;
title: res.data.msg == null ? '系统繁忙，请稍后再试' : res.data.msg,
icon: 'none'
    &#125;)
    reject(res);
&#125;
&#125;,
fail: (res) => &#123;
uni.hideLoading();
uni.showToast(&#123;
title: "系统繁忙，请稍后再试",
icon: 'none'
&#125;)
reject(res);
&#125;
&#125;)
&#125;)
&#125;

//把所有方法导出暴露出去
module.exports = &#123;
requestFun: requestFun
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里封装的方法，接收参数是地址，参数，请求方式，也可以自己加一些其他需要的参数，目前我用到的已经够用了，使用promise的方式调用接口，把接口放回的数据状态resolve/reject出去，然后相应的做出提示，这里掉完接口可以拿到请求接口的状态码：200,404这些，可以再做一些跳转。</p>
<p>封装请求的时候我加了loading，并且加了蒙层，不能点击，不然用户操作会点击多次。</p>
<p><strong>调用方式</strong>：</p>
<pre><code class="copyable">let _this = this;
this.$utils.requestFun('/hh/searchList',&#123;
    token: getApp().globalData.token
&#125;,'GET').then(res=> &#123;
    _this.dataList = res.data.data;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里调用的方式很简单，值需要传入接口地址，参数，请求方式，这里的this.$utils，要在<strong>main.js里配置</strong>，上一章讲过：</p>
<pre><code class="copyable">import utils from '@/utils/utils.js';、

Vue.prototype.$utils = utils;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>main.js引用utils，并且在vue的原型里加入这个对象，后面调用的时候只需要在前面加this.就可以了，utils.js里可以加很多公共方法完全够用</p>
<h3 data-id="heading-1">二、动态修改导航栏名称</h3>
<pre><code class="copyable">onLoad(options)&#123;
    if(options.flag == 1) &#123;
        uni.setNavigationBarTitle(&#123;            title: '名字'
        &#125;)    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是uniapp自带的，如果一个页面是可以重复使用的，只是标题名称不一样，在前面加一些判断修改标题名称就可以了.</p>
<h3 data-id="heading-2">三、上传图片</h3>
<pre><code class="copyable">let _this = this;
wx.chooseImage(&#123;
count: 1,//可以选择的上传图片数量
success:(res) => &#123;
const tempFilePaths = res.tempFilePaths;
uni.uploadFile(&#123;
url: getApp().globalData.serverUrl+'/file/upload', //仅为示例，非真实的接口地址
filePath: tempFilePaths[0],
name: 'file',
formData: &#123;
token: getApp().globalData.token,
file: tempFilePaths[0]
&#125;,
success: (uploadFileRes) => &#123;
let imgData = JSON.parse(uploadFileRes.data);
//调用接口存到服务器上
                                ……
&#125;
&#125;);
&#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里多说一句，如果你开发的是H5和微信小程序平台，app.vue页面里的生命周期里千万不要写任何跳转页面的方法，不然你在H5上测试上传成功之后就会自动跳转到首页！！如果app.vue页面必须有跳转到首页的方法，可以判断一下是不是H5的平台，不是H5平台再跳转！</p>
<h3 data-id="heading-3">四、picker下拉列表选择</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a28400b357e4f9a8e6b57b2780d8477~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我这里的样式在下拉框的右边还有一个省略号，但是之前写的时候点击省略号没有反应，所以下面代码加了样式避免了：</p>
<pre><code class="copyable"><view class="selectBox flex">
        <!--这里的样式设置是因为我有一张省略号的图片，因为点击这个图片也要可以出发下拉框-->
<picker mode="selector" :range="selectList" @change="changeSelect" style="width: 100%;position: relative;"><view class="inputBox">&#123;&#123;selectList[selectIdx]&#125;&#125;</view><image src="../../static/images/moreIcon3.png" @click="changeSelect" class="moreIcon3"></image>
</picker>
</view>

js:
data() &#123;
    return &#123;
        selectList:['请选择'],
        selectIdx: 0
    &#125;
&#125;,
methods: &#123;
    //选择下拉框
    changeSelect(e) &#123;
this.selectIdx= e.target.value;    &#125;
&#125;

css:
        .selectBox &#123;width: 88%;
height: 98rpx;
line-height: 98rpx;
margin: 80rpx 45rpx 45rpx 45rpx;
background: #F6F6F6;
border-radius: 49rpx;
&#125;
.inputBox &#123;
margin-left: 46rpx;
&#125;
.moreIcon3 &#123;
width: 66rpx;
height: 16rpx;
position: absolute;
right: 20px;
top: 43%;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">五、下拉刷新页面</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a14631853e1548aeb0f6b07bf33e4910~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在pages.json中配置页面的时候加参数enablePullDownRefresh，让这个页面可以有下拉刷新的事件</p>
<pre><code class="copyable">//mine页面代码：
onPullDownRefresh() &#123;
this.searchList();//下拉刷新查询接口
setTimeout(function () &#123;
uni.stopPullDownRefresh();//停止下拉刷新
&#125;, 1000);
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>今天写了一些常用的方法和开发页面中需要避免的坑，最近也是自己遇到的，写出来记录一下</p></div>  
</div>
            