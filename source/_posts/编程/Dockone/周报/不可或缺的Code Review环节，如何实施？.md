
---
title: '不可或缺的Code Review环节，如何实施？'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210608/2caf76dea0536dc0b6dfc11c7c373f30.gif'
author: Dockone
comments: false
date: 2021-06-10 03:24:22
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210608/2caf76dea0536dc0b6dfc11c7c373f30.gif'
---

<div>   
<br>众所周知，Code Review是开发过程中一个非常重要的环节，但是很多公司或者团队是没有这一环节的，今天笔者结合自己所在团队，浅谈Code Review的价值及如何实施。<br>
<h3>Code Review的价值</h3>许多团队没有Code Review环节，或者因为追求项目快速上线，认为CR浪费时间；或者团队成员缺少CR观念，认为CR的价值并不大。所以想要推动CR在团队中的实施，最最重要的一点便是增强团队成员对CR环节的认同感。<br>
<br>Code Review环节，它更加依赖于团队成员的主观能动性，只有团队成员对其认可，他们才会积极地参入这一环节，CR的价值才能最大化的体现。如果团队成员不认可CR，即使强制设置了CR流程，也是形同虚设，反而可能阻碍正常开发流程的效率。那么如何让团队成员认可CR环节呢，自然是让他们意识到CR的价值，然后就会……真香！<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210608/2caf76dea0536dc0b6dfc11c7c373f30.gif" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210608/2caf76dea0536dc0b6dfc11c7c373f30.gif" class="img-polaroid" title="1.gif" alt="1.gif" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>提升团队代码质量</h4>随着团队规模的扩大和项目的迭代升级，团队之间的信息透明度会越来越低，项目的可维护性也会越来越差，可能引发如下一系列问题：<br>
<ol><li>已有的utils方法，重复造轮子</li><li>代码过于复杂，缺少必要注释，后人难以维护</li><li>目录结构五花八门，杂乱不堪</li><li>……  </li></ol><br>
<br>合理的CR环节，可以有效地把控每次提交的代码质量，不至于让项目的可维护性随着版本迭代和时间推移变得太差，这也是CR的首要目的。<strong>CR环节并不会降低开发效率</strong>，就一次代码提交来说，也许部分人认为CR可能花费了时间，但是有效的CR给后人扩展和维护时所节省的时间是远超于此的。<br>
<h4>团队技术交流</h4>Reviewer和Reviewee，在参与CR的过程中，都是可以收获到许多知识，进行技术交流的。<br>
<ol><li>有利于帮助新人快速成长，团队有新人加入时（如实习生和校招生），往往需要以为导师带领一段时间，通过CR环节，可以使导师最直接的了解到新人开发过程中所遇到的问题，作出相应的指导。</li><li>通过CR环节，团队成员可以了解他人的业务，而不局限于自己的所负责的业务范围。项目发现问题时，可以迅速定位到相关业务的负责人进行修改。同时若有的团队成员离职后，也可以减少业务一人负责所带来的后期维护困难。</li><li>学习他人的优秀代码。通过CR环节，可以迅速接触到团队成员在项目中解决某些问题的优秀代码，或者使用的一些你所未接触过的一些api等。</li></ol><br>
<br><h4>保证项目的统一规范</h4>既然要进行CR，首先要对项目的规范制定要求，包括编码风格规范、目录结构规范、业务规范等等。一方面，统一的项目规范才能保证项目的代码质量，提高项目的质量和可维护性；另一方面，在大家熟悉了统一的规范后，能够提升CR的效率，节省时间。<br>
<h3>Code Review的实践</h3>关于Code Review的实践，要考虑的包括CR所花费的时间、CR的形式、何时进行CR等等。<br>
<h4>预留CR的时间</h4>首先不得不承认，CR环节是要耗费一定时间的，所以在项目排期中，不仅要考虑开发、联调、提测、改bug等时间，还要预留出CR的时间。包括担任Reviewer和Reviewee角色的时间都要考虑。<br>
<br>另外如果遇到的需求比较复杂，为了避免因为CR过程导致代码需要大量修改，最好提前和团队成员沟通好需求的设计和结果思路。<br>
<h4>CR的形式</h4>我所见过的CR大多有两种形式。一种是设立一个特定时间，例如每周或者每半月等等，团队成员一起对之前的Merge Request进行CR；另一种是对每次的Merge Request都进行CR。<br>
<br>我个人更偏向于后者。第一种定期CR，Merge Request的数量太多，不太可能对所有的MR进行CR，如果CR之后再对之前的诸多MR进行修改成本太大；而且一次性太多的CR会打击团队成员的积极性。第二种MR相对就轻松的多，可以考虑轮班每天设置2-3人对当天的MR进行CR即可。<br>
<h4>CR的时机</h4>CR的环节应该设立在提测环节之前。因为CR后如果优化代码虽然理论上只是代码优化，但很可能会对业务逻辑产生影响，如果在提测时候，那么可能会影响到已经测试过的功能点。<br>
<br>当然也要分情况，如果遇到比较紧急的需求或者bug修复，那么也可以先提测，后续再做相应的CR。<br>
<h3>对团队成员要求</h3>前面已经提到，要增强团队成员对CR环节的认同感。作为CR环节的参与者，还应该根据自己的团队特点，对团队成员做出相应要求，可以参考我们团队。<br>
<h4>Reviewer</h4><ul><li><br>指明review的级别。reviewer再给相应的代码添加评论时，建议指明评论的级别，可以在评论前用[]作出标识，例如：  <br>
<ul><li>[request]xxxxxxx　　　　　　　此条评论的代码必须修改才能予以通过</li><li>[advise]xxxxxxxx　　　　　　　此条评论的代码建议修改，但不修改也可以通过</li><li>[question]xxxxxx　　　　　　　此条评论的代码有疑问，需reviewee进一步解释</li></ul></li><li><br>讲明该评论的原因。在对代码做出评论时，应当解释清楚原因，如果自己有现成的更好地解决思路，应该把相应的解决思路也评论上，节省reviewee的修改时间。</li><li>平等友善的评论。评论者在review的过程中，目的是提升项目代码质量，而不是抨击别人，质疑别人的能力，应该保持平等友善的语气。</li><li>享受Code Review。只有积极的参与CR，把CR作为一种享受，才能将CR的价值最大化的体现。</li></ul><br>
<br><h4>Reviewee</h4><ol><li>注重注释。对于复杂代码写明相应注释，在进行commit时也应简明的写清楚背景，帮助reviewer理解，提高review的效率。</li><li>保持乐观的心态接受别人的review。团队成员的review不是对你的批判，而是帮助你的提升，所以要尊重别人的review，如果review你感觉不正确，可以在下面提出疑问，进一步解释。</li><li>完成相应review的修改应当在下面及时进行回复，保持信息同步。</li></ol><br>
<br>原文链接：<a href="https://juejin.cn/post/6882333635203039239" rel="nofollow" target="_blank">https://juejin.cn/post/6882333635203039239</a>，作者：梨香
                                                                <div class="aw-upload-img-list">
                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                            </ul>
                                                              
</div>
            