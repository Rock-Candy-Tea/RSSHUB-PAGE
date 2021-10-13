
---
title: 'iOS App 背着我们干了啥？手动分析iOS 15 App活动记录'
categories: 
 - 新媒体
 - 少数派 sspai
 - Matrix
headimg: 'https://raw.fastgit.org/womeimingzi11/self-image/main//202110112311828.jpeg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
author: 少数派 sspai
comments: false
date: Tue, 12 Oct 2021 08:15:41 GMT
thumbnail: 'https://raw.fastgit.org/womeimingzi11/self-image/main//202110112311828.jpeg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
---

<div>   
<div class="articleWidth-content" data-v-6a669db8><div class="content wangEditor-txt minHeight" data-v-6a669db8><p>最近随着 iOS 15 中「记录 App 活动」功能的加入，以微信为代表的一类软件频繁读写用户信息的行为被抓了现形。具体的新闻可以阅读 <a href="https://www.zhihu.com/question/491251960/answer/2162795183">Hackl0us 发布在知乎的记录</a>.</p><p>虽然微信在 10 月 11 日发布了新版似乎修复了这个问题，然而美团针对每 5 分钟获取一次用户定位的行为发布了公告：</p><blockquote><p>美团 App 技术工程师就此前美团 APP ”频繁定位“回应：之所以出现这种情况，是因为这类软件在单方面读取系统操作日志后，进行了选择性展示，经测试，在相关权限开启且 App 后台仍处于活跃状态时，大部分主流 App 均会被该软件检测出频繁读取用户信息，且监测结果高度相似。</p><p>该工程师还表示，并未对上述读取 iOS 15 系统日志的软件进行安全性和保密性测试，建议大家谨慎下载。</p></blockquote><p>hmmm，怎么说呢，就无话可说吧，既然有可能是这类检测软件的问题，那么我就排除软件的障碍，自己手动检测试试看。</p><p>首先在 iOS 15 设备进入「设置」-「隐私」–「记录 App 活动」，打开 App 活动开关，等待一定时间，iOS 会自动记录期间所有 App 活动，点击存储 App 活动即可导出为 <code>ndjson</code> 文件——声明：本操作系 <strong>iOS 自主记录日志</strong>，且用户绝对有权力<strong>单方面</strong>导出，此操作不涉及也没有办法<strong>选择性</strong>导出，更<strong>不具备展示</strong>功能。</p><figure class="image ss-img-wrapper"><img src="https://raw.fastgit.org/womeimingzi11/self-image/main//202110112311828.jpeg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt data-original="https://raw.fastgit.org/womeimingzi11/self-image/main//202110112311828.jpeg" referrerpolicy="no-referrer"></figure><p>这里的 <code>ndjson</code> 大致相当于一种流式 json 文件，可以通过 <code>ndjson</code> 包读取为 data.table 并转换为 tibble。</p><h2>读取与预览</h2><p>首先是读取 ndjson 文件，并预览</p><blockquote><p>声明：下列读取 iOS 15 系统日志的操作并未进行安全性和保密性测试，建议大家谨慎操作，或者拔掉网线并开启电磁屏蔽操作（摊手。</p></blockquote><pre class="language-"><code>library("ndjson")
library("pillar")
library("dplyr")</code></pre><pre class="language-"><code>## 
## Attaching package: 'dplyr'</code></pre><pre class="language-"><code>## The following object is masked from 'package:pillar':
## 
##     dim_desc</code></pre><p> </p><pre class="language-"><code>## The following objects are masked from 'package:stats':
## 
##     filter, lag</code></pre><p> </p><pre class="language-"><code>## The following objects are masked from 'package:base':
## 
##     intersect, setdiff, setequal, union</code></pre><p> </p><pre class="language-"><code>library("lubridate")</code></pre><p> </p><pre class="language-"><code>## 
## Attaching package: 'lubridate'</code></pre><p> </p><pre class="language-"><code>## The following objects are masked from 'package:base':
## 
##     date, intersect, setdiff, union</code></pre><p> </p><pre class="language-"><code>app_privacy_report_tb <-
  ndjson::stream_in("resource/App_Privacy_Report_v4_2021-10-11T22_36_54.ndjson",
                    cls = "tbl")

glimpse(app_privacy_report_tb)</code></pre><p> </p><pre class="language-"><code>## Rows: 19,687
## Columns: 15
## $ accessor.identifier     <chr> "com.xiaomi.mihome", "com.xiaomi.mihome", "com…
## $ accessor.identifierType <chr> "bundleID", "bundleID", "bundleID", "bundleID"…
## $ category                <chr> "location", "location", "location", "location"…
## $ identifier              <chr> "60E8004B-D969-4ABB-B83F-460663BCC29F", "60E80…
## $ kind                    <chr> "intervalBegin", "intervalEnd", "intervalBegin…
## $ timeStamp               <chr> "2021-10-08T13:30:43.340+08:00", "2021-10-08T1…
## $ type                    <chr> "access", "access", "access", "access", "acces…
## $ bundleID                <chr> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
## $ context                 <chr> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
## $ domain                  <chr> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
## $ domainOwner             <chr> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
## $ domainType              <dbl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
## $ firstTimeStamp          <chr> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
## $ hits                    <dbl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…
## $ initiatedType           <chr> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA…</code></pre><p> </p><pre class="language-"><code>head(app_privacy_report_tb)</code></pre><p> </p><pre class="language-"><code>## # A tibble: 6 × 15
##   accessor.identif… accessor.identif… category identifier  kind  timeStamp type 
##   <chr>             <chr>             <chr>    <chr>       <chr> <chr>     <chr>
## 1 com.xiaomi.mihome bundleID          location 60E8004B-D… inte… 2021-10-… acce…
## 2 com.xiaomi.mihome bundleID          location 60E8004B-D… inte… 2021-10-… acce…
## 3 com.xiaomi.mihome bundleID          location 865B785C-D… inte… 2021-10-… acce…
## 4 com.xiaomi.mihome bundleID          location 865B785C-D… inte… 2021-10-… acce…
## 5 com.xiaomi.mihome bundleID          location 7626338D-D… inte… 2021-10-… acce…
## 6 com.xiaomi.mihome bundleID          location 7626338D-D… inte… 2021-10-… acce…
## # … with 8 more variables: bundleID <chr>, context <chr>, domain <chr>,
## #   domainOwner <chr>, domainType <dbl>, firstTimeStamp <chr>, hits <dbl>,
## #   initiatedType <chr></code></pre><p>三天记录下所有 App 总共有 19687 条隐私请求，不过由于记录是成对出现的，即开始请求——请求结束，所以说请求次数只有一半9843.5呃，怎么说呢，就还挺勤劳的吧。</p><p>我们首先关注 accessor.identifier (App ID), category (访问分类), kind（时间戳类型）,timeStamp (时间戳), type (大类) 这几列，选择上述列并设置为合适的数据类型。</p><pre class="language-"><code>main_tb <-
app_privacy_report_tb %>% 
  select(accessor.identifier, category, kind, type, timeStamp) %>% 
  mutate(
    `accessor.identifier` = as.factor(accessor.identifier),
    category = as.factor(category),
    kind = as.factor(kind),
    type = as.factor(type),
    timeStamp = ymd_hms(timeStamp)
  )

head(main_tb)</code></pre><p> </p><pre class="language-"><code>## # A tibble: 6 × 5
##   accessor.identifier category kind          type   timeStamp          
##   <fct>               <fct>    <fct>         <fct>  <dttm>             
## 1 com.xiaomi.mihome   location intervalBegin access 2021-10-08 05:30:43
## 2 com.xiaomi.mihome   location intervalEnd   access 2021-10-08 05:34:21
## 3 com.xiaomi.mihome   location intervalBegin access 2021-10-08 05:34:24
## 4 com.xiaomi.mihome   location intervalEnd   access 2021-10-08 05:34:53
## 5 com.xiaomi.mihome   location intervalBegin access 2021-10-08 05:34:58
## 6 com.xiaomi.mihome   location intervalEnd   access 2021-10-08 05:35:08</code></pre><p> </p><pre class="language-"><code>skimr::skim(main_tb)</code></pre><p>(#tab:tb_select_type_convert)Data summary<br>| Name | main_tb |<br>| Number of rows | 19687 |<br>| Number of columns | 5 |<br>| _______________________ | |<br>| Column type frequency: | |<br>| factor | 4 |<br>| POSIXct | 1 |<br>| ________________________ | |<br>| Group variables | None |</p><p><strong>Variable type: factor</strong></p><figure class="table"><table><thead><tr><th>skim_variable</th><th>n_missing</th><th>complete_rate</th><th>ordered</th><th>n_unique</th><th>top_counts</th></tr></thead><tbody><tr><td>accessor.identifier</td><td>9121</td><td>0.54</td><td>FALSE</td><td>26</td><td>com: 9062, com: 236, com: 228, com: 176</td></tr><tr><td>category</td><td>9121</td><td>0.54</td><td>FALSE</td><td>4</td><td>loc: 9940, con: 290, pho: 288, cam: 48</td></tr><tr><td>kind</td><td>9121</td><td>0.54</td><td>FALSE</td><td>2</td><td>int: 5283, int: 5283</td></tr><tr><td>type</td><td>0</td><td>1.00</td><td>FALSE</td><td>2</td><td>acc: 10566, net: 9121</td></tr></tbody></table></figure><p><strong>Variable type: POSIXct</strong></p><figure class="table"><table><thead><tr><th>skim_variable</th><th>n_missing</th><th>complete_rate</th><th>min</th><th>max</th><th>median</th><th>n_unique</th></tr></thead><tbody><tr><td>timeStamp</td><td>0</td><td>1</td><td>2021-10-08 05:30:41</td><td>2021-10-11 14:36:29</td><td>2021-10-09 02:33:52</td><td>19671</td></tr></tbody></table></figure><p>在这三天里面，总共有 26 款 App 请求了我的隐私数据（共安装 130 款 App），那么平均下来一款 App 就请求了 378.5961538 次，然而这怎么可能嘛！必然是有更勤劳的小蜜蜂。</p><figure class="image ss-img-wrapper"><img src="https://raw.fastgit.org/womeimingzi11/self-image/main//202110112333078.jpeg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt data-original="https://raw.fastgit.org/womeimingzi11/self-image/main//202110112333078.jpeg" referrerpolicy="no-referrer"></figure><h2>数据可视化</h2><pre class="language-"><code>library(forcats)
library(ggplot2)

main_tb %>%
  group_by(accessor.identifier) %>% 
  count() %>% 
  ungroup() %>% 
  mutate(
    accessor.identifier = fct_reorder(accessor.identifier, n)
  ) %>% 
  ggplot(aes(
    x = accessor.identifier,
    y = n
  )) +
  geom_col() +
  coord_flip()</code></pre><p> </p><figure class="image ss-img-wrapper"><img src="https://d33wubrfki0l68.cloudfront.net/02af4f97182b616e830bf8f5dd1b5d5c4a929403/2b461/post/2021-10-12-what-you-did-app/index.zh-hans_files/figure-html/request_count-1.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt data-original="https://d33wubrfki0l68.cloudfront.net/02af4f97182b616e830bf8f5dd1b5d5c4a929403/2b461/post/2021-10-12-what-you-did-app/index.zh-hans_files/figure-html/request_count-1.png" referrerpolicy="no-referrer"></figure><p>简单的排序后发现三个有趣的点：</p><ol><li>在 accessor.identifier 中 com.dianping （美团点评）并不是非常显眼，这可能是因为我已经关闭了大众点评和美团等 App 的后台定位权限相关；</li><li>com.xiaomi.mihome 这位小老弟还是挺疯狂，盲猜是因为我开启了它的后台定位所致，然而我并没有开启地理围栏等相关智能化脚本，这个稍后再看；</li><li>NA 太多了，也就是说并非所有的操作都有 accessor.identifier？后续再看。</li></ol><p>根据 main_tb 的预览， 与 App 身份认证相关的列还有 accessor.identifierType 以及 identifier</p><pre class="language-"><code>app_privacy_report_tb %>% 
  select(accessor.identifier, 
         accessor.identifierType) %>% 
  mutate(across(everything(), as.factor)) %>%
  unique() %>% 
  print(., n = nrow(.))</code></pre><p> </p><p> </p><pre class="language-"><code>## # A tibble: 27 × 2
##    accessor.identifier               accessor.identifierType
##    <fct>                             <fct>                  
##  1 com.xiaomi.mihome                 bundleID               
##  2 com.TickTick.task                 bundleID               
##  3 com.autonavi.amap                 bundleID               
##  4 io.robbie.HomeAssistant           bundleID               
##  5 com.google.photos                 bundleID               
##  6 com.cainiao.cnwireless            bundleID               
##  7 com.taobao.taobao4iphone          bundleID               
##  8 com.lifubing.lbs.stepOfLife       bundleID               
##  9 com.tencent.xin                   bundleID               
## 10 ph.telegra.Telegraph              bundleID               
## 11 com.taobao.fleamarket             bundleID               
## 12 com.readdle.smartemail            bundleID               
## 13 com.tencent.tim                   bundleID               
## 14 com.360buy.jdmobile               bundleID               
## 15 com.xiaomi.mishop                 bundleID               
## 16 com.alipay.iphoneclient           bundleID               
## 17 com.wdk.hmxs                      bundleID               
## 18 com.xiaomi.miwatch.pro            bundleID               
## 19 com.heweather.weatherapp          bundleID               
## 20 tv.danmaku.bilianime              bundleID               
## 21 com.atebits.Tweetie2              bundleID               
## 22 com.dianping.dpscope              bundleID               
## 23 com.johnil.vvebo                  bundleID               
## 24 com.tmri.12123                    bundleID               
## 25 cn.mucang.ios.jiakaobaodianhuoche bundleID               
## 26 com.readdle.Scanner               bundleID               
## 27 <NA>                              <NA></code></pre><h2>数据整形与预览</h2><p>还是存在 <code>NA</code>，后面发现除通过 accessor.identifier 标记的是除网络访问之外的记录，bundleID 列是记录的 App 的网络链接请求，那就对数据帧变形。</p><pre class="language-"><code>library(tidyr)
app_privacy_report_meld_tb <-
  app_privacy_report_tb %>% 
  pivot_longer(cols = c(accessor.identifier, bundleID),
               names_to = "id_type", 
               values_to = "app_id"
               ) %>% 
  filter(!is.na(app_id)) %>%
  select(-id_type) %>% 
  select(app_id, everything())

meld_tb <-
app_privacy_report_meld_tb %>% 
  select(app_id, category, kind, type, timeStamp) %>% 
  mutate(
    app_id = as.factor(app_id),
    category = as.factor(category),
    kind = as.factor(kind),
    type = as.factor(type),
    timeStamp = ymd_hms(timeStamp)
  )

head(meld_tb)</code></pre><p> </p><pre class="language-"><code>## # A tibble: 6 × 5
##   app_id            category kind          type   timeStamp          
##   <fct>             <fct>    <fct>         <fct>  <dttm>             
## 1 com.xiaomi.mihome location intervalBegin access 2021-10-08 05:30:43
## 2 com.xiaomi.mihome location intervalEnd   access 2021-10-08 05:34:21
## 3 com.xiaomi.mihome location intervalBegin access 2021-10-08 05:34:24
## 4 com.xiaomi.mihome location intervalEnd   access 2021-10-08 05:34:53
## 5 com.xiaomi.mihome location intervalBegin access 2021-10-08 05:34:58
## 6 com.xiaomi.mihome location intervalEnd   access 2021-10-08 05:35:08</code></pre><p> </p><pre class="language-"><code>skimr::skim(meld_tb)</code></pre><p>(#tab:accesor_n_bundle)Data summary<br>| Name | meld_tb |<br>| Number of rows | 19687 |<br>| Number of columns | 5 |<br>| _______________________ | |<br>| Column type frequency: | |<br>| factor | 4 |<br>| POSIXct | 1 |<br>| ________________________ | |<br>| Group variables | None |</p><p><strong>Variable type: factor</strong></p><figure class="table"><table><thead><tr><th>skim_variable</th><th>n_missing</th><th>complete_rate</th><th>ordered</th><th>n_unique</th><th>top_counts</th></tr></thead><tbody><tr><td>app_id</td><td>0</td><td>1.00</td><td>FALSE</td><td>85</td><td>com: 9159, com: 4140, com: 2518, com: 429</td></tr><tr><td>category</td><td>9121</td><td>0.54</td><td>FALSE</td><td>4</td><td>loc: 9940, con: 290, pho: 288, cam: 48</td></tr><tr><td>kind</td><td>9121</td><td>0.54</td><td>FALSE</td><td>2</td><td>int: 5283, int: 5283</td></tr><tr><td>type</td><td>0</td><td>1.00</td><td>FALSE</td><td>2</td><td>acc: 10566, net: 9121</td></tr></tbody></table></figure><p><strong>Variable type: POSIXct</strong></p><figure class="table"><table><thead><tr><th>skim_variable</th><th>n_missing</th><th>complete_rate</th><th>min</th><th>max</th><th>median</th><th>n_unique</th></tr></thead><tbody><tr><td>timeStamp</td><td>0</td><td>1</td><td>2021-10-08 05:30:41</td><td>2021-10-11 14:36:29</td><td>2021-10-09 02:33:52</td><td>19671</td></tr></tbody></table></figure><p>经过整形的数据再看，发现总共有 85 款 App 请求了隐私数据，那么平均下来一款 App 就请求了 115.8058824 次。</p><h2>第二次数据可视化</h2><p>在 App Privacy Report 中，type 大类分为了两种 access, networkActivity, 对于 access 分类，在 category 中又有子分类 location, photos, contacts, camera。为了方便可视化，我们首先对这个部分进行更进一步整形，将网络请求补充到 category 中，然后进行可视化。</p><pre class="language-"><code>cat_to_type_tb <-
  meld_tb %>%
  mutate(
    # unfactor columns to avoid level missing
    category = as.character(category),
    type = as.character(type)) %>%
  mutate(
    # Do not use `ifelse`,
    # it does not support vectorization operation
    category = if_else(is.na(category),
                       type,
                       category)) %>%
  mutate(
    category = as.factor(category),
    type = as.factor(type)
  )

app_n_count_tb <-  
cat_to_type_tb %>% 
  group_by(app_id) %>%
  mutate(count = n()) %>%
  ungroup() %>%
  mutate(
    app_id = fct_reorder(app_id, count)
  )

app_n_count_tb %>%
  ggplot(aes(
    x = app_id,
    y = count
  )) +
  geom_col(aes(fill = type)) +
  coord_flip()</code></pre><p> </p><figure class="image ss-img-wrapper"><img src="https://d33wubrfki0l68.cloudfront.net/0126c9a2e32c06c27e56db4b4ea434ac13e7a51f/fec62/post/2021-10-12-what-you-did-app/index.zh-hans_files/figure-html/re_data_viz_by_cat-1.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt data-original="https://d33wubrfki0l68.cloudfront.net/0126c9a2e32c06c27e56db4b4ea434ac13e7a51f/fec62/post/2021-10-12-what-you-did-app/index.zh-hans_files/figure-html/re_data_viz_by_cat-1.png" referrerpolicy="no-referrer"></figure><pre class="language-"><code>app_n_count_tb %>%
  ggplot(aes(
    x = app_id,
    y = count
  )) +
  geom_col(aes(fill = category)) +
  coord_flip()</code></pre><p> </p><figure class="image ss-img-wrapper"><img src="https://d33wubrfki0l68.cloudfront.net/68ba05726c8760398b8ed8d3d3456dcc299361ee/0a097/post/2021-10-12-what-you-did-app/index.zh-hans_files/figure-html/re_data_viz_by_cat-2.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt data-original="https://d33wubrfki0l68.cloudfront.net/68ba05726c8760398b8ed8d3d3456dcc299361ee/0a097/post/2021-10-12-what-you-did-app/index.zh-hans_files/figure-html/re_data_viz_by_cat-2.png" referrerpolicy="no-referrer"></figure><p>由于 App 数量太多，而且 Bundle ID 还存在 com.apple.corelocation.CoreLocationVanilaWhenInUseAuthPromptPlugin 这种龙傲天般的命名，上面两张图的视觉效果还有很大优化空间，然而这已经足够确定一个问题了：米家 App 靠实力诠释了一骑绝尘是什么。且根据第二站图，可以发现米家似乎绝大多数请求都用在 location 定位上。</p><pre class="language-"><code>library(showtext)</code></pre><p> </p><pre class="language-"><code>## Loading required package: sysfonts</code></pre><p> </p><pre class="language-"><code>## Loading required package: showtextdb</code></pre><p> </p><pre class="language-"><code>showtext::showtext_auto()
cat_to_type_tb %>% 
  filter(app_id == "com.xiaomi.mihome") %>% 
  group_by(category) %>% 
  count() %>% 
  ggplot(aes(x = "", y = n, fill = category)) +
  geom_bar(stat = "identity", width = 1, color="white") +
  coord_polar("y", start = 0) +
  theme_void() +
  labs(title = "米家权限请求分布")</code></pre><p> </p><figure class="image ss-img-wrapper"><img src="https://d33wubrfki0l68.cloudfront.net/187c8b556a93099bbb96a2ed12dfd4b6020a8268/d9cbc/post/2021-10-12-what-you-did-app/index.zh-hans_files/figure-html/mijia_tile-1.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt data-original="https://d33wubrfki0l68.cloudfront.net/187c8b556a93099bbb96a2ed12dfd4b6020a8268/d9cbc/post/2021-10-12-what-you-did-app/index.zh-hans_files/figure-html/mijia_tile-1.png" referrerpolicy="no-referrer"></figure><pre class="language-"><code>mj_time_begin_end_tb <-
cat_to_type_tb %>% 
  filter(app_id == "com.xiaomi.mihome") %>% 
  filter(category == "location") %>% 
  select(kind, timeStamp) %>% 
  # 此处实现很奇怪，应该可以用 pivot_wider 一步到位的
  pivot_wider(
    names_from = kind,
    values_from = timeStamp
    )</code></pre><p> </p><pre class="language-"><code>## Warning: Values are not uniquely identified; output will contain list-cols.
## * Use `values_fn = list` to suppress this warning.
## * Use `values_fn = length` to identify where the duplicates arise
## * Use `values_fn = &#123;summary_fun&#125;` to summarise duplicates</code></pre><p> </p><pre class="language-"><code>mj_time_tb <-
  tibble(
    begin = mj_time_begin_end_tb$intervalEnd[[1]],
    duration = mj_time_begin_end_tb$intervalEnd[[1]] - mj_time_begin_end_tb$intervalBegin[[1]]
  )

skimr::skim(mj_time_tb)</code></pre><p>(#tab:mijia_tile)Data summary<br>| Name | mj_time_tb |<br>| Number of rows | 4531 |<br>| Number of columns | 2 |<br>| _______________________ | |<br>| Column type frequency: | |<br>| difftime | 1 |<br>| POSIXct | 1 |<br>| ________________________ | |<br>| Group variables | None |</p><p><strong>Variable type: difftime</strong></p><figure class="table"><table><thead><tr><th>skim_variable</th><th>n_missing</th><th>complete_rate</th><th>min</th><th>max</th><th>median</th><th>n_unique</th></tr></thead><tbody><tr><td>duration</td><td>0</td><td>1</td><td>10.01 secs</td><td>1129.66 secs</td><td>10.19 secs</td><td>2052</td></tr></tbody></table></figure><p><strong>Variable type: POSIXct</strong></p><figure class="table"><table><thead><tr><th>skim_variable</th><th>n_missing</th><th>complete_rate</th><th>min</th><th>max</th><th>median</th><th>n_unique</th></tr></thead><tbody><tr><td>begin</td><td>0</td><td>1</td><td>2021-10-08 05:34:21</td><td>2021-10-10 12:06:44</td><td>2021-10-08 21:26:44</td><td>4531</td></tr><tr><td>mj_time_tb %>%</td><td> </td><td> </td><td> </td><td> </td><td> </td><td> </td></tr><tr><td>mutate(</td><td> </td><td> </td><td> </td><td> </td><td> </td><td> </td></tr></tbody></table></figure><pre class="language-"><code>hour_of_day =
  hour(begin)</code></pre><p>) %>%<br>group_by(hour_of_day) %>%<br>count() %>%<br>ggplot(<br>aes(x = hour_of_day,<br>y = n)<br>) +<br>geom_line() +<br>scale_x_continuous(name = "时间", limits = c(0,24), expand = c(0,0)) +<br>scale_y_continuous(name = "请求次数") +<br>theme_linedraw()</p><p>```</p><figure class="image ss-img-wrapper"><img src="https://d33wubrfki0l68.cloudfront.net/c1383a8afc1cfbc1bcc08f72eafe7ec698e49518/1db52/post/2021-10-12-what-you-did-app/index.zh-hans_files/figure-html/mijia_tile-2.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt data-original="https://d33wubrfki0l68.cloudfront.net/c1383a8afc1cfbc1bcc08f72eafe7ec698e49518/1db52/post/2021-10-12-what-you-did-app/index.zh-hans_files/figure-html/mijia_tile-2.png" referrerpolicy="no-referrer"></figure><p>总的来说，米家主要请求的因素数据就是定位，并且是夜以继日的工作，可以说是007了。只有在凌晨才舍得勉强克制一点。再结合 iOS 电池选项里面米家出色的耗电量，应该没有冤枉。</p><figure class="image ss-img-wrapper"><img src="https://raw.fastgit.org/womeimingzi11/self-image/main//202110121513402.jpeg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt data-original="https://raw.fastgit.org/womeimingzi11/self-image/main//202110121513402.jpeg" referrerpolicy="no-referrer"></figure><p>关键是笔者米家中需要用到定位的自动化并没有开启（因为从来就没有按照预期正常工作过），所以勤劳的定位请求真的让人头大。</p><figure class="image ss-img-wrapper"><img src="https://raw.fastgit.org/womeimingzi11/self-image/main//202110121515654.jpeg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt data-original="https://raw.fastgit.org/womeimingzi11/self-image/main//202110121515654.jpeg" referrerpolicy="no-referrer"></figure><p>目前笔者的解决办法是关闭 App 的始终定位功能，只能从根源上解决问题，关键是对于使用影响非常有限（依赖地理围栏功能的小伙伴慎重考虑）</p><figure class="image ss-img-wrapper"><img src="https://raw.fastgit.org/womeimingzi11/self-image/main//202110121517781.jpeg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt data-original="https://raw.fastgit.org/womeimingzi11/self-image/main//202110121517781.jpeg" referrerpolicy="no-referrer"></figure><h2>总结</h2><p>总的来说，根据使用 R 分析 App_Privacy_Report 报告，笔者并未发现美团与微信的频繁访问，不过这并不能说明它们没有问题，因为我已经关掉了此二者的后台刷新以及始终定位功能，使得他两个没有办法实现频繁唤醒；不过让人意外的是，无意中发现了潜在的耗电大户，还是希望能克制一点。</p><p>声明：本文采用 R 语言是为境外团队 R-Core Team 开发软件；ndjson 包是境外冰岛开发者开发；tidyverse bundle 是新西兰开发者牵头开发；下列读取 iOS 15 系统日志的操作并未进行安全性和保密性测试，建议大家谨慎操作，或者拔掉网线并开启电磁屏蔽操作；不过写作的人是境内人员（战术后仰</p><p>米家版本为v6.11.201-build6.11.201.2</p><p> </p></div><!----></div><div style="border:1px solid transparent;" data-v-6a669db8></div><div class="article-side sideTop" style="display:none;left:0;" data-v-7be936cf data-v-6a669db8><div class="download-guide-container" data-v-14f9065e data-v-7be936cf><div class="btn-wrapper" data-v-14f9065e><!----><button class="btn btn-view" data-v-14f9065e><i class="iconfont iconfont-phone" data-v-14f9065e></i></button></div><a href="https://sspai.com/s/JYjP" target="_blank" data-v-14f9065e><!----></a></div><div class="item-wrapper" data-v-7be936cf><button class="btn btn-charge" data-v-7be936cf><i class="iconfont" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>9</span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-comment" data-v-7be936cf><i class="iconfont iconfont-comment" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>4</span></div><div class="item-wrapper" data-v-7be936cf><span data-v-7be936cf><div role="tooltip" id="el-popover-5773" aria-hidden="true" class="el-popover el-popper popper-share right ss-popper-dark-border" style="width:undefinedpx;display:none;"><!----><div class="article-side-share-btn"><a href="https://service.weibo.com/share/share.php?url=null?ref=weibo&title=%E3%80%90iOS%20App%20%E8%83%8C%E7%9D%80%E6%88%91%E4%BB%AC%E5%B9%B2%E4%BA%86%E5%95%A5%EF%BC%9F%E6%89%8B%E5%8A%A8%E5%88%86%E6%9E%90iOS%2015%20App%E6%B4%BB%E5%8A%A8%E8%AE%B0%E5%BD%95%E3%80%91%E6%9C%80%E8%BF%91%E9%9A%8F%E7%9D%80iOS15%E4%B8%AD%E3%80%8C%E8%AE%B0%E5%BD%95App%E6%B4%BB%E5%8A%A8%E3%80%8D%E5%8A%9F%E8%83%BD%E7%9A%84%E5%8A%A0%E5%85%A5%EF%BC%8C%E4%BB%A5%E5%BE%AE%E4%BF%A1%E4%B8%BA%E4%BB%A3%E8%A1%A8%E7%9A%84%E4%B8%80%E7%B1%BB%E8%BD%AF%E4%BB%B6%E9%A2%91%E7%B9%81%E8%AF%BB%E5%86%99%E7%94%A8%E6%88%B7%E4%BF%A1%E6%81%AF%E7%9A%84%E8%A1%8C%E4%B8%BA%E8%A2%AB%E6%8A%93%E4%BA%86%E7%8E%B0%E5%BD%A2%E3%80%82%E5%85%B7%E4%BD%93%E7%9A%84%E6%96%B0%E9%97%BB%E5%8F%AF%E4%BB%A5%E9%98%85%E8%AF%BB%5BHackl0u%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&pic=&appkey=3196502474#" target="_blank"><i class="iconfont iconfont-weibo-simple right-16"></i></a><span><div role="tooltip" id="el-popover-978" aria-hidden="true" class="el-popover el-popper" style="width:undefinedpx;display:none;"><!----><div style="text-align:center;"><div id="qr-code"></div><small class="qr-small">扫码分享</small></div></div><span class="el-popover__reference-wrapper"><i class="iconfont iconfont-wechat-simple right-16"></i></span></span><a href="https://twitter.com/share?text=%E3%80%90iOS%20App%20%E8%83%8C%E7%9D%80%E6%88%91%E4%BB%AC%E5%B9%B2%E4%BA%86%E5%95%A5%EF%BC%9F%E6%89%8B%E5%8A%A8%E5%88%86%E6%9E%90iOS%2015%20App%E6%B4%BB%E5%8A%A8%E8%AE%B0%E5%BD%95%E3%80%91%E6%9C%80%E8%BF%91%E9%9A%8F%E7%9D%80iOS15%E4%B8%AD%E3%80%8C%E8%AE%B0%E5%BD%95App%E6%B4%BB%E5%8A%A8%E3%80%8D%E5%8A%9F%E8%83%BD%E7%9A%84%E5%8A%A0%E5%85%A5%EF%BC%8C%E4%BB%A5%E5%BE%AE%E4%BF%A1%E4%B8%BA%E4%BB%A3%E8%A1%A8%E7%9A%84%E4%B8%80%E7%B1%BB%E8%BD%AF%E4%BB%B6%E9%A2%91%E7%B9%81%E8%AF%BB%E5%86%99%E7%94%A8%E6%88%B7%E4%BF%A1%E6%81%AF%E7%9A%84%E8%A1%8C%E4%B8%BA%E8%A2%AB%E6%8A%93%E4%BA%86%E7%8E%B0%E5%BD%A2%E3%80%82%E5%85%B7%E4%BD%93%E7%9A%84%E6%96%B0%E9%97%BB%E5%8F%AF%E4%BB%A5%E9%98%85%E8%AF%BB%5BHackl0u%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&url=null" target="_blank" class="twitter"><i class="iconfont iconfont-twitter-simple right-16"></i></a></div></div><span class="el-popover__reference-wrapper"><button class="btn-mini btn-share" data-v-7be936cf><i class="iconfont iconfont-share" data-v-7be936cf></i></button></span></span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-collect" data-v-7be936cf><i class="iconfont iconfont-collect" data-v-7be936cf></i></button></div><!----></div><!---->  
</div>
            