
---
title: '又被Steam吞存档了？教你构建自己的云存档！'
categories: 
 - 游戏
 - 小黑盒
 - 游戏新闻
headimg: 'https://imgheybox.max-c.com/web/2022/03/28/f8794cdafa2b6c8a5d8f3a87882b98ae/thumb.png'
author: 小黑盒
comments: false
date: Mon, 28 Mar 2022 17:30:44 GMT
thumbnail: 'https://imgheybox.max-c.com/web/2022/03/28/f8794cdafa2b6c8a5d8f3a87882b98ae/thumb.png'
---

<div>   
<p><img class="lazy" data-height="431" src="https://imgheybox.max-c.com/web/2022/03/28/f8794cdafa2b6c8a5d8f3a87882b98ae/thumb.png" data-width="984" referrerpolicy="no-referrer"></p><h4 class="img-desc">无法同步云存档</h4><p>Steam的云存档是一个非常实用的功能，可以让你在不同设备上保持游戏进度的同步，它会在你启动游戏时检测本地存档和云上存档的版本是否一致，并将最新的存档覆盖到本地。</p><p>但是由于网络等原因，经常出现无法同步的情况，或者同步下来的是旧存档，反而覆盖了自己刚玩过的新的存档。</p><p>Steam本身有通过客服系统获取云存档列表的功能，只不过访问起来体验极差，腿腿在挂着梯子的情况下都没能把存档拯救回来。</p><p>下面介绍种自己实现云存档的方法，腿腿自己一直也在用这种方法，缺点是需要自己配置，但是同步的效果和速度比Steam要强上不少，有需要的盒友可以试一试。</p><h2>1. 同步软件</h2><p>现在市面上可以实现云备份功能的软件都可以，微软的OneDrive，百度云，坚果云，WPS云等等。各有优劣，但是原理是一样的，腿腿在用的是OneDrive，单纯是比较干净，速度和空间大小都比不上其他几家。</p><p><img class="lazy" data-height="621" src="https://imgheybox.max-c.com/web/2022/03/28/8da1b8e0369c1547328e41617830422f/thumb.jpeg" data-width="1120" referrerpolicy="no-referrer"></p><h4 class="img-desc">OneDrive</h4><p>这里以OneDrive为例，正好是微软自带的功能，大部分PC也都预装的这个东西，就省的再去下载了（一不小心就是个全家桶）。</p><p><img class="lazy" data-height="802" src="https://imgheybox.max-c.com/web/2022/03/28/7be40f4337bb9833fbf5fcef0699d177/thumb.png" data-width="452" referrerpolicy="no-referrer"></p><h4 class="img-desc">OneDrive界面</h4><p>OneDrive由于只有云备份的功能，所以整体比较简约，基本功能扫一眼就能看个大概，登录微软账号就可以看到主界面了，我们去设置里面稍微开启几个选项，就可以启动我们的云存档功能了。</p><h2>2. 云存档实现</h2><p>备份的方式有两种，一种是直接备份整个“文档”文件夹，这种不是很推荐，因为两台电脑安装的软件游戏未必一样，全部都同步的话，一是空间捉紧，也有可能出现不明的错误，而且也不是所有游戏的存档都在文档下呀。方法就是在选择同步的文件夹时勾选文档，这里还可以勾选桌面和照片，这里就不再赘述了，总之是不推荐这种方式就是了。</p><p><img class="lazy" data-height="699" src="https://imgheybox.max-c.com/web/2022/03/28/290e6c1d5e5939240320b3143dc5b7dc/thumb.png" data-width="741" referrerpolicy="no-referrer"></p><h4 class="img-desc">看看就行，不推荐备份整个文档</h4><p>第二种就是按照游戏逐一同步，每个游戏都需要设置一下，不过搞定一次，终身受用就是了，而且备份到的目录是自己定的，就可以避免某些游戏同步时会把画面设置也同步到云上的问题。这里着重讲解下这种方式：</p><h3>第一步 在OneDrive下创建Saved Games文件夹</h3><p>主要是为了集中管理，文件夹名可以自己定，但是一定不要有中文。</p><h3>第二步 将存档剪切到Saved Games文件夹下</h3><p><img class="lazy" data-height="345" src="https://imgheybox.max-c.com/web/2022/03/28/cdbc7daa59142a8d6411fecec4911242/thumb.png" data-width="586" referrerpolicy="no-referrer"></p><h4 class="img-desc">游戏存档位置</h4><p>找到游戏存档的位置，剪切到OndeDrice的Saved Games目录下，如上图中就需要把God of War文件夹整个移过去。这时候存档的位置是空的。</p><h3>第三步 创建文件关联</h3><p>简单说就是在游戏存档的位置创建一个快捷方式直接链接到OneDrive目录（只是方便理解，并不是真的创建快捷方式）。</p><p>以管理员权限运行CMD，输入：</p><p>mklink /d "游戏存档位置" “对应到Ond Drive的位置”</p><p>以上图为例就是</p><p>mklink /d "C:\Users\Nite\Saved Games\God of War" "C:\Users\Nite\OneDrive\Saved Games\God of War"</p><p>然后回车就可以了。</p><p>注意这时候游戏存档是空的，链接后OneDrive上面的文件夹会以快捷方式的样子存在于游戏的存档目录下。</p><p><img class="lazy" data-height="639" src="https://imgheybox.max-c.com/web/2022/03/28/a319ab588583cca5d5ec2aa52724b327/thumb.png" data-width="1223" referrerpolicy="no-referrer"></p><h4 class="img-desc">关联存档位置</h4><p>在第二台电脑进行相同的操作，云存档功能就可以实现了。</p><p>这种方式的优点一是比较稳定，不会出现丢档或者无法同步的问题，二是速度比较快，开机后会自动同步不同的数据，而不是像Steam一样在游戏启动的时候才去同步存档。</p><p>有需要的盒友可以试一下。</p>  
</div>
            