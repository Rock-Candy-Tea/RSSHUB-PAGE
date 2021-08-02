
---
title: 'uniapp 安卓app 非媒体文件上传下载'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3985'
author: 掘金
comments: false
date: Fri, 30 Jul 2021 20:06:46 GMT
thumbnail: 'https://picsum.photos/400/300?random=3985'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>记一次，uniapp 安卓app非媒体文件上传下载的学习记录</p>
<h3 data-id="heading-0">上传</h3>
<p>首先要解决安卓app文件上传问题，就要考虑app中文件的选取和上传问题。因为uniapp input不支持type=file，所以就要使用原生的文件路径选取api 以及uniapp的文件上传api。</p>
<p>文件的话选取由于本人对安卓原生不熟悉，所以首先考虑插件市场的文件选取组件 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fext.dcloud.net.cn%2Fplugin%3Fid%3D117" target="_blank" rel="nofollow noopener noreferrer" title="https://ext.dcloud.net.cn/plugin?id=117" ref="nofollow noopener noreferrer">tki-file-manager</a> 详细信息点击连接查看，这里只是搬运一下实例以方便阅读。然后上传到服务器使用uniapp 官方api <a href="https://link.juejin.cn/?target=https%3A%2F%2Funiapp.dcloud.io%2FuniCloud%2Fstorage%3Fid%3Duploadfile" target="_blank" rel="nofollow noopener noreferrer" title="https://uniapp.dcloud.io/uniCloud/storage?id=uploadfile" ref="nofollow noopener noreferrer">uni.uploadFile</a> 方法。</p>
<pre><code class="copyable"><template>
    <view class="content">
        <button type="primary" @tap="openFile">打开文件选择器</button>
        <view>文件路径为:</view>
        <view class="path">&#123;&#123;path&#125;&#125;</view>
        <tki-file-manager ref="filemanager" @result="resultPath"></tki-file-manager>
    </view>
</template>

<script>
import tkiFileManager from "@/components/tki-file-manager/tki-file-manager.vue"
export default &#123;
    data() &#123;
        return &#123;
            title: '',
            baseUrl: '',
            path: ''      
        &#125;
    &#125;,
    methods: &#123;
        openFile()&#123;
            this.$refs.filemanager._openFile()
        &#125;,
        // 
        resultPath(path)&#123;
            this.path = path
            this.sendFile()         
        &#125;,
        // 将文件上到服务器
sendFile() &#123;    
            uni.uploadFile(&#123;
                url: baseUrl,
filePath: this.path,
                name: 'file',header: &#123;
     'Authorization': uni.getStorageSync('lifeData').vuex_token
&#125;,
success: (uploadFileRes) => &#123;
     console.log(uploadFileRes.data.id);
&#125;
    &#125;);
&#125;,
    &#125;,
    components: &#123;
        tkiFileManager
    &#125;
&#125;
</script>
<style>
    .content &#123;
        width: 100%;
        overflow: hidden;
    &#125;
    .path&#123;
        font-size: 14px;
        word-break:break-all;
    &#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">下载</h3>
<p>由于app环境中无Blob对象 下载的话这里在网上找到的使用到原生的api plus.downloader.createDownload 进行文件保存的方法。</p>
<pre><code class="copyable">// 下载请求
async downloadFileFn(id) &#123;
// #ifdef APP-PLUS
let res = await downloadFile(&#123; id: id &#125;);// 封装的按id获取文件接口的 方法
let path = res.data.path;
console.log(path);
let url = path;
let name = this.file.name;
// var name = 'fileName.docx'; //文件名称可以在上传时进行保存，下载时取出，当文件名称中存在单双引号时，要做好处理，否则会报错
var dtask = plus.downloader.createDownload(
url,
&#123;
filename: '_downloads/' + name //利用保存路径，实现下载文件的重命名
&#125;,
function(d, status) &#123;
var fileSaveUrl = plus.io.convertLocalFileSystemURL(d.filename);
plus.runtime.openFile(d.filename); //选择软件打开文件
&#125;
);
dtask.start();
// #endif
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>只是一种思路，网上文件上传还有一种是使用安卓原生webview 进行内嵌网页进行上传，但是就要考虑内嵌网页和app内部的通信问题，因时间有限暂没有研究这种方法。</p>
<p>最后，上面的文章有许多是在网上找到的一些解决方法进行一些拼凑，本文也只是一次记录，不喜勿喷。</p></div>  
</div>
            