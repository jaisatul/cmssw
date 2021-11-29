import FWCore.ParameterSet.Config as cms

#Example version list of MEs to save with singel Luminosity Granularity
#in the nanoDQMIO reduced version of DQMIO data Tier
#It needs process.DQMStore.saveByLumi = cms.untracked.bool(True)
#to make effect in the MEs saved by DQMStore
#DQMIO with per Lumisection data, are a special kind of DQM files 
#containing almost the full set of DQM Monitor Elements (MEs) saved 
#with single lumisection time granularity. 
#Saying "almost" we refer to the fact that only Monitor Elements 
#produced in DQM Step1 are saved, 
#while those produced in the Harvesting step are not, 
#even if they could be obtained with some ad-hoc harvesting on Step1 data
#Hence, DQM Step2 (HARVESTING DQM) should not follow when saveByLumi is True
#since most DQM Harvesting modules expect perRun output
#https://twiki.cern.ch/twiki/bin/view/CMS/PerLsDQMIO

nanoDQMIO_perLSoutput = cms.PSet(
      MEsToSave = cms.untracked.vstring(*( #Using tuple to avoid python limit of 255 arguments
                                           #as suggested in:
                #https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePoolInputSources#Example_3_More_than_255_input_fi

                #Examples:
                #'Muons/MuonRecoAnalyzer/',               #Folder and its subfolders
                #'Muons/MuonIdDQM/GlobalMuons/hDT1Pullx'  #particular ME
            
              #Version 0.1 for nanoDQMIO in CMSSW_12_1_0 ReReco of Pilot Test Runs taken in Autumn 2021
              
 #ECAL            
 'EcalBarrel/EBOccupancyTask/EBOT digi occupancy',
 'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE -',
 'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE +',

 #Muon POG
 'Muons/MuonRecoAnalyzer/',               
 'Muons/MuonIdDQM/GlobalMuons/',
            
 #Tracker/Tracking
 #2D (PixelPhase1) histograms:
'PixelPhase1/Phase1_MechanicalView/PXBarrel/clusterposition_zphi_PXLayer_1',
'PixelPhase1/Phase1_MechanicalView/PXBarrel/clusterposition_zphi_PXLayer_2',
'PixelPhase1/Phase1_MechanicalView/PXBarrel/clusterposition_zphi_PXLayer_3',
'PixelPhase1/Phase1_MechanicalView/PXBarrel/clusterposition_zphi_PXLayer_4',
'PixelPhase1/Phase1_MechanicalView/PXForward/clusterposition_xy_PXDisk_+1',
'PixelPhase1/Phase1_MechanicalView/PXForward/clusterposition_xy_PXDisk_+2',
'PixelPhase1/Phase1_MechanicalView/PXForward/clusterposition_xy_PXDisk_+3',
'PixelPhase1/Phase1_MechanicalView/PXForward/clusterposition_xy_PXDisk_-1',
'PixelPhase1/Phase1_MechanicalView/PXForward/clusterposition_xy_PXDisk_-2',
'PixelPhase1/Phase1_MechanicalView/PXForward/clusterposition_xy_PXDisk_-3',
'PixelPhase1/Phase1_MechanicalView/PXBarrel/clusters_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_1',
'PixelPhase1/Phase1_MechanicalView/PXBarrel/clusters_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_2',
'PixelPhase1/Phase1_MechanicalView/PXBarrel/clusters_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_3',
'PixelPhase1/Phase1_MechanicalView/PXBarrel/clusters_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_4',
'PixelPhase1/Phase1_MechanicalView/PXBarrel/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_1',
'PixelPhase1/Phase1_MechanicalView/PXBarrel/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_2',
'PixelPhase1/Phase1_MechanicalView/PXBarrel/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_3',
'PixelPhase1/Phase1_MechanicalView/PXBarrel/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_4',
'PixelPhase1/Phase1_MechanicalView/PXForward/clusters_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_1',
'PixelPhase1/Phase1_MechanicalView/PXForward/clusters_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_2',
'PixelPhase1/Phase1_MechanicalView/PXForward/digi_occupancy_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_1',
'PixelPhase1/Phase1_MechanicalView/PXForward/digi_occupancy_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_2',
'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_1',
'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_2',
'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_3',
'PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_4',
'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+1',
'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+2',
'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+3',
'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-1',
'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-2',
'PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-3',

#1D (PixelPhase1) histograms:
'PixelPhase1/Phase1_MechanicalView/PXBarrel/charge_PXLayer_1',
'PixelPhase1/Phase1_MechanicalView/PXBarrel/charge_PXLayer_2',
'PixelPhase1/Phase1_MechanicalView/PXBarrel/charge_PXLayer_3',
'PixelPhase1/Phase1_MechanicalView/PXBarrel/charge_PXLayer_4',
'PixelPhase1/Phase1_MechanicalView/PXBarrel/size_PXLayer_1',
'PixelPhase1/Phase1_MechanicalView/PXBarrel/size_PXLayer_2',
'PixelPhase1/Phase1_MechanicalView/PXBarrel/size_PXLayer_3',
'PixelPhase1/Phase1_MechanicalView/PXBarrel/size_PXLayer_4',
'PixelPhase1/Phase1_MechanicalView/PXForward/charge_PXDisk_-1',
'PixelPhase1/Phase1_MechanicalView/PXForward/charge_PXDisk_-2',
'PixelPhase1/Phase1_MechanicalView/PXForward/charge_PXDisk_-3',
'PixelPhase1/Phase1_MechanicalView/PXForward/charge_PXDisk_+1',
'PixelPhase1/Phase1_MechanicalView/PXForward/charge_PXDisk_+2',
'PixelPhase1/Phase1_MechanicalView/PXForward/charge_PXDisk_+3',
'PixelPhase1/Phase1_MechanicalView/PXForward/size_PXDisk_-1',
'PixelPhase1/Phase1_MechanicalView/PXForward/size_PXDisk_-2',
'PixelPhase1/Phase1_MechanicalView/PXForward/size_PXDisk_-3',
'PixelPhase1/Phase1_MechanicalView/PXForward/size_PXDisk_+1',
'PixelPhase1/Phase1_MechanicalView/PXForward/size_PXDisk_+2',
'PixelPhase1/Phase1_MechanicalView/PXForward/size_PXDisk_+3',
'PixelPhase1/Tracks/num_clusters_ontrack_PXBarrel',
'PixelPhase1/Tracks/num_clusters_ontrack_PXForward',
'PixelPhase1/Tracks/PXBarrel/adc_PXLayer_1',
'PixelPhase1/Tracks/PXBarrel/adc_PXLayer_2',
'PixelPhase1/Tracks/PXBarrel/adc_PXLayer_3',
'PixelPhase1/Tracks/PXBarrel/adc_PXLayer_4',
'PixelPhase1/Tracks/PXBarrel/chargeInner_PXLayer_1',
'PixelPhase1/Tracks/PXBarrel/chargeInner_PXLayer_2',
'PixelPhase1/Tracks/PXBarrel/chargeInner_PXLayer_3',
'PixelPhase1/Tracks/PXBarrel/chargeInner_PXLayer_4',
'PixelPhase1/Tracks/PXBarrel/chargeOuter_PXLayer_1',
'PixelPhase1/Tracks/PXBarrel/chargeOuter_PXLayer_2',
'PixelPhase1/Tracks/PXBarrel/chargeOuter_PXLayer_3',
'PixelPhase1/Tracks/PXBarrel/chargeOuter_PXLayer_4',
'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_1',
'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_2',
'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_3',
'PixelPhase1/Tracks/PXBarrel/charge_PXLayer_4',
'PixelPhase1/Tracks/PXBarrel/size_PXLayer_1',
'PixelPhase1/Tracks/PXBarrel/size_PXLayer_2',
'PixelPhase1/Tracks/PXBarrel/size_PXLayer_3',
'PixelPhase1/Tracks/PXBarrel/size_PXLayer_4',
'PixelPhase1/Tracks/PXForward/adc_PXDisk_+1',
'PixelPhase1/Tracks/PXForward/adc_PXDisk_+2',
'PixelPhase1/Tracks/PXForward/adc_PXDisk_+3',
'PixelPhase1/Tracks/PXForward/adc_PXDisk_-1',
'PixelPhase1/Tracks/PXForward/adc_PXDisk_-2',
'PixelPhase1/Tracks/PXForward/adc_PXDisk_-3',
'PixelPhase1/Tracks/PXForward/charge_PXDisk_-1',
'PixelPhase1/Tracks/PXForward/charge_PXDisk_-2',
'PixelPhase1/Tracks/PXForward/charge_PXDisk_-3',
'PixelPhase1/Tracks/PXForward/charge_PXDisk_+1',
'PixelPhase1/Tracks/PXForward/charge_PXDisk_+2',
'PixelPhase1/Tracks/PXForward/charge_PXDisk_+3',
'PixelPhase1/Tracks/PXForward/size_PXDisk_-1',
'PixelPhase1/Tracks/PXForward/size_PXDisk_-2',
'PixelPhase1/Tracks/PXForward/size_PXDisk_-3',
'PixelPhase1/Tracks/PXForward/size_PXDisk_+1',
'PixelPhase1/Tracks/PXForward/size_PXDisk_+2',
'PixelPhase1/Tracks/PXForward/size_PXDisk_+3',

#1D (SiStrip) histograms:
'SiStrip/MechanicalView/MainDiagonal Position',
'SiStrip/MechanicalView/NumberOfClustersInPixel',
'SiStrip/MechanicalView/NumberOfClustersInStrip',
'SiStrip/MechanicalView/TEC/MINUS/wheel_1/NormalizedHitResiduals_TEC__wheel__1',
'SiStrip/MechanicalView/TEC/MINUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__1',
'SiStrip/MechanicalView/TEC/MINUS/wheel_2/NormalizedHitResiduals_TEC__wheel__2',
'SiStrip/MechanicalView/TEC/MINUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__2',
'SiStrip/MechanicalView/TEC/MINUS/wheel_3/NormalizedHitResiduals_TEC__wheel__3',
'SiStrip/MechanicalView/TEC/MINUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__3',
'SiStrip/MechanicalView/TEC/MINUS/wheel_4/NormalizedHitResiduals_TEC__wheel__4',
'SiStrip/MechanicalView/TEC/MINUS/wheel_4/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__4',
'SiStrip/MechanicalView/TEC/MINUS/wheel_5/NormalizedHitResiduals_TEC__wheel__5',
'SiStrip/MechanicalView/TEC/MINUS/wheel_5/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__5',
'SiStrip/MechanicalView/TEC/MINUS/wheel_6/NormalizedHitResiduals_TEC__wheel__6',
'SiStrip/MechanicalView/TEC/MINUS/wheel_6/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__6',
'SiStrip/MechanicalView/TEC/MINUS/wheel_7/NormalizedHitResiduals_TEC__wheel__7',
'SiStrip/MechanicalView/TEC/MINUS/wheel_7/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__7',
'SiStrip/MechanicalView/TEC/MINUS/wheel_8/NormalizedHitResiduals_TEC__wheel__8',
'SiStrip/MechanicalView/TEC/MINUS/wheel_8/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__8',
'SiStrip/MechanicalView/TEC/MINUS/wheel_9/NormalizedHitResiduals_TEC__wheel__9',
'SiStrip/MechanicalView/TEC/MINUS/wheel_9/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__9',
'SiStrip/MechanicalView/TEC/PLUS/wheel_1/NormalizedHitResiduals_TEC__wheel__1',
'SiStrip/MechanicalView/TEC/PLUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__1',
'SiStrip/MechanicalView/TEC/PLUS/wheel_2/NormalizedHitResiduals_TEC__wheel__2',
'SiStrip/MechanicalView/TEC/PLUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__2',
'SiStrip/MechanicalView/TEC/PLUS/wheel_3/NormalizedHitResiduals_TEC__wheel__3',
'SiStrip/MechanicalView/TEC/PLUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__3',
'SiStrip/MechanicalView/TEC/PLUS/wheel_4/NormalizedHitResiduals_TEC__wheel__4',
'SiStrip/MechanicalView/TEC/PLUS/wheel_4/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__4',
'SiStrip/MechanicalView/TEC/PLUS/wheel_5/NormalizedHitResiduals_TEC__wheel__5',
'SiStrip/MechanicalView/TEC/PLUS/wheel_5/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__5',
'SiStrip/MechanicalView/TEC/PLUS/wheel_6/NormalizedHitResiduals_TEC__wheel__6',
'SiStrip/MechanicalView/TEC/PLUS/wheel_6/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__6',
'SiStrip/MechanicalView/TEC/PLUS/wheel_7/NormalizedHitResiduals_TEC__wheel__7',
'SiStrip/MechanicalView/TEC/PLUS/wheel_7/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__7',
'SiStrip/MechanicalView/TEC/PLUS/wheel_8/NormalizedHitResiduals_TEC__wheel__8',
'SiStrip/MechanicalView/TEC/PLUS/wheel_8/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__8',
'SiStrip/MechanicalView/TEC/PLUS/wheel_9/NormalizedHitResiduals_TEC__wheel__9',
'SiStrip/MechanicalView/TEC/PLUS/wheel_9/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__9',
'SiStrip/MechanicalView/TIB/layer_1/NormalizedHitResiduals_TIB__Layer__1',
'SiStrip/MechanicalView/TIB/layer_1/Summary_ClusterStoNCorr__OnTrack__TIB__layer__1',
'SiStrip/MechanicalView/TIB/layer_2/NormalizedHitResiduals_TIB__Layer__2',
'SiStrip/MechanicalView/TIB/layer_2/Summary_ClusterStoNCorr__OnTrack__TIB__layer__2',
'SiStrip/MechanicalView/TIB/layer_3/NormalizedHitResiduals_TIB__Layer__3',
'SiStrip/MechanicalView/TIB/layer_3/Summary_ClusterStoNCorr__OnTrack__TIB__layer__3',
'SiStrip/MechanicalView/TIB/layer_4/NormalizedHitResiduals_TIB__Layer__4',
'SiStrip/MechanicalView/TIB/layer_4/Summary_ClusterStoNCorr__OnTrack__TIB__layer__4',
'SiStrip/MechanicalView/TID/MINUS/wheel_1/NormalizedHitResiduals_TID__wheel__1',
'SiStrip/MechanicalView/TID/MINUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__1',
'SiStrip/MechanicalView/TID/MINUS/wheel_2/NormalizedHitResiduals_TID__wheel__2',
'SiStrip/MechanicalView/TID/MINUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__2',
'SiStrip/MechanicalView/TID/MINUS/wheel_3/NormalizedHitResiduals_TID__wheel__3',
'SiStrip/MechanicalView/TID/MINUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__3',
'SiStrip/MechanicalView/TID/PLUS/wheel_1/NormalizedHitResiduals_TID__wheel__1',
'SiStrip/MechanicalView/TID/PLUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__1',
'SiStrip/MechanicalView/TID/PLUS/wheel_2/NormalizedHitResiduals_TID__wheel__2',
'SiStrip/MechanicalView/TID/PLUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__2',
'SiStrip/MechanicalView/TID/PLUS/wheel_3/NormalizedHitResiduals_TID__wheel__3',
'SiStrip/MechanicalView/TID/PLUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__3',
'SiStrip/MechanicalView/TOB/layer_1/NormalizedHitResiduals_TOB__Layer__1',
'SiStrip/MechanicalView/TOB/layer_1/Summary_ClusterStoNCorr__OnTrack__TOB__layer__1',
'SiStrip/MechanicalView/TOB/layer_2/NormalizedHitResiduals_TOB__Layer__2',
'SiStrip/MechanicalView/TOB/layer_2/Summary_ClusterStoNCorr__OnTrack__TOB__layer__2',
'SiStrip/MechanicalView/TOB/layer_3/,NormalizedHitResiduals_TOB__Layer__3',
'SiStrip/MechanicalView/TOB/layer_3/,Summary_ClusterStoNCorr__OnTrack__TOB__layer__3',
'SiStrip/MechanicalView/TOB/layer_4/,NormalizedHitResiduals_TOB__Layer__4',
'SiStrip/MechanicalView/TOB/layer_4/,Summary_ClusterStoNCorr__OnTrack__TOB__layer__4',
'SiStrip/MechanicalView/TOB/layer_5/,NormalizedHitResiduals_TOB__Layer__5',
'SiStrip/MechanicalView/TOB/layer_5/,Summary_ClusterStoNCorr__OnTrack__TOB__layer__5',
'SiStrip/MechanicalView/TOB/layer_6/,NormalizedHitResiduals_TOB__Layer__6',
'SiStrip/MechanicalView/TOB/layer_6/,Summary_ClusterStoNCorr__OnTrack__TOB__layer__6',
'SiStrip/MechanicalView/TEC/MINUS/wheel_1/Summary_TotalNumberOfDigis__TEC__MINUS__wheel__1',
'SiStrip/MechanicalView/TEC/MINUS/wheel_2/Summary_TotalNumberOfDigis__TEC__MINUS__wheel__2',
'SiStrip/MechanicalView/TEC/MINUS/wheel_3/Summary_TotalNumberOfDigis__TEC__MINUS__wheel__3',
'SiStrip/MechanicalView/TEC/MINUS/wheel_4/Summary_TotalNumberOfDigis__TEC__MINUS__wheel__4',
'SiStrip/MechanicalView/TEC/MINUS/wheel_5/Summary_TotalNumberOfDigis__TEC__MINUS__wheel__5',
'SiStrip/MechanicalView/TEC/MINUS/wheel_6/Summary_TotalNumberOfDigis__TEC__MINUS__wheel__6',
'SiStrip/MechanicalView/TEC/MINUS/wheel_7/Summary_TotalNumberOfDigis__TEC__MINUS__wheel__7',
'SiStrip/MechanicalView/TEC/MINUS/wheel_8/Summary_TotalNumberOfDigis__TEC__MINUS__wheel__8',
'SiStrip/MechanicalView/TEC/MINUS/wheel_9/Summary_TotalNumberOfDigis__TEC__MINUS__wheel__9',
'SiStrip/MechanicalView/TED/PLUS/wheel_1/Summary_TotalNumberOfDigis__TEC__PLUS__wheel__1',
'SiStrip/MechanicalView/TED/PLUS/wheel_2/Summary_TotalNumberOfDigis__TEC__PLUS__wheel__2',
'SiStrip/MechanicalView/TED/PLUS/wheel_3/Summary_TotalNumberOfDigis__TEC__PLUS__wheel__3',
'SiStrip/MechanicalView/TED/PLUS/wheel_4/Summary_TotalNumberOfDigis__TEC__PLUS__wheel__4',
'SiStrip/MechanicalView/TED/PLUS/wheel_5/Summary_TotalNumberOfDigis__TEC__PLUS__wheel__5',
'SiStrip/MechanicalView/TED/PLUS/wheel_6/Summary_TotalNumberOfDigis__TEC__PLUS__wheel__6',
'SiStrip/MechanicalView/TED/PLUS/wheel_7/Summary_TotalNumberOfDigis__TEC__PLUS__wheel__7',
'SiStrip/MechanicalView/TED/PLUS/wheel_8/Summary_TotalNumberOfDigis__TEC__PLUS__wheel__8',
'SiStrip/MechanicalView/TED/PLUS/wheel_9/Summary_TotalNumberOfDigis__TEC__PLUS__wheel__9',
'SiStrip/MechanicalView/TIB/layer_1/Summary_TotalNumberOfDigis__TIB__layer__1',
'SiStrip/MechanicalView/TIB/layer_2/Summary_TotalNumberOfDigis__TIB__layer__2',
'SiStrip/MechanicalView/TIB/layer_3/Summary_TotalNumberOfDigis__TIB__layer__3',
'SiStrip/MechanicalView/TIB/layer_4/Summary_TotalNumberOfDigis__TIB__layer__4',
'SiStrip/MechanicalView/TID/MINUS/wheel_1/Summary_TotalNumberOfDigis__TID__MINUS__wheel__1',
'SiStrip/MechanicalView/TID/MINUS/wheel_2/Summary_TotalNumberOfDigis__TID__MINUS__wheel__2',
'SiStrip/MechanicalView/TID/MINUS/wheel_3/Summary_TotalNumberOfDigis__TID__MINUS__wheel__3',
'SiStrip/MechanicalView/TID/PLUS/wheel_1/Summary_TotalNumberOfDigis__TID__PLUS__wheel__1',
'SiStrip/MechanicalView/TID/PLUS/wheel_2/Summary_TotalNumberOfDigis__TID__PLUS__wheel__2',
'SiStrip/MechanicalView/TID/PLUS/wheel_3/Summary_TotalNumberOfDigis__TID__PLUS__wheel__3',
'SiStrip/MechanicalView/TOB/layer_1/Summary_TotalNumberOfDigis__TOB__layer__1',
'SiStrip/MechanicalView/TOB/layer_2/Summary_TotalNumberOfDigis__TOB__layer__2',
'SiStrip/MechanicalView/TOB/layer_3/Summary_TotalNumberOfDigis__TOB__layer__3',
'SiStrip/MechanicalView/TOB/layer_4/Summary_TotalNumberOfDigis__TOB__layer__4',
'SiStrip/MechanicalView/TOB/layer_5/Summary_TotalNumberOfDigis__TOB__layer__5',
'SiStrip/MechanicalView/TOB/layer_6/Summary_TotalNumberOfDigis__TOB__layer__6',

#2D (SiStrip) histograms:
'SiStrip/MechanicalView/StripClusVsPixClus',
'SiStrip/MechanicalView/TEC/MINUS/wheel_1/Summary_ClusterPosition2D__OnTrack__TEC__MINUS__wheel__1',
'SiStrip/MechanicalView/TEC/MINUS/wheel_2/Summary_ClusterPosition2D__OnTrack__TEC__MINUS__wheel__2',
'SiStrip/MechanicalView/TEC/MINUS/wheel_3/Summary_ClusterPosition2D__OnTrack__TEC__MINUS__wheel__3',
'SiStrip/MechanicalView/TEC/MINUS/wheel_4/Summary_ClusterPosition2D__OnTrack__TEC__MINUS__wheel__4',
'SiStrip/MechanicalView/TEC/MINUS/wheel_5/Summary_ClusterPosition2D__OnTrack__TEC__MINUS__wheel__5',
'SiStrip/MechanicalView/TEC/MINUS/wheel_6/Summary_ClusterPosition2D__OnTrack__TEC__MINUS__wheel__6',
'SiStrip/MechanicalView/TEC/MINUS/wheel_7/Summary_ClusterPosition2D__OnTrack__TEC__MINUS__wheel__7',
'SiStrip/MechanicalView/TEC/MINUS/wheel_8/Summary_ClusterPosition2D__OnTrack__TEC__MINUS__wheel__8',
'SiStrip/MechanicalView/TEC/MINUS/wheel_9/Summary_ClusterPosition2D__OnTrack__TEC__MINUS__wheel__9',
'SiStrip/MechanicalView/TEC/PLUS/wheel_1/Summary_ClusterPosition2D__OnTrack__TEC__PLUS__wheel__1',
'SiStrip/MechanicalView/TEC/PLUS/wheel_2/Summary_ClusterPosition2D__OnTrack__TEC__PLUS__wheel__2',
'SiStrip/MechanicalView/TEC/PLUS/wheel_3/Summary_ClusterPosition2D__OnTrack__TEC__PLUS__wheel__3',
'SiStrip/MechanicalView/TEC/PLUS/wheel_4/Summary_ClusterPosition2D__OnTrack__TEC__PLUS__wheel__4',
'SiStrip/MechanicalView/TEC/PLUS/wheel_5/Summary_ClusterPosition2D__OnTrack__TEC__PLUS__wheel__5',
'SiStrip/MechanicalView/TEC/PLUS/wheel_6/Summary_ClusterPosition2D__OnTrack__TEC__PLUS__wheel__6',
'SiStrip/MechanicalView/TEC/PLUS/wheel_7/Summary_ClusterPosition2D__OnTrack__TEC__PLUS__wheel__7',
'SiStrip/MechanicalView/TEC/PLUS/wheel_8/Summary_ClusterPosition2D__OnTrack__TEC__PLUS__wheel__8',
'SiStrip/MechanicalView/TEC/PLUS/wheel_9/Summary_ClusterPosition2D__OnTrack__TEC__PLUS__wheel__9',
'SiStrip/MechanicalView/TIB/layer_1/Summary_ClusterPosition2D__OnTrack__TIB__layer__1',
'SiStrip/MechanicalView/TIB/layer_2/Summary_ClusterPosition2D__OnTrack__TIB__layer__2',
'SiStrip/MechanicalView/TIB/layer_3/Summary_ClusterPosition2D__OnTrack__TIB__layer__3',
'SiStrip/MechanicalView/TIB/layer_4/Summary_ClusterPosition2D__OnTrack__TIB__layer__4',
'SiStrip/MechanicalView/TID/MINUS/wheel_1/Summary_ClusterPosition2D__OnTrack__TID__MINUS__wheel__1',
'SiStrip/MechanicalView/TID/MINUS/wheel_2/Summary_ClusterPosition2D__OnTrack__TID__MINUS__wheel__2',
'SiStrip/MechanicalView/TID/MINUS/wheel_3/Summary_ClusterPosition2D__OnTrack__TID__MINUS__wheel__3',
'SiStrip/MechanicalView/TID/PLUS/wheel_1/Summary_ClusterPosition2D__OnTrack__TID__PLUS__wheel__1',
'SiStrip/MechanicalView/TID/PLUS/wheel_2/Summary_ClusterPosition2D__OnTrack__TID__PLUS__wheel__2',
'SiStrip/MechanicalView/TID/PLUS/wheel_3/Summary_ClusterPosition2D__OnTrack__TID__PLUS__wheel__3',
'SiStrip/MechanicalView/TOB/layer_1/Summary_ClusterPosition2D__OnTrack__TOB__layer__1',
'SiStrip/MechanicalView/TOB/layer_2/Summary_ClusterPosition2D__OnTrack__TOB__layer__2',
'SiStrip/MechanicalView/TOB/layer_3/Summary_ClusterPosition2D__OnTrack__TOB__layer__3',
'SiStrip/MechanicalView/TOB/layer_4/Summary_ClusterPosition2D__OnTrack__TOB__layer__4',
'SiStrip/MechanicalView/TOB/layer_5/Summary_ClusterPosition2D__OnTrack__TOB__layer__5',
'SiStrip/MechanicalView/TOB/layer_6/Summary_ClusterPosition2D__OnTrack__TOB__layer__6',

#1D (Tracking) histograms:
'Tracking/PrimaryVertices/highPurityTracks/pt_0to1/offline/NumberOfGoodPVtx_offline',
'Tracking/TrackParameters/generalTracks/LSanalysis/Chi2oNDF_lumiFlag_GenTk',
'Tracking/TrackParameters/generalTracks/LSanalysis/NumberOfRecHitsPerTrack_lumiFlag_GenTk',
'Tracking/TrackParameters/generalTracks/LSanalysis/NumberOfTracks_lumiFlag_GenTk',
'Tracking/TrackParameters/highPurityTracks/pt_0to1/LSanalysis/Chi2oNDF_lumiFlag_GenTk',
'Tracking/TrackParameters/highPurityTracks/pt_0to1/LSanalysis/NumberOfRecHitsPerTrack_lumiFlag_GenTk',
'Tracking/TrackParameters/highPurityTracks/pt_0to1/LSanalysis/NumberOfTracks_lumiFlag_GenTk',
'Tracking/TrackParameters/generalTracks/GeneralProperties/DistanceOfClosestApproachErrorVsDxy_GenTk',
'Tracking/TrackParameters/generalTracks/GeneralProperties/SIPDxyToBS_GenTk',
'Tracking/TrackParameters/generalTracks/GeneralProperties/SIPDxyToPV_GenTk',
'Tracking/TrackParameters/generalTracks/GeneralProperties/Chi2Prob_GenTk',
'Tracking/TrackParameters/generalTracks/GeneralProperties/Chi2oNDF_GenTk',
'Tracking/TrackParameters/generalTracks/GeneralProperties/NumberOfMeanLayersPerTrack_GenTk',
'Tracking/TrackParameters/generalTracks/GeneralProperties/NumberOfMeanRecHitsPerTrack_GenTk',
'Tracking/TrackParameters/generalTracks/GeneralProperties/TrackEtaErr_ImpactPoint_GenTk',
'Tracking/TrackParameters/generalTracks/GeneralProperties/TrackPtErr_ImpactPoint_GenTk',
'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/DistanceOfClosestApproachErrorVsDxy_GenTk',
'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/SIPDxyToBS_GenTk',
'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/SIPDxyToPV_GenTk',
'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/Chi2Prob_GenTk',
'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/Chi2oNDF_GenTk',
'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/NumberOfMeanLayersPerTrack_GenTk',
'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/NumberOfMeanRecHitsPerTrack_GenTk',
'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/TrackEtaErr_ImpactPoint_GenTk',
'Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/TrackPtErr_ImpactPoint_GenTk',
'Tracking/TrackParameters/highPurityTracks/pt_1/dzPV0p1/GeneralProperties/DistanceOfClosestApproachErrorVsDxy_GenTk',
'Tracking/TrackParameters/highPurityTracks/pt_1/dzPV0p1/GeneralProperties/SIPDxyToBS_GenTk',
'Tracking/TrackParameters/highPurityTracks/pt_1/dzPV0p1/GeneralProperties/SIPDxyToPV_GenTk',
'Tracking/TrackParameters/highPurityTracks/pt_1/dzPV0p1/GeneralProperties/Chi2Prob_GenTk',
'Tracking/TrackParameters/highPurityTracks/pt_1/dzPV0p1/GeneralProperties/Chi2oNDF_GenTk',
'Tracking/TrackParameters/highPurityTracks/pt_1/dzPV0p1/GeneralProperties/NumberOfMeanLayersPerTrack_GenTk',
'Tracking/TrackParameters/highPurityTracks/pt_1/dzPV0p1/GeneralProperties/NumberOfMeanRecHitsPerTrack_GenTk',
'Tracking/TrackParameters/highPurityTracks/pt_1/dzPV0p1/GeneralProperties/TrackEtaErr_ImpactPoint_GenTk',
'Tracking/TrackParameters/highPurityTracks/pt_1/dzPV0p1/GeneralProperties/TrackPtErr_ImpactPoint_GenTk',
'Tracking/TrackParameters/generalTracks/HitProperties/NumberMIRecHitsPerTrackVsPt_GenTk',
'Tracking/TrackParameters/generalTracks/HitProperties/NumberMORecHitsPerTrackVsPt_GenTk',
'Tracking/TrackParameters/generalTracks/HitProperties/NumberOf3DLayersPerTrack_GenTk',
'Tracking/TrackParameters/generalTracks/HitProperties/NumberOfValidRecHitPerTrack_GenTk',
'Tracking/TrackParameters/highPurityTracks/pt_1/HitProperties/NumberMIRecHitsPerTrackVsPt_GenTk',
'Tracking/TrackParameters/highPurityTracks/pt_1/HitProperties/NumberMORecHitsPerTrackVsPt_GenTk',
'Tracking/TrackParameters/highPurityTracks/pt_1/HitProperties/NumberOf3DLayersPerTrack_GenTk',
'Tracking/TrackParameters/highPurityTracks/pt_1/HitProperties/NumberOfValidRecHitPerTrack_GenTk',

#All the MEs (96) in:
'Tracking/TrackParameters/generalTracks/GeneralProperties/'
              )
      )
)
