
---
title: 'DDR5内存到底升级了什么？'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1117/6b0ef0fb5b86031.jpg'
author: cnBeta
comments: false
date: Wed, 17 Nov 2021 03:25:50 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1117/6b0ef0fb5b86031.jpg'
---

<div>   
<strong>随着11月初各大主板厂商Z690系列主板的发售，家用电脑上的内存终于进入了DDR5的时代。那么DDR5相比过去的DDR4都有哪些变化呢？以及现在值得买吗？</strong>外观方面，DDR5和DDR4的区别主要有两方面。第一，在内存条中间的部分多了一些电子模块。第二，内存条下部的防呆口位置发生了改变。<br>
 <p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/1117/6b0ef0fb5b86031.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">来源：<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://kingston.jd.com/" target="_blank">金士顿</a></p><p>防呆口位置发生改变也就意味着DDR5的内存条与DDR4的内存条物理上不兼容。现在老主板上的内存插槽一般都是DDR4或者DDR3的，如果你想升级DDR5的内存条就必须换新主板。</p><p>关于新主板方面，目前发售的主板中只有Intel的Z690平台系列主板支持DDR5的内存条。需要注意的是，不是所有Z690主板都支持DDR5内存条。Z690平台的CPU内部有两种内存控制器，DDR4和DDR5都有。但因为DDR5和DDR4物理上不兼容，所以具体主板能使用哪种内存要看主板厂商的设计。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/1117/33b8d4a62a28b1b.png" referrerpolicy="no-referrer"></p><p>以<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://msi-pc.jd.com/" target="_blank">微星</a>为例，一般主板型号后缀中有“DDR4”字样的，就说明该型号主板上的内存槽是DDR4的，如果你买DDR5内存条是插不进去的。所以想要体验DDR5内存的小伙伴，在购买主板之前一定要看清楚主板支持的内存类型。</p><p><strong>新加入的电子模块</strong></p><p>在说完了关于“防呆口”的问题之后，咱们该聊聊DDR5多出来的那部分“电子模块”了。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/1117/d02f9225e66dc66.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">来源：瑞萨电子</p><p>多出来的“电子模块”可以分成两个部分，SPD Hub（SPD集线器）和PMIC（电源管理模块）。</p><p>其中SPD Hub主要带来的是关于I3C总线方面的升级，I3C的12.5MHz速率大幅超越当前和传统解决方案（例如I2C 1MHz速率）。而电源管理模块则是把原来位于主板上的内存供电模块转移到了内存条上。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/1117/5a628200efedbea.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">来源：十铨科技</p><p>对于喜欢给内存条超频的小伙伴可能会了解，DDR4的标准工作电压为1.2V，如果超频的话电压会增加，但一般也不会超过1.5V。而电脑电源给主板的直接供电一般就3.3V、5V、12V这几个档位，没有内存所需的1.2V。因此在DDR4的时代，主板在接受电源供电之后需要通过电源管理模块把电源降低到1.2V供给内存条使用，这也是电源模块的主要作用。而在DDR5的时代，这个模块被转移到了内存条上。对于一般的电脑来说，主板只需要给内存条一个5V供电（此处对于一般PC电脑是5V，服务器电脑是12V）就可以了，之后的电压转换可以由内存条自己完成。</p><p>这样做的结果就是：</p><p>内存条成本增加（毕竟多了一个模块）主板成本非常轻微的降低（毕竟电源模块对整个主板来说值不了几个钱）内存获得的供电更加精准</p><p><strong>其它亮点和说明</strong></p><p>速度性能更高，DDR5初代速度为4800MHz，超过了大多数DDR4内存条，而且随着DDR5内存条的发展，日后还会推出更快的内存条。容量更大，根据目前相关厂商的宣传，DDR5内存条的单条容量应该会达到64GB甚至128GB。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/1117/49232b380217024.png" referrerpolicy="no-referrer"></p><p>“自带双通道”，有一些软件在识别DDR5内存的时候会把原单条单通道的内存识别为双通道内存，原双条双通道的内存识别为四通道内存。但这种叫法其实是不准确的，这种“四通道”和类似X299平台上的四通道技术原理和性能表现是不一样的。DDR5实际上是把64位的数据带宽分成两个 32 位可寻址通道（并不是增加带宽，而是切分），这样就可以提高内存控制器数据访问的效率并减少延迟。低能耗，这其实算是内存厂商的宣传点，对普通用户的实际影响不大。用1.1V的DDR5功耗肯定是比用1.2V的DDR4要低的，但是内存条的能耗对于整个电脑来说是非常小的一部分，通常也就几瓦。电脑的能耗大头主要集中的CPU、显卡甚至显示器上。所以如果想靠DDR5提高电脑续航能力或者省电，还不如去降低一下显示器亮度。片内 ECC，通俗来说就是一种纠错功能，可以提高可靠性。</p><p><strong>结语</strong></p><p>对于大多数小伙伴来说目前的DDR5其实不建议购买，理由如下：</p><p>目前的DDR5内存条还不是一个“满血”的状态，正如上文所提，DDR5在频率、容量等各个方面都还有提高空间。之后各大厂商还会推出更快更强的DDR5内存条。Z690平台的Intel十二代CPU目前还是带着两套内存控制器，这样虽然可以兼容老内存条，让主板厂商造出可以使用DDR4内存的主板。但是这在一定程度上会限制内存的性能。当CPU完全甩掉旧的内存控制器之后，DDR5的性能表现应该会更好。贵，整个与DDR5配套的硬件目前的售价还是比较高的。</p>   
</div>
            