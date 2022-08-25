import FWCore.ParameterSet.Config as cms

l1pfProducerHGCalNoTK = cms.EDProducer("L1TPFProducer",
    debug = cms.untracked.int32(0),
    emClusters = cms.VInputTag(),
    emPtCut = cms.double(0.5),
    etaCharged = cms.double(2.5),
    hadClusters = cms.VInputTag(cms.InputTag("pfClustersFromHGC3DClusters")),
    hadPtCut = cms.double(1.0),
    linking = cms.PSet(
        caloEmPtMinFrac = cms.double(0.5),
        caloReLink = cms.bool(False),
        caloReLinkDR = cms.double(0.3),
        caloReLinkThreshold = cms.double(0.5),
        ecalPriority = cms.bool(False),
        emCaloDR = cms.double(0.1),
        emCaloSubtractionPtSlope = cms.double(1.2),
        emCaloUseAlsoCaloSigma = cms.bool(True),
        maxInvisiblePt = cms.double(10.0),
        rescaleTracks = cms.bool(False),
        rescaleUnmatchedTrack = cms.bool(False),
        sumTkCaloErr2 = cms.bool(True),
        tightTrackMaxChi2 = cms.double(50),
        tightTrackMaxInvisiblePt = cms.double(20),
        tightTrackMinStubs = cms.uint32(6),
        trackCaloDR = cms.double(0.1),
        trackCaloLinkMetric = cms.string('bestByDRPt'),
        trackCaloNSigmaHigh = cms.double(1.0),
        trackCaloNSigmaLow = cms.double(2.0),
        trackEmDR = cms.double(0.04),
        trackEmMayUseCaloMomenta = cms.bool(True),
        trackEmUseAlsoTrackSigma = cms.bool(True),
        trackMuDR = cms.double(0.2),
        trackMuMatch = cms.string('boxBestByPtRatio'),
        useCaloTrkWeightedAverage = cms.bool(False),
        useTrackCaloSigma = cms.bool(True)
    ),
    muons = cms.InputTag("simGmtStage2Digis"),
    pfAlgo = cms.string('PFAlgo2HGC'),
    puAlgo = cms.string('LinearizedPuppi'),
    puppiAlphaCrops = cms.vdouble(3, 3, 4),
    puppiAlphaCropsPhotons = cms.vdouble(3, 3, 4),
    puppiAlphaSlopes = cms.vdouble(1.5, 1.5, 2.2),
    puppiAlphaSlopesPhotons = cms.vdouble(1.5, 1.5, 2.2),
    puppiAlphaZeros = cms.vdouble(6.0, 6.0, 9.0),
    puppiAlphaZerosPhotons = cms.vdouble(6.0, 6.0, 9.0),
    puppiDr = cms.double(0.3),
    puppiDrMin = cms.double(0.04),
    puppiEtaCuts = cms.vdouble(2.0, 2.4, 3.1),
    puppiPriors = cms.vdouble(5.0, 5.0, 7.0),
    puppiPriorsPhotons = cms.vdouble(1.5, 1.5, 5.0),
    puppiPtCuts = cms.vdouble(1.0, 2.0, 4.0),
    puppiPtCutsPhotons = cms.vdouble(1.0, 2.0, 4.0),
    puppiPtMax = cms.double(50.0),
    puppiPtSlopes = cms.vdouble(0.3, 0.3, 0.3),
    puppiPtSlopesPhotons = cms.vdouble(0.4, 0.4, 0.4),
    puppiPtZeros = cms.vdouble(5.0, 7.0, 9.0),
    puppiPtZerosPhotons = cms.vdouble(3.0, 4.0, 5.0),
    puppiUsingBareTracks = cms.bool(True),
    regions = cms.VPSet(
        cms.PSet(
            etaBoundaries = cms.vdouble(-3, -2.5),
            etaExtra = cms.double(0.3),
            phiExtra = cms.double(0.0),
            phiSlices = cms.uint32(1)
        ),
        cms.PSet(
            etaBoundaries = cms.vdouble(2.5, 3),
            etaExtra = cms.double(0.3),
            phiExtra = cms.double(0.0),
            phiSlices = cms.uint32(1)
        )
    ),
    tkMuons = cms.InputTag("L1TkMuonsGmt"),
    trackRegionMode = cms.string('atCalo'),
    tracks = cms.InputTag("pfTracksFromL1TracksHGCal"),
    trkMaxChi2 = cms.double(15),
    trkMinStubs = cms.uint32(4),
    trkPtCut = cms.double(2.0),
    useRelativeRegionalCoordinates = cms.bool(False),
    useStandaloneMuons = cms.bool(True),
    useTrackerMuons = cms.bool(False),
    vtxAdaptiveCut = cms.bool(True),
    vtxAlgo = cms.string('external'),
    vtxCollection = cms.InputTag("L1TkPrimaryVertex"),
    vtxFormat = cms.string('TkPrimaryVertex'),
    vtxRes = cms.double(0.333)
)
