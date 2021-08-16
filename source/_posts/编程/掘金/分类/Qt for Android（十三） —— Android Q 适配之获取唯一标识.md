
---
title: 'Qt for Android（十三） —— Android Q 适配之获取唯一标识'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8143'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 18:01:46 GMT
thumbnail: 'https://picsum.photos/400/300?random=8143'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第13天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h4 data-id="heading-0">背景</h4>
<p>  我们产品之前的唯一标识是通过<code>android.os.Build.SERIAL</code>或者Build.getSerial() 获取，但是在Android 10之后这个方法会返回unknow或者空。因此在Android 10 之后此方法便不可行了。</p>
<p>在Android P之后，Android系统的安全和数据更加隐私，所以通过 <code>getMacAddress()</code>方法
获取的无线mac地址会被随机化。但是我们的产品是运行在瑞星微板卡上的LCD广告机应用，是有有线网口的。有线的网口mac地址肯定不会变化了，因此我们的方案是获取etho的mac地址（etho代表以太网，wlan0代表了无线网卡）。</p>
<h4 data-id="heading-1">代码</h4>
<pre><code class="copyable"> public String getSerialNumber() &#123;
        String serial = "";
        System.out.println("getSerialNumber Begin\n");
        try &#123;
             if (Build.VERSION.SDK_INT < Build.VERSION_CODES.N) &#123;//8.0-
                serial = execCmd("getprop ro.boot.serialno");
                System.out.println("getprop.serialno:" + serial+"\n");
            &#125;else&#123;
                 serial = getMacEth0();
            &#125;
        &#125; catch (Exception e) &#123;
            e.printStackTrace();
        &#125;
   if(TextUtils.isEmpty(serial))
        &#123;
            serial = getAndroidID();
        &#125;
        System.out.println("getSerialNumber end"+"\n");
        return serial;
    &#125;


 private String getMacEth0() &#123;
        try &#123;
            //获取本机器所有的网络接口,找以太网卡
            Enumeration enumeration = NetworkInterface.getNetworkInterfaces();
            while (enumeration.hasMoreElements()) &#123;
                NetworkInterface networkInterface = (NetworkInterface)enumeration.nextElement();
                //获取硬件地址，一般是MAC
                byte[] arrayOfByte = networkInterface.getHardwareAddress();
                if (arrayOfByte == null || arrayOfByte.length == 0) &#123;
                           continue;
                &#125;
                
                StringBuilder stringBuilder = new StringBuilder();
                for (byte b : arrayOfByte) &#123;
                    //格式化为：两位十六进制加冒号的格式，若是不足两位，补0
                    stringBuilder.append(String.format("%02X:", new Object[] &#123; Byte.valueOf(b) &#125;));
                &#125;
                if (stringBuilder.length() > 0) &#123;
                    //删除后面多余的冒号
                    stringBuilder.deleteCharAt(stringBuilder.length() - 1);
                &#125; String str = stringBuilder.toString();
                // wlan0:无线网卡 eth0：以太网卡
                if (networkInterface.getName().equals("eth0")) &#123;
                    return str;
                &#125;
            &#125;
        &#125; catch (SocketException socketException) &#123;
            return "";
        &#125;
        return "";
    &#125;
    

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">        private String getAndroidID()
    &#123;
        String m_szAndroidID = Settings.Secure.getString(getApplicationContext().getContentResolver(),
                Settings.Secure.ANDROID_ID);
        return m_szAndroidID;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码给出了两种方案，1是使用了优化的获取mac地址的方式。
二是使用ANDROID_ID。但是AndroidID有个缺点，root、刷机或恢复出厂设置都会导致设备的ANDROID_ID发生改变，因此如果没有此类场景的话，其实建议用ANDROID_ID，方便可靠。</p>
<p>如果你没有有线网口，那请参考下面的文章获取唯一标识：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2Fe8b6cafa91d5" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/e8b6cafa91d5" ref="nofollow noopener noreferrer">Android 10获取设备标识方案探究</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhujiang.blog.csdn.net%2Farticle%2Fdetails%2F102500462%3Futm_medium%3Ddistribute.pc_relevant_t0.none-task-blog-2%257Edefault%257EBlogCommendFromMachineLearnPai2%257Edefault-1.control%26depth_1-utm_source%3Ddistribute.pc_relevant_t0.none-task-blog-2%257Edefault%257EBlogCommendFromMachineLearnPai2%257Edefault-1.control" target="_blank" rel="nofollow noopener noreferrer" title="https://zhujiang.blog.csdn.net/article/details/102500462?utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control" ref="nofollow noopener noreferrer">Android Q（安卓10）获取唯一ID(最优解)</a></p></div>  
</div>
            