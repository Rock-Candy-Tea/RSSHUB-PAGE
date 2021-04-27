
---
title: 'QuickSDK1.0 发布，开源微云百度云 SDK'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8907'
author: 开源中国
comments: false
date: Tue, 27 Apr 2021 13:53:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8907'
---

<div>   
<div class="content">
                                                                    
                                                        <div> 
 <h1>QuickSDk</h1> 
 <p>QuickSDK是一个开源的SDK包.目前支持以下功能:</p> 
 <h2>微云</h2> 
 <ul> 
  <li>获取用户可用容量和总空间大小</li> 
  <li>获取微云文件夹信息</li> 
  <li>创建文件夹</li> 
  <li>删除文件夹</li> 
  <li>下载微云文件</li> 
  <li>解析微云分享链接</li> 
  <li>保存微云分享链接</li> 
  <li>分享微云文件</li> 
  <li>为分享微云文件设置密码</li> 
  <li>获取回收站文件列表</li> 
  <li>清空回收站 ......</li> 
 </ul> 
 <h2>百度云</h2> 
 <ul> 
  <li>获取用户空间容量信息</li> 
  <li>解析百度云分享链接</li> 
  <li>解析带密码的百度云分享链接</li> 
  <li>下载分享链接</li> 
  <li>保存分享链接</li> 
  <li>获取百度云文件列表</li> 
  <li>创建文件夹</li> 
  <li>删除文件夹</li> 
  <li>私密分享百度云文件</li> 
  <li>公开分享百度云文件</li> 
  <li>取消分享百度云文件</li> 
  <li>重命名文件</li> 
  <li>删除文件</li> 
  <li>查看回收站文件</li> 
  <li>清空回收站 ......</li> 
 </ul> 
 <p>QuickSDK需要用户手动设置微云Cookie或者百度云Cookie后才可使用.</p> 
 <h2>快速入门</h2> 
 <p> </p> 
 <p>maven引入</p> 
 <p> </p> 
 <p>```</p> 
 <pre><span style="color:null"><dependency></span>
<span style="color:null"><span style="background-color:null">    <groupId>cn.schoolwow</groupId></span>
<span style="background-color:null">    <artifactId>QuickSDK</artifactId></span>
<span style="background-color:null">    <version>1.0</version></span>
<span style="background-color:null"></dependency></span></span></pre> 
 <p>```</p> 
 <pre>WeiYunAPI weiYunAPI = new WeiYunAPIImpl();</pre> 
 <div> 
  <div> 
   <div> 
    <div> 
     <div> 
      <div> 
       <div> 
        <pre>weiYunAPI.setCookie("&#123;weiyun.com域名下的所有Cookie信息&#125;");</pre> 
        <pre>weiYunAPI.xxx();//调用相关方法</pre> 
        <pre>​</pre> 
        <pre>BaiDuYunAPI baiDuYunAPI = new BaiDuYunAPIImpl();</pre> 
        <pre>baiDuYunAPI.setCookie("&#123;baidu.com域名下所有Cookie信息&#125;");</pre> 
        <pre>baiDuYunAPI.xxx();//调用相关方法</pre> 
       </div> 
      </div> 
     </div> 
    </div> 
   </div> 
   <div>
     
   </div> 
   <div>
    由于百度云和微云的API可能随时变化,本框架并不能保证随时可用.
   </div> 
  </div> 
 </div> 
 <h1>免责声明</h1> 
 <p>本框架仅用于技术交流,请勿使用本框架用于非法目的.因使用者使用不当造成的一切后果与本人无关.</p> 
 <p> </p> 
 <p><span style="background-color:#ffffff; color:#333333">QuickSDK仓库地址: </span><a href="https://gitee.com/648823596/quick-sdk">https://gitee.com/648823596/quick-sdk</a></p> 
</div>
                                        </div>
                                      
</div>
            