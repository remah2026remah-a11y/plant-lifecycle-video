# دورة حياة النبات

## Overview
- **Topic**: دورة حياة النبات من البذرة إلى بذور جديدة.
- **Hook**: كيف تتحول بذرة صغيرة إلى نبات قادر على إنتاج جيل جديد؟
- **Target Audience**: أطفال وطلاب المرحلة الابتدائية.
- **Estimated Length**: 93.28 ثانية.
- **Key Insight**: الحياة النباتية دورة مستمرة: بذرة، إنبات، نمو، إزهار، ثم بذور جديدة.

## Narrative Arc
نبدأ ببذرة ساكنة في التربة، ثم نتابع خروج الجذر والساق، ونرى كيف تصنع الأوراق غذاء النبات حتى يصل إلى الإزهار. في النهاية تتكون بذور جديدة تعيد الدورة من البداية.

## Audio Sync
- `/home/ubuntu/plant_lifecycle/audio/scene1.wav` — 21.44s
- `/home/ubuntu/plant_lifecycle/audio/scene2.wav` — 18.96s
- `/home/ubuntu/plant_lifecycle/audio/scene3.wav` — 24.84s
- `/home/ubuntu/plant_lifecycle/audio/scene4.wav` — 28.04s

## Scenes
### Scene 1: البذرة تستعد
**Duration**: 21.44 seconds
**Purpose**: تقديم البذرة وعوامل بدء الدورة.
**Visuals**: تربة، بذرة، قطرات ماء، شمس، سهم بدء.

### Scene 2: الإنبات
**Duration**: 18.96 seconds
**Purpose**: إظهار الجذر إلى الأسفل والساق إلى الأعلى.
**Visuals**: مقطع تربة، جذر، ساق وبرعم، أسهم اتجاه.

### Scene 3: النمو والبناء الضوئي
**Duration**: 24.84 seconds
**Purpose**: إظهار الأوراق وصناعة الغذاء بضوء الشمس.
**Visuals**: نبات أخضر، شمس، أسهم ماء وثاني أكسيد الكربون، فقاعة غذاء.

### Scene 4: الإزهار وعودة الدورة
**Duration**: 28.04 seconds
**Purpose**: إظهار الزهرة والتلقيح والثمرة والبذور الجديدة.
**Visuals**: زهرة، حبوب لقاح، ثمرة، بذور، حلقة دورة.

## Color Palette
- Background: `#071A2B`
- Soil: `#6B4423`
- Green: `#4ADE80`
- Yellow: `#FACC15`
- Blue: `#60A5FA`
- Pink: `#F472B6`

## Technical Notes
- Framework: Manim Community Edition.
- No external raster assets or plugins.
- Arabic labels use Pango `Text`.
- Total animation duration must match narration within 1 second.

## Implementation Order
1. Render each scene at low quality.
2. Extract representative frames and inspect layout.
3. Finalize at 1080p60.
4. Concatenate audio and mux Arabic subtitles.
