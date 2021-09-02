# ZoomToDovetailTranscriber
Changes default Zoom transcript to import to Dovetail properly

Let's say you have a transcript file (`GMT20210824-140503_Recording.transcript.vtt`) from Zoom:
```
WEBVTT

1
00:00:04.440 --> 00:00:14.639
Andrew Nelson (he): Hello and welcome to my ted talk
```

You'd then run `python ZoomToDovetailTranscriber.py GMT20210824-140503_Recording.transcript.vtt` to get a new file (`GMT20210824-140503_Recording.transcript_fordovetail.vtt`) ready for upload to Dovetail:
```
WEBVTT

1
00:00:04.440 --> 00:00:14.639
<v Andrew Nelson (he)>Hello and welcome to my ted talk
```
