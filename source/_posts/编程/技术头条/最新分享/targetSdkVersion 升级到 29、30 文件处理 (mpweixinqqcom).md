
---
title: 'targetSdkVersion 升级到 29、30 文件处理 (mp.weixin.qq.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=8083'
author: 技术头条
comments: false
date: 2021-06-21 02:01:56
thumbnail: 'https://picsum.photos/400/300?random=8083'
---

<div>   
在29版本后，只能操作本身内部存储私有目录、外部存储私有目录、共享存储，但是依然可以通过android:requestLegacyExternalStorage="true"来设置（在AndroidManifest.xml中的application添加该配置），不启用分区存储，一切照旧。
    
</div>
            