
---
title: '下载的文件打不开甚至中毒？教你几招Hash文件'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220704/S9798c79f-74b8-4c43-8d14-41729b056e7c.png'
author: 快科技（原驱动之家）
comments: false
date: Mon, 04 Jul 2022 10:22:53 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220704/S9798c79f-74b8-4c43-8d14-41729b056e7c.png'
---

<div>   
<p>很多朋友都有过下载了某个文件打不开，或者打开后根本不是那么回事的情况，有的朋友甚至下载某“官方系统”安装后却一堆病毒，这往往是由于下载的文件货不对板造成的。由于网络问题、CDN 缓存乃至钓鱼网站等原因，默认情况下真的很难判断下载回来的文件会不会货不对板。要解决这个问题，对文件进行 Hash 哈希校验，是非常有效的做法，但 Windows 默认似乎没有这功能选项。怎么办？今天就来分享几招！</p>
<p><strong>命令行</strong></p>
<p>其实说 Windows 默认没有 Hash 文件的功能，是不准确的，Windows 系统其实带有 Hash 文件功能，只不过并不直接在图形界面提供给用户，通过命令行就可以执行 Hash 命令。</p>
<p>首先，我们需要查询某个文件的具体路径，这个很简单，通过点击文件呼出右键菜单查看属性即可查询到。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220704/9798c79f-74b8-4c43-8d14-41729b056e7c.png" target="_blank"><img alt="下载的文件打不开甚至中毒？教你几招Hash文件" h="414" src="https://img1.mydrivers.com/img/20220704/S9798c79f-74b8-4c43-8d14-41729b056e7c.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>接着，运行 PowerShell，输入以下命令。</p>
<p>Get-FileHash <文件路径> -Algorithm <Hash算法>| Format-List其中，<文件路径> 填写文件所在的位置，而 < Hash 算法 > 则填写想要运算的 Hash 类型。Windows 默认支持 SHA1、SHA256、SHA384、SHA512、MACTripleDES、MD5、RIPEMD160 算法，不支持 CRC-32、CRC-64。</p>
<p>例如，有个文件叫“1.jpg”，存在于 C 盘的根目录，想要用 MD5 算法来校验，那么就应该输入以下命令。</p>
<p>Get-FileHash C:\1.jpg -Algorithm md5| Format-List之后，PowerShell 中就会给出 Hash 值了。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220704/2aee5d6b-f58e-4ad1-a3fa-1d0c53263241.png" target="_blank"><img alt="下载的文件打不开甚至中毒？教你几招Hash文件" h="319" src="https://img1.mydrivers.com/img/20220704/S2aee5d6b-f58e-4ad1-a3fa-1d0c53263241.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>7-Zip</strong></p>
<p>命令行虽然有用，但毕竟麻烦，有没有什么更简便的方法？其实可以尝试使用 7-Zip 这款压缩软件。</p>
<p>7-Zip：https://www.7-zip.org/</p>
<p>7-Zip 的大名相信很多人都听说过，这是目前世界上最流行的开源压缩软件之一，影响力巨大，很多压缩软件尤其是国产压缩软件，都使用了 7-Zip 的源代码。但鲜为人知的是，其实 7-Zip 除了能帮你压缩、解压文件，也提供了非常方便快捷的 Hash 文件功能。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220704/2c3bf6e5-a3a7-4f9c-8b46-8f669fb9eedc.png" target="_blank"><img alt="下载的文件打不开甚至中毒？教你几招Hash文件" h="404" src="https://img1.mydrivers.com/img/20220704/S2c3bf6e5-a3a7-4f9c-8b46-8f669fb9eedc.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>打开 7-Zip 的主界面，点击“工具”进入“选项”，即可看到多个选项卡。切换到“7-Zip”，勾选“添加 7-Zip 到右键菜单”，并勾选下面“CRC SHA”的选项，之后用右键点击文件，就可以看到 7-Zip 提供的 Hash 功能了。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220704/0823fd9b-9ac3-4f07-8c90-722d316a6518.jpg" target="_blank"><img alt="下载的文件打不开甚至中毒？教你几招Hash文件" h="403" src="https://img1.mydrivers.com/img/20220704/S0823fd9b-9ac3-4f07-8c90-722d316a6518.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>7-Zip 支持 CRC-32、CRC-64、SHA256、SHA1 以及 BLAKE2sp 等 Hash 算法，很好地弥补了 Windows 自带 Hash 算法的不足。可惜的是 7-Zip 没有提供非常常见的 MD5，如果需要 MD5 的 Hash，还得另寻他法。</p>
<p><strong>OpenHashTab</strong></p>
<p>7-Zip 虽好，但它本职始终是一个压缩软件。如果你需要更专业的解决方案，OpenHashTab 或许是更完美的选择。</p>
<p>OpenHashTab：https://github.com/namazso/OpenHashTab</p>
<p>OpenHashTab 是一款开源的、专注于提供 Hash 校验功能的小软件。它的体积小巧，支持中文，不存在什么使用门槛。</p>
<p>OpenHashTab 的使用很简单，下载后直接安装即可。之后，只要打开文件属性，就可以看到“哈希信息”的标签，里面罗列着文件的各种哈希值。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220704/44cd6e46-6098-4199-b677-942cc60aea4e.png" target="_blank"><img alt="下载的文件打不开甚至中毒？教你几招Hash文件" h="847" src="https://img1.mydrivers.com/img/20220704/S44cd6e46-6098-4199-b677-942cc60aea4e.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>OpenHashTab 的功能是专业且全面的。在支持的算法方面，OpenHashTab 支持以下 Hash 算法。</p>
<p>CRC32, CRC64 (xz) xxHash (XXH32, XXH64) xxHash3 (64 and 128 bit variants) MD4, MD5 RipeMD160 Blake2sp SHA-1 SHA-2 (SHA-224, SHA-256, SHA-384, SHA-512) SHA-3 (SHA3-224, SHA3-256, SHA3-384, SHA3-512) BLAKE3 (256 bit, 512 bit) KangarooTwelve (264 bit, 256 bit, 512 bit) ParallelHash128 (264 bit) and ParallelHash256 (528 bit) Streebog (GOST R 34.11-12) (256 bit, 512 bit)另外，OpenHashTab 还支持文件夹，也可以选择多个文件一同计算 Hash，双击计算出来的 Hash 值即可选择复制，还是非常方便的。</p>
<p>总的来说，如果你经常有计算文件 Hash 的需求，OpenHashTab 会是非常好的选择。</p>
<p><strong>总结</strong></p>
<p>担心下载的文件出差错，利用 Hash 对比的确是行之有效的方法。目前 Windows 默认的 Hash 功能并不算方便，希望上文的方法能够帮到大家！</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220704/b0badcd0cd19455fafc8f99649e8d71c.png" target="_blank"><img alt="下载的文件打不开甚至中毒？教你几招Hash文件" h="399" src="https://img1.mydrivers.com/img/20220704/s_b0badcd0cd19455fafc8f99649e8d71c.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
           <p class="end"><img src="https://icons.mydrivers.com/news/end_article.png" referrerpolicy="no-referrer"></p>
<div style="overflow: hidden;font-size:14px;">
             
          <p class="url"><span style="color:#666">责任编辑：随心</span><a href="javascript:;" class="jiucuo" id="leftjiucuo">文章纠错</a></p>
        </div>
        <div class="page_article" id="bnext">
 
</div>
<p class="bqian">话题标签：<a href="https://news.mydrivers.com/tag/wenjian.htm">文件</a><a href="https://news.mydrivers.com/tag/wenjianguanliqi.htm">文件管理器</a><a href="https://news.mydrivers.com/tag/xiazai.htm">下载</a>  </p>
        
</div>
            